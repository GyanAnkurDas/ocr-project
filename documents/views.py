from django.shortcuts import render, redirect, get_object_or_404
from .models import Document
from .utils.preprocess import preprocess_image
from .utils.ocr_engine import extract_text
from .utils.validator import validate_text
from .utils.file_processor import get_file_type, process_file
import cv2
import tempfile
import os


def upload_document(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('file')
        title = request.POST.get('title', 'Untitled')

        if not uploaded_file:
            return render(request, 'documents/upload.html',
                        {'error': 'Please select a file.'})

        file_type = get_file_type(uploaded_file.name)

        if file_type == 'unknown':
            return render(request, 'documents/upload.html',
                        {'error': 'Unsupported file type.'})

        doc = Document(title=title, file=uploaded_file, file_type=file_type)
        doc.save()

        file_path = doc.file.path

        if file_type == 'image':
            # Run through OpenCV + PaddleOCR pipeline
            processed = preprocess_image(file_path)
            with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as tmp:
                cv2.imwrite(tmp.name, processed)
                raw_items = extract_text(tmp.name)
                os.unlink(tmp.name)
            doc.extracted_text = validate_text(raw_items)
        else:
            # Directly extract text from the file
            doc.extracted_text = process_file(file_path, file_type)

        doc.save()
        return redirect('document_detail', pk=doc.pk)

    return render(request, 'documents/upload.html')


def document_detail(request, pk):
    doc = get_object_or_404(Document, pk=pk)
    return render(request, 'documents/detail.html', {'doc': doc})


def search_documents(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        results = Document.objects.filter(
            extracted_text__icontains=query
        ).order_by('-uploaded_at')
    return render(request, 'documents/search.html', {
        'results': results,
        'query': query
    })
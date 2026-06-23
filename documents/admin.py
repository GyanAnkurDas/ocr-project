from django.contrib import admin
from .models import Document

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'file_type', 'uploaded_at']
    search_fields = ['title', 'extracted_text']
    list_filter = ['file_type']
    readonly_fields = ['extracted_text', 'uploaded_at']
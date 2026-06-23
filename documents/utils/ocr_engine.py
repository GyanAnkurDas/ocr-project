from paddleocr import PaddleOCR

# Initialize once (downloading models on first run — takes time)
ocr = PaddleOCR(use_angle_cls=True, lang='en')

def extract_text(image_path):
    result = ocr.ocr(image_path, cls=True)
    extracted = []
    for line in result[0]:
        text = line[1][0]
        confidence = line[1][1]
        extracted.append({
            'text': text,
            'confidence': confidence
        })
    return extracted
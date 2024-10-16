import fitz  # PyMuPDF

def extract_text_and_images_from_pdf(pdf_path):
    questions = []
    doc = fitz.open(pdf_path)
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text()
        images = page.get_images(full=True)
        
        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            # You can save the image if needed
            
        questions.append({"text": text.strip(), "page": page_num + 1})  # Save question text
        
    return questions

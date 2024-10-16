import fitz  # PyMuPDF

def extract_text_and_images_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    questions = []

    for page in doc:
        text = page.get_text()
        images = page.get_images(full=True)

        # Collecting text and images
        if text:
            questions.append({'text': text.strip(), 'images': images})

    doc.close()
    
    # Return the list of questions and images extracted
    return questions

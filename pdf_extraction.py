import fitz  # PyMuPDF for PDF extraction
from PIL import Image  # For image processing
import io  # To handle byte streams

# Function to extract text and images from PDF
def extract_text_and_images_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    questions = []
    
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        
        # Extract text from the page
        text = page.get_text("text")
        questions.append({'text': text, 'images': []})
        
        # Extract images from the page
        image_list = page.get_images(full=True)
        
        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image = Image.open(io.BytesIO(image_bytes))
            
            # Save images to process later
            image.save(f"image_{page_num}_{img_index}.{image_ext}")
            questions[-1]['images'].append(image)
    
    return questions

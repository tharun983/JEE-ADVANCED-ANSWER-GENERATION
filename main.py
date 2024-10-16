from fpdf import FPDF  # To create a PDF
from pdf_extraction import extract_text_and_images_from_pdf  # Import PDF extraction
from answer_generation import generate_answer  # Import answer generation

# PDF generation class
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Question and Answer Sheet', 0, 1, 'C')

    def add_question_and_answer(self, question, answer):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, f'Q: {question}')
        self.multi_cell(0, 10, f'A: {answer}')
        self.ln()

    def add_image(self, image_path):
        self.image(image_path, w=100, h=100)
        self.ln()

# Function to create a PDF with extracted questions and generated answers
def create_pdf_with_answers(output_pdf_path, questions):
    pdf = PDF()
    pdf.add_page()
    
    for idx, q in enumerate(questions):
        question_text = q['text']
        answer = generate_answer(question_text)
        
        # Add question and answer to the PDF
        pdf.add_question_and_answer(question_text, answer)
        
        # If there are images associated with the question
        if q['images']:
            for img_idx, img in enumerate(q['images']):
                img_path = f'image_{idx}_{img_idx}.png'
                img.save(img_path)  # Save image temporarily to insert in PDF
                pdf.add_image(img_path)
    
    # Output the final PDF
    pdf.output(output_pdf_path)

# Main function to process the PDF and generate output with answers
def main():
    input_pdf_path = 'input_question_paper.pdf'  # Input PDF with questions
    output_pdf_path = 'output_with_answers.pdf'  # Output PDF to save answers
    
    # Extract questions and images from the PDF
    questions = extract_text_and_images_from_pdf(input_pdf_path)

    for q in questions:
        print("Extracted Question:", q['text'])  # This will show the extracted questions
    
    # Create a PDF with generated answers
    create_pdf_with_answers(output_pdf_path, questions)

if __name__ == '__main__':
    main()

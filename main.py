import os
from pdf_extraction import extract_text_and_images_from_pdf
from answer_generation import generate_answer
from fpdf import FPDF
import re

def clean_text(text):
    # Remove or replace problematic characters
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)  # Remove non-ASCII characters
    text = text.replace('\u2022', '*')  # Replace bullet with asterisk
    text = text.replace('\u2212', '-')  # Replace minus sign with hyphen
    # Add more replacements as needed
    return text.strip()

def create_pdf_with_answers(output_pdf_path, questions):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for question in questions:
        question_text = clean_text(question['text'])  # Clean the question text
        answer = generate_answer(question_text)  # Generate answer
        # Add question and answer to PDF
        pdf.multi_cell(0, 10, f"Question: {question_text}")
        pdf.multi_cell(0, 10, f"Answer: {answer}")
        pdf.ln(10)  # Add a line break

    pdf.output(output_pdf_path, 'F')

def main():
    input_pdf_path = 'input_question_paper.pdf'  # Replace with your input PDF file
    output_pdf_path = 'output_answers.pdf'

    # Extract questions and images from the PDF
    questions = extract_text_and_images_from_pdf(input_pdf_path)

    # Check if questions were extracted
    if not questions:
        print("No questions extracted.")
        return

    print(f"Extracted {len(questions)} questions.")
    create_pdf_with_answers(output_pdf_path, questions)

if __name__ == "__main__":
    main()

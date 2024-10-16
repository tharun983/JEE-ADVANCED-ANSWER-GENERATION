from pdf_extraction import extract_text_and_images_from_pdf
from answer_generation import generate_answer
import sys

def main():
    input_pdf_path = "input_question_paper.pdf"  # Update with your actual PDF path
    output_pdf_path = "output_answers.pdf"

    questions = extract_text_and_images_from_pdf(input_pdf_path)

    # Write extracted questions to a file
    with open('extracted_questions.txt', 'w', encoding='utf-8') as f:
        for q in questions:
            question_text = q['text']
            f.write(question_text + '\n')  # Write to the file in UTF-8 encoding

    print("Extracted questions written to 'extracted_questions.txt'")

if __name__ == "__main__":
    main()


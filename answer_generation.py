import cohere

# Initialize the Cohere client
cohere_client = cohere.Client('API KEY')  # Replace with your actual Cohere API key

def generate_answer(question_text):
    try:
        response = cohere_client.generate(
            model='command-r-plus',  # Ensure this model is available to your API key
            prompt=f"Provide a detailed answer for the following question:\n{question_text}\nAnswer:",
            max_tokens=150,
            temperature=0.5,
            stop_sequences=["\n"]
        )
        return response.generations[0].text.strip()
    except Exception as e:
        print(f"Error generating answer: {e}")
        return "Answer not found."

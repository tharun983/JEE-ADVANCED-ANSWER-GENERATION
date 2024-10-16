import cohere

# Initialize the Cohere client
co = cohere.Client('8wgcLA8KR8GmgAHaM73oaE7I6mgx6lRuTVdqWKkN')  # Replace with your actual API key

def generate_answer(question_text):
    response = co.generate(
        model='command-r-plus',  # Specify the model to use
        prompt=f"Answer the following question:\n\n{question_text}\n\nAnswer:",
        max_tokens=100,  # Adjust the number of tokens based on your needs
        temperature=0.7,  # Control the creativity of the response
        stop_sequences=["\n"]  # Stop generating at a new line
    )
    
    answer = response.generations[0].text.strip()
    return answer

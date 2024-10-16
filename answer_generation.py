import ollama  # For generating answers using Ollama API

# Function to generate answers using Ollama API
def generate_answer(question_text):
    response = ollama.chat(
        model="llama2",  # You can specify other models available in Ollama
        messages=[{"role": "user", "content": f"Provide the correct answer and explanation for the following question: {question_text}"}]
    )
    
    # Extract the answer from the response
    answer = response['message'].strip()
    return answer

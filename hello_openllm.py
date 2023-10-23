import openllm

# Constants
SERVER = 'http://localhost:3000'

# Question
question = 'What is LLM?'

client = openllm.client.HTTPClient(SERVER)
answer = client.query(question)

# Print Results to Terminal
print(f"Question: {question}\n Result: {answer}")
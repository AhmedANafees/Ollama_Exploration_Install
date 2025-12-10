from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model="gemma3:1b", messages=[
        {
            'role': 'user',
            'content': 'what is the infamous line said by hamlet in shakespeare\'s play?'
        },
])

# Handle encoding properly for Windows terminal
content = response['message']['content']
# Convert Unicode to ASCII, replacing special chars with closest equivalent
content = content.encode('ascii', errors='replace').decode('ascii')
print(content)

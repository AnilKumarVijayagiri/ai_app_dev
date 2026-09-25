from google import genai
from google.genai import types
import numpy as np

client = genai.Client(api_key="AQ.Ab8RN6JhtdIZtEw5L2nGyoSteNVm_lxf7Ey8aGO4vlC9QU9fZw")
with open("raamayana.txt", "r",encoding="utf=8") as file:
    ramayana_text = file.read()
print("My EPIC AI")
print("Welcome to Epic AI, your personal AI researcher!")
print("Ask anything")
print("Type 'exit' to end the conversation.")
while True:
    question = input("You: ")
    if question.lower() == 'exit':
        print("EPIC AI: Goodbye!")
        break
    prompt=f"""
You are my personal AI researcher. 
Use the information about Ramayana below to answer the user's questions.
If something is not mentioned in the information, you can say "I don't know" or "I don't have that information".
Do not make up any information.
My information: {ramayana_text}
My questions: {question}
"""
    
    response=client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )
    print("\n EPIC AI: ",response.text)
from openai import OpenAI
import os


client = OpenAI()

response = client.responses.create(
    model="gpt-4o-mini",
    
    input="Escreva uma piada sobre a linguagem de programação Python"
)

print(response.output_text)
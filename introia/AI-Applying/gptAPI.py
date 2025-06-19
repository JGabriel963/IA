from openai import OpenAI
import os

os.environ['OPENAI_API_KEY'] = "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"

client = OpenAI()

response = client.responses.create(
    model="gpt-4o-mini",
    
    input="Escreva uma piada sobre a linguagem de programação Python"
)

print(response.output_text)
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

def generate_with_gemini(prompt: str, model_name: str):
    client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

    response = client.models.generate_content(
        model=model_name,
        contents=prompt
    )

    return response.text

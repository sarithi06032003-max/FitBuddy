import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_nutrition_tip(details):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"Give short nutrition tip for Goal {details['goal']}, Age {details['age']}, Weight {details['weight']}. 2-3 lines."
    res = model.generate_content(prompt)
    return res.text
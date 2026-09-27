import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def update_workout_plan(original_plan, feedback):
    model = genai.GenerativeModel('gemini-1.5-pro')
    prompt = f"Original plan: {original_plan}. User feedback: {feedback}. Update the plan accordingly and return new JSON."
    res = model.generate_content(prompt)
    return res.text
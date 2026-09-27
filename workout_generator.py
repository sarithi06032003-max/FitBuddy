import google.generativeai as genai
import os, json
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_workout_plan(details):
    model = genai.GenerativeModel('gemini-1.5-pro')
    prompt = f"Create 7-day workout plan for Age {details['age']}, Weight {details['weight']}, Goal {details['goal']}, Level {details['level']}. Return JSON with day1 to day7 each having warmup, main_workout with sets/reps, cooldown."
    res = model.generate_content(prompt)
    text = res.text.replace("```json","").replace("```","").strip()
    return json.loads(text)
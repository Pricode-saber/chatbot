import google.generativeai as genai

from config import API_KEY
from prompts import PROMPTS
from few_shot_examples import FEW_SHOT_EXAMPLES
from utils.intent_classifier import detect_intent
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

print("API KEY:", API_KEY)

API_KEY = os.getenv("GEMINI_API_KEY")
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found. Check your .env file.")

print("Loaded API Key:", API_KEY[:10] + "...")

genai.configure(api_key=API_KEY)

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")


def chatbot(user_input):
    # Detect user intent
    intent = detect_intent(user_input)

    # Get the appropriate prompt
    system_prompt = PROMPTS[intent]
    few_shot = FEW_SHOT_EXAMPLES[intent]

    # Combine prompt + examples + user input
    final_prompt = f"""
{system_prompt}

Here are some examples of good customer support conversations.

{few_shot}

Now respond to the customer professionally.

Customer:
{user_input}

Support:
"""

    # Generate AI response
    response = model.generate_content(final_prompt)

    return response.text

from google import genai
from dotenv import load_dotenv
import os

load_dotenv()


API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(
    api_key=API_KEY
)


SYSTEM_PROMPT = """
You are an expert AI Student Assistant.

You help students with:
- Python
- Data Science
- Machine Learning
- Exams
- Coding
- Career Guidance
- Study Plans

Always give detailed, professional answers.
"""


def ask_ai(user_message):

    try:

        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=[
                SYSTEM_PROMPT,
                user_message
            ]
        )


        if response.text:
            return response.text

        else:
            return "Sorry, I could not generate an answer."


    except Exception as e:

        return f"❌ Gemini Error: {str(e)}"
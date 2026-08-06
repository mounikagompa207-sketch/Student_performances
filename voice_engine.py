from utils.gemini_engine import ask_ai
from gtts import gTTS
import tempfile
import os


def get_voice_response(question):

    try:

        # Gemini response
        answer = ask_ai(question)

        if not answer:
            answer = "Sorry, I could not generate a response."

        # Text to speech
        tts = gTTS(
            text=answer,
            lang="en",
            slow=False
        )

        audio_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp3"
        )

        audio_path = audio_file.name

        audio_file.close()

        tts.save(audio_path)

        return answer, audio_path


    except Exception as e:

        return f"Error: {str(e)}", None
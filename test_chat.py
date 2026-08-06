from utils.gemini_engine import ask_ai

def chatbot_response(user_message):
    response = ask_ai(user_message)
    return response


print(chatbot_response("Hi"))
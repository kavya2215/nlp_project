import speech_recognition as sr
import pyttsx3

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speech_to_text():
    # Capture audio from the microphone
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            # Recognize speech using Google's API
            text = recognizer.recognize_google(audio)
            print(f"User said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            return None

def text_to_speech(response):
    engine.say(response)
    engine.runAndWait()

# Example usage
user_input = speech_to_text()
if user_input:
    chatbot_response = "I'm processing your query."
    text_to_speech(chatbot_response)

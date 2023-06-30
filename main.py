import speech_recognition as sr
import os
from transformers import pipeline

def select_microphone():
    recognizer = sr.Recognizer()
    microphones = sr.Microphone.list_microphone_names()

    print("Available Microphones:")
    for i, mic in enumerate(microphones):
        print(f"{i + 1}. {mic}")

    while True:
        try:
            index = int(input("Enter the index of the microphone you want to use: ")) - 1
            if 0 <= index < len(microphones):
                return index
            else:
                print("Invalid input. Please enter a valid index.")
        except ValueError:
            print("Invalid input. Please enter a valid index.")

def speech_to_text(index, timeout=3):
    recognizer = sr.Recognizer()

    with sr.Microphone(device_index=index) as source:
        print("Listening...")

        # Adjust for ambient noise if necessary
        recognizer.adjust_for_ambient_noise(source)

        # Listen for the wake phrase with a timeout
        audio = recognizer.listen(source, timeout=timeout)

        try:
            # Convert speech to text
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return ""
        except sr.WaitTimeoutError:
            print("No speech detected. Assuming you've finished speaking.")
            return ""

def text_to_speech(text):
    # Save response as a text file
    with open('response.txt', 'w') as file:
        file.write(text)

    # Convert text to speech using your preferred TTS library or service
    # Add your code here to convert the response.txt file to audio

# Set up the text generation pipeline using a language model from Hugging Face
generator = pipeline('text-generation', model='EleutherAI/gpt-neo-1.3B')

# Prompt user to select a microphone
microphone_index = select_microphone()

# Main loop
while True:
    # Listen for wake phrase
    phrase = speech_to_text(microphone_index)

    if phrase == "hey chat":
        print("Listening for the question...")
        # Listen for the user's question
        question = speech_to_text(microphone_index, timeout=3)
        print("Processing the question:", question)

        # Generate response using the language model
        response = generator(question, max_length=50, num_return_sequences=1)[0]['generated_text']

        print("Generating response...")
        # Convert response to speech
        text_to_speech(response)

        print("Response generated and played.")

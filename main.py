import speech_recognition as sr

def recognize_speech_from_mic():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    while True:

        with sr.Microphone() as source:
            print("Please say something...")
            # Adjust for ambient noise and record audio from the microphone
            recognizer.adjust_for_ambient_noise(source)
            # Adjust phrase time limit for window of detection
            audio = recognizer.listen(source, phrase_time_limit=10)

            # Try recognizing the speech using PocketSphinx
            try:
                text = recognizer.recognize_sphinx(audio)
                print(f"You said: {text}")

                # Saving the recognized text to a file
                with open("recognized_text.txt", "a") as file:
                    file.write(text + "\n")
                print("Text saved to recognized_text.txt")

            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio")
            except sr.RequestError as e:
                print(f"Could not request results from Sphinx service; {e}")

        # Check if the user wants to exit or use dictation again
        user_input = input("Press 'r' to repeat, or any other key to exit: ")
        if user_input.lower() != 'r':
            print("Exiting the loop.")
            break

if __name__ == "__main__":
    recognize_speech_from_mic()

import openai
import speech_recognition as sr
import pyttsx3
import snowboydecoder

# Replace with your OpenAI API key
openai.api_key = "your_openai_api_key"

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio, language="en-US")
        return text
    except Exception as e:
        print("Error recognizing speech:", e)
        return None

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.say(text)
    engine.runAndWait()

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )

    return response.choices[0].text.strip()

def detected_callback():
    print("Wake word detected!")
    snowboydecoder.play_audio_file(snowboydecoder.DETECT_DING)
    user_input = recognize_speech()

    if user_input is None:
        return

    print("You said:", user_input)
    if user_input.lower() in ["exit", "stop", "quit"]:
        speak("Goodbye!")
        detector.terminate()

    gpt_response = chat_with_gpt(user_input)
    print("ChatGPT:", gpt_response)
    speak(gpt_response)

def main():
    global detector
    speak("Welcome to your ChatGPT Smart Speaker! I will listen for my wake word.")

    # Change the path to your desired wake word model file (e.g., 'alexa.umdl')
    model = "model/jarvis.umdl"

    # Sensitivity controls how sensitive the wake word detection should be
    sensitivity = [0.5]

    detector = snowboydecoder.HotwordDetector(model, sensitivity=sensitivity)
    print("Listening for wake word...")

    # Main loop
    detector.start(detected_callback=detected_callback, sleep_time=0.03)

if __name__ == "__main__":
    main()

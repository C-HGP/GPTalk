import openai
import speech_recognition as sr
import pyttsx3
from pvporcupine import Porcupine
import pyaudio

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

def main():
    speak("Welcome to your ChatGPT Smart Speaker! I will listen for my wake word.")

    porcupine = None
    pa = None
    audio_stream = None

    try:
        porcupine = Porcupine(keyword_paths=["model/Jarvis_en_windows_v2_2_0.ppn"])
        pa = pyaudio.PyAudio()

        audio_stream = pa.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length,
            input_device_index=None,
        )

        print("Listening for wake word...")

        while True:
            pcm = audio_stream.read(porcupine.frame_length)
            pcm = [int(x) for x in pcm]

            keyword_index = porcupine.process(pcm)

            if keyword_index >= 0:
                print("Wake word detected!")
                user_input = recognize_speech()

                if user_input is None:
                    continue

                print("You said:", user_input)
                if user_input.lower() in ["exit", "stop", "quit"]:
                    speak("Goodbye!")
                    break

                gpt_response = chat_with_gpt(user_input)
                print("ChatGPT:", gpt_response)
                speak(gpt_response)

    finally:
        if audio_stream is not None:
            audio_stream.close()

        if pa is not None:
            pa.terminate()

        if porcupine is not None:
            porcupine.delete()

if __name__ == "__main__":
    main()

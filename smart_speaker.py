import openai
import speech_recognition as sr
import pyttsx3
from pvporcupine import Porcupine
import pyaudio
import struct
import configparser
import os

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

def load_config():
    config_file = "config.ini"
    config = configparser.ConfigParser()
    if not os.path.exists(config_file):
        config["Credentials"] = {
            "OpenAI_API_Key": "",
            "Porcupine_Access_Key": "",
        }
        with open(config_file, "w") as f:
            config.write(f)

    config.read(config_file)
    return config


def main():
    config = load_config()
    openai_api_key = config.get("Credentials", "OpenAI_API_Key")
    porcupine_access_key = config.get("Credentials", "Porcupine_Access_Key")

    if not openai_api_key:
        openai_api_key = input("Enter your OpenAI API Key: ")
        config.set("Credentials", "OpenAI_API_Key", openai_api_key)
        with open("config.ini", "w") as f:
            config.write(f)

    if not porcupine_access_key:
        porcupine_access_key = input("Enter your Porcupine Access Key: ")
        config.set("Credentials", "Porcupine_Access_Key", porcupine_access_key)
        with open("config.ini", "w") as f:
            config.write(f)

    openai.api_key = openai_api_key
    
    speak("Welcome to GPTalk.")

    # Replace "path/to/your/custom_wake_word.ppn" with the path to your downloaded .ppn file
    keyword_path = "model/jarvis_windows.ppn"

    # Replace "path/to/your/porcupine/library" with the path to the downloaded library file
    library_path = "library/libpv_porcupine.dll"

    # Replace "path/to/your/porcupine/model" with the path to the downloaded model file
    model_path = "model/porcupine_params.pv"

    porcupine = None
    pa = None
    audio_stream = None

    try:
        porcupine = Porcupine(
            access_key=porcupine_access_key,
            library_path=library_path,
            model_path=model_path,
            keyword_paths=[keyword_path],
            sensitivities=[0.5]
        )
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
            pcm = audio_stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            keyword_index = porcupine.process(pcm)

            if keyword_index >= 0:
                print("Wake word detected!")
                user_input = recognize_speech()

                if user_input is None:
                    continue

                print("You said:", user_input)
                if user_input.lower() in ["exit", "stop", "quit"]:
                    speak("Goodbye")
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

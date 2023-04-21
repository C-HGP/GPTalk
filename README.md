# GPTalk

GPTalk is a smart speaker powered by OpenAI's ChatGPT and Picovoice's Porcupine wake word engine. The application listens for a wake word, processes your speech using speech-to-text, generates a response with ChatGPT, and speaks the response using text-to-speech.

## Requirements

- Python 3.6 or higher
- PyAudio

## Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/GPTalk.git
```

2. Change the directory:

```bash
cd GPTalk
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

```bash
python -m pip install pyaudio
```

4. Download the Porcupine library and model files for your platform from the <a href=https://github.com/Picovoice/porcupine#getting-started>Porcupine GitHub repository</a>. The library file has the extension .dll for Windows, .dylib for macOS, and .so for Linux. The model file has the extension .pv. Update the smart_speaker.py script with the correct paths to the downloaded library and model files.

5. Obtain a Porcupine access key from Picovoice Console. The application will prompt you to enter the access key on the initial launch.

6. Obtain an OpenAI API key from the OpenAI website. The application will prompt you to enter the API key on the initial launch.

## Setting up Porcupine

1. Go to the [Picovoice Console](https://console.picovoice.ai/).
2. Sign in or create an account if you don't have one.
3. Click on "Create Voice Model" in the top right corner.
4. Select "Wake Word" as the model type.
5. Enter your desired wake word.
6. Select the platforms you want to support.
7. Click "Create" to generate the wake word model.
8. Download the generated `.ppn` file(s) for your chosen platforms.

Update the `smart_speaker.py` script to use your custom wake word:

1. Replace the following line:

Make sure to replace `"path/to/your/custom_wake_word.ppn"` with the actual path to the downloaded `.ppn` file.

## Usage

1. Run the main script:

```bash
python smart_speaker.py
```

2. Speak the wake word and wait for the confirmation sound. Then, ask a question or give a command.

3. To stop the application, say Goodbye.

## Note

Using the OpenAI API may incur costs depending on your usage. You might need to adjust the `engine` parameter in the `chat_with_gpt` function, as the API and engine names might change over time.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

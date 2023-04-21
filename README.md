# GPTalk [WIP]

GPTalk is a voice-activated AI assistant powered by OpenAI's ChatGPT, featuring speech recognition and text-to-speech. The project turns your device into a smart speaker that listens for a wake word, responds to voice commands, and reads the generated text aloud.

## Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/GPTalk.git
```

2. Change the directory:

```bash
cd GPTalk
```

3. Install the necessary packages:

```bash
pip install -r requirements.txt
```

4. Install PyAudio using the following command:

```bash
python -m pip install pyaudio
```

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

```python
porcupine = Porcupine(keyword_paths=["path/to/your/custom_wake_word.ppn"])
```

Make sure to replace `"path/to/your/custom_wake_word.ppn"` with the actual path to the downloaded `.ppn` file.

## Usage

1. Obtain an API key from the [OpenAI website](https://beta.openai.com/signup/) and replace `your_openai_api_key` in `smart_speaker.py` with your key.

2. Run the main script:

```bash
python smart_speaker.py
```

3. Speak the wake word and wait for the confirmation sound. Then, ask a question or give a command.

4. To stop the application, say "exit", "stop", or "quit".

## Note

Using the OpenAI API may incur costs depending on your usage. You might need to adjust the `engine` parameter in the `chat_with_gpt` function, as the API and engine names might change over time.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

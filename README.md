# GPTalk [WIP]

GPTalk is a voice-activated AI assistant powered by OpenAI's ChatGPT, featuring speech recognition and text-to-speech. The project turns your device into a smart speaker that listens for a wake word, responds to voice commands, and reads the generated text aloud.

## Installation

1. Clone this repository
2. Install the necessary packages:

```
pip install -r requirements.txt
```

## Usage

- Obtain an API key from the OpenAI website and replace your_openai_api_key in smart_speaker.py with your key.

- Download or create a wake word model file (e.g., alexa.umdl). Replace the path in smart_speaker.py with the path to your wake word model file. You can find some pre-trained models <a href= https://github.com/Kitt-AI/snowboy/tree/master/resources/models>here</a>, or create your own using the Snowboy website.

- Run the main script:

```
python smart_speaker.py
```

- Speak the wake word and wait for the confirmation sound. Then, ask a question or give a command.

- To stop the application, say "exit", "stop", or "quit".

## Note

The snowboy library is deprecated, and the official website and repositories may not be maintained anymore. Additionally, using the OpenAI API may incur costs depending on your usage. You might need to adjust the engine parameter in the chat_with_gpt function, as the API and engine names might change over time.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

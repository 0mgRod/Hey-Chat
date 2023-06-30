# Hey, Chat!

This is a voice-activated chat application that uses speech recognition and a language model to generate responses.

## Features

- Activated by saying "hey chat"
- Converts speech to text using the selected microphone
- Generates responses using a language model
- Plays the generated response as speech

## Prerequisites

- Python 3.6 or higher
- Install required libraries using pip:

```
pip install speechrecognition transformers
```


## Usage

1. Clone the repository:

```
git clone https://github.com/0mgRod/Hey-Chat.git
cd Hey-Chat
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Run the application:

```
python main.py
```

4. Select a microphone from the available options presented.

5. Say "hey chat" to activate the chat feature.

6. Ask your question or provide input after the activation prompt.

7. The application will generate a response based on the input.

8. The response will be played as speech.

9. Repeat the process to have a conversation with the chat application.

## Configuration

- Microphone Selection: You can select the desired microphone by running the application and choosing the microphone's index from the available options.

- Language Model: The application uses the EleutherAI GPT-Neo 1.3B model by default. You can explore other models available in the `transformers` library and modify the code accordingly to use a different model.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

This application is based on the work of OpenAI's GPT-3.5 language model and the Hugging Face `transformers` library.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements or bug fixes.

## Support

If you have any questions or need assistance, please feel free to open an issue in the [issue tracker](https://github.com/0mgRod/Hey-Chat/issues).

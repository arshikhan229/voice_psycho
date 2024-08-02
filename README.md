# Voice Psycho

Voice Psycho is a virtual psychiatrist assistant that leverages machine learning models to interact with users through speech recognition and text-to-speech functionalities. The assistant can convert audio inputs into text, generate responses using a pre-trained language model, and convert these responses back into speech.

## Features

- **Speech-to-Text**: Converts spoken words into text using the SpeechRecognition library.
- **Text Generation**: Utilizes a pre-trained language model from the Hugging Face Transformers library to generate responses.
- **Text-to-Speech**: Converts text responses into speech using the gTTS library.
- **Interactive Sessions**: Provides a virtual assistant experience for interactive voice-based communication.

## Installation

1. **Clone the Repository**:
   ```sh
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Set Up Virtual Environment**:
   - Install `virtualenv` if you haven't already:
     ```sh
     pip install virtualenv
     ```
   - Create a virtual environment:
     ```sh
     python -m venv env
     ```
   - Activate the virtual environment:
     ```sh
     .\env\Scripts\activate
     ```

3. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Install Additional Packages**:
   ```sh
   pip install optimum peft torch==2.1 auto-gptq bitsandbytes SpeechRecognition gtts pydub
   ```

## Usage

1. **Activate the Virtual Environment**:
   ```sh
   .\env\Scripts\activate
   ```

2. **Run the Script**:
   ```sh
   python voice_psycho.py
   ```

3. **Input Audio File**:
   - Replace `audio_filename` in the script with the path to your audio file.
   - Example:
     ```python
     audio_filename = "path/to/your/audio/file.mp3"
     ```

4. **Script Workflow**:
   - The script will convert the audio file to text.
   - Generate a response using the pre-trained model.
   - Convert the generated response back to speech and save it as an MP3 file.

## Example

To see an example in action, you can run the script with a provided audio file. The script will:
- Convert the audio input to text.
- Generate a response based on the input text.
- Convert the response to speech and save it as `output.mp3`.

## Dependencies

- Python 3.6+
- [virtualenv](https://pypi.org/project/virtualenv/)
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [gTTS](https://pypi.org/project/gTTS/)
- [pydub](https://pypi.org/project/pydub/)
- Additional packages listed in `requirements.txt`

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.

## Acknowledgments

- Hugging Face for providing the Transformers library.
- The authors of the SpeechRecognition, gTTS, and pydub libraries for their invaluable tools.

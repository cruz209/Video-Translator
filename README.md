# Video-Translator

Video Translator App

This is a Flask-based web application that allows users to upload a video file, extract and transcribe the audio, translate the transcribed text into a different language, and convert the translated text back to audio. The output is provided in the form of an audio file that contains the translated version of the video's content.

Features
- Upload Video: Users can upload a video file in various formats.
- Automatic Speech Recognition: Extracts the audio from the video and converts it to text using Google's SpeechRecognition API.
- Translation: Translates the extracted text to a language of the user's choice using Googletrans.
- Text-to-Speech: Converts the translated text into an audio file using gTTS (Google Text-to-Speech).
- Language Selection: Users can select from multiple languages, such as English, Spanish, French, German, Tamil, Chinese, Hindi, Japanese, Korean, Italian, Portuguese, and Russian.

Prerequisites
- Python 3.7+
- Googletrans
- gTTS
- MoviePy
- SpeechRecognition

Installation
1. Clone this repository:
   git clone https://github.com/cruz209/Video-Translator.git
   cd Video-Translator

2. Create a virtual environment and activate it:
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On Mac/Linux
   source venv/bin/activate

3. Install the required dependencies:
   pip install -r requirements.txt

4. Set up environment variables if needed

Usage
1. Run the Flask application:
   flask run

2. Access the app in your web browser at http://127.0.0.1:5000.

3. Upload a video and select the target language for translation.

4. Download the translated audio file after the process is complete.

Project Structure
- app.py: Main application code for the Flask server.
- templates/: Contains the HTML files, including upload.html.
- static/uploads/: Folder where uploaded videos are stored.
- static/output/: Folder where output audio files are saved.
- requirements.txt: List of Python dependencies for the project.

Supported Languages
- Source and Target Languages: English, Spanish, French, German, Tamil, Chinese (Simplified), Hindi, Japanese, Korean, Italian, Portuguese, Russian.

License
This project is licensed under the Apache License 2.0. See the LICENSE file for details.

Acknowledgments
- Flask: Micro web framework used to build the application.
- MoviePy: For handling video processing.
- SpeechRecognition: For converting audio to text.
- gTTS: For converting translated text to speech.
- Googletrans: For translating the extracted text.

Contributing
Feel free to open an issue or submit a pull request if you want to contribute to this project. Any suggestions or improvements are welcome!

Contact
- GitHub: cruz209
- Email: cchris2004@gmail.com

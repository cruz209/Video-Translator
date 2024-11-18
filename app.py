#
# from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
# import os
# from moviepy.editor import VideoFileClip
# import speech_recognition as sr
# from googletrans import Translator
# from gtts import gTTS
#
# app = Flask(__name__)
# app.secret_key = 'your_secret_key'  # Required for flash messages
#
# UPLOAD_FOLDER = 'static/uploads'
# OUTPUT_FOLDER = 'static/output'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER
#
# # Ensure folders exist
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# os.makedirs(OUTPUT_FOLDER, exist_ok=True)
#
#
# @app.route('/')
# def upload_file():
#     return render_template('upload.html')
#
#
# @app.route('/upload', methods=['POST'])
# def handle_upload():
#     if 'file' not in request.files:
#         flash('No file part', 'error')
#         return redirect(request.url)
#     file = request.files['file']
#     if file.filename == '':
#         flash('No selected file', 'error')
#         return redirect(request.url)
#
#     # Get source and target language from the form
#     source_language = request.form.get('source_language', 'ta')
#     target_language = request.form.get('target_language', 'en')
#
#     if file:
#         filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#         file.save(filepath)
#
#         try:
#             # Process video file
#             translated_file = process_video(filepath, source_language, target_language)
#
#             # Flash success message
#             flash('File uploaded and translated successfully!', 'success')
#
#             # Redirect to the home page after successful upload
#             return redirect(url_for('upload_file'))
#
#         except Exception as e:
#             flash(f'Error processing the video: {str(e)}', 'error')
#             return redirect(url_for('upload_file'))
#
#
# def process_video(filepath, source_language, target_language):
#     # Step 1: Extract audio using moviepy
#     audio_path = os.path.join(app.config['OUTPUT_FOLDER'], 'audio.wav')
#     video = VideoFileClip(filepath)
#     video.audio.write_audiofile(audio_path)
#
#     # Step 2: Transcribe audio to text using SpeechRecognition
#     transcript = transcribe_audio(audio_path, source_language=source_language)
#
#     # Step 3: Translate text using googletrans
#     translated_text = translate_text(transcript, target_language)
#
#     # Step 4: Convert translated text to audio
#     translated_audio_path = os.path.join(app.config['OUTPUT_FOLDER'], 'translated_audio.mp3')
#     tts = gTTS(text=translated_text, lang=target_language)
#     tts.save(translated_audio_path)
#
#     # Step 5: Return translated audio path
#     return 'translated_audio.mp3'
#
#
# def transcribe_audio(audio_path, source_language='ta'):
#     recognizer = sr.Recognizer()
#     with sr.AudioFile(audio_path) as source:
#         audio_data = recognizer.record(source)
#         transcript = recognizer.recognize_google(audio_data, language=source_language)
#     return transcript
#
#
# def translate_text(text, target_language='en'):
#     translator = Translator()
#     translated_text = translator.translate(text, dest=target_language).text
#     return translated_text
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
import os
from moviepy.editor import VideoFileClip
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages

UPLOAD_FOLDER = 'static/uploads'
OUTPUT_FOLDER = 'static/output'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

# Ensure folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


@app.route('/')
def upload_file():
    languages = [
        {'code': 'en', 'name': 'English'},
        {'code': 'es', 'name': 'Spanish'},
        {'code': 'fr', 'name': 'French'},
        {'code': 'de', 'name': 'German'},
        {'code': 'ta', 'name': 'Tamil'},
        {'code': 'zh-cn', 'name': 'Chinese (Simplified)'},
        {'code': 'hi', 'name': 'Hindi'},
        {'code': 'ja', 'name': 'Japanese'},
        {'code': 'ko', 'name': 'Korean'},
        {'code': 'it', 'name': 'Italian'},
        {'code': 'pt', 'name': 'Portuguese'},
        {'code': 'ru', 'name': 'Russian'}
    ]
    return render_template('upload.html', languages=languages)


@app.route('/upload', methods=['POST'])
def handle_upload():
    if 'file' not in request.files:
        flash('No file part', 'error')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file', 'error')
        return redirect(request.url)

    # Get target language from the form
    target_language = request.form.get('target_language', 'en')

    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        try:
            # Process video file
            translated_file = process_video(filepath, target_language)

            # Flash success message
            flash('File uploaded and translated successfully!', 'success')

            # Redirect to the home page after successful upload
            return redirect(url_for('upload_file'))

        except Exception as e:
            flash(f'Error processing the video: {str(e)}', 'error')
            return redirect(url_for('upload_file'))


def process_video(filepath, target_language):
    # Step 1: Extract audio using moviepy
    audio_path = os.path.join(app.config['OUTPUT_FOLDER'], 'audio.wav')
    video = VideoFileClip(filepath)
    video.audio.write_audiofile(audio_path)

    # Step 2: Transcribe audio to text and detect source language
    transcript, source_language = transcribe_audio(audio_path)

    # Step 3: Translate text using googletrans
    translated_text = translate_text(transcript, target_language)

    # Step 4: Convert translated text to audio
    translated_audio_path = os.path.join(app.config['OUTPUT_FOLDER'], 'translated_audio.mp3')
    tts = gTTS(text=translated_text, lang=target_language)
    tts.save(translated_audio_path)

    # Step 5: Return translated audio path
    return 'translated_audio.mp3'


def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
        # Using Google Web Speech API to detect language automatically
        transcript = recognizer.recognize_google(audio_data)
        # Assuming source language is English for simplicity; language detection can be added
        source_language = 'en'
        return transcript, source_language


def translate_text(text, target_language='en'):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language).text
    return translated_text


if __name__ == '__main__':
    app.run(debug=True)

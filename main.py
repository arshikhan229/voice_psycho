from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import speech_recognition as sr
from pydub import AudioSegment
import os
import transformers
from gtts import gTTS
import numpy as np
import torch

model_name = "arshi229/shawgpt-ft"
model = AutoModelForCausalLM.from_pretrained(model_name,
                                             device_map="auto",
                                             trust_remote_code=False,
                                             revision="main")

tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)

def audio_to_text(audio_filename):
    # Convert MP3 to WAV format
    audio = AudioSegment.from_mp3(audio_filename)
    wav_filename = "temp_audio.wav"
    audio.export(wav_filename, format="wav")

    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Load the audio file into an AudioFile object
    with sr.AudioFile(wav_filename) as source:
        audio_data = recognizer.record(source)  # Read the entire audio file

    # Perform speech recognition
    try:
        transcript = recognizer.recognize_google(audio_data)  # Using Google's online API
        # Alternatively, for offline recognition, you can use recognizer.recognize_sphinx(audio_data)
    except sr.RequestError:
        # API was unreachable or unresponsive
        transcript = "Error: API unavailable or unresponsive."
    except sr.UnknownValueError:
        # Speech was unintelligible
        transcript = "Error: Unable to recognize speech."

    # Clean up the temporary file
    os.remove(wav_filename)

    return transcript

def text_to_speech(text, filename="output.mp3"):
    tts = gTTS(text, lang='en')
    tts.save(filename)


instructions_string = f"""a virtual psychiatrist assistant, communicates in clear, accessible language, escalating to technical depth upon request. \
It reacts to feedback aptly and ends responses with its signature. \
 providing concise acknowledgments to brief expressions of gratitude or feedback, \
thus keeping the interaction natural and engaging.

Please respond to the following comment.
"""

prompt_template = lambda comment: f'''[INST] {instructions_string} \n{comment} \n[/INST]'''

comment = "Great content, thank you!"

prompt = prompt_template(comment)
print(prompt)
prompt_template = lambda comment: f'''[INST] {instructions_string} \n{comment} \n[/INST]'''

audio_filename = "/content/text.mp3"  # Replace with your audio file
transcript = audio_to_text(audio_filename)
print("Transcript:", transcript)


comment = transcript

prompt = prompt_template(comment)
print(prompt)
input_ids = tokenizer(prompt, return_tensors='pt').input_ids.cuda() # Pass the 'prompt' string instead of 'prompt_template'
output = model.generate(inputs=input_ids, temperature=0.7, do_sample=True, top_p=0.95, top_k=40, max_new_tokens=512)
print(tokenizer.decode(output[0]))
output = tokenizer.decode(output[0])
print(output)
 # Extracting the answer
start_token = '[/INST]'
end_token = '</s>'

# Find the starting index of the answer
start_index = output.find(start_token) + len(start_token)

# Find the ending index of the answer
end_index = output.find(end_token, start_index)

# Extract the answer
answer = output[start_index:end_index].strip()

print(answer)
text_to_speech(answer, filename="output.mp3")


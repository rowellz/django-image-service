import requests
import json
import speech_recognition as sr
from django.core.files.base import ContentFile, File
import os
from scipy.io import wavfile
import numpy as np
import shutil


class LipSyncService:
    def sync_audio_and_text(self, alignment, automate_text=False):

        if automate_text:
            text = self.speach_to_text(alignment)
            alignment.text_file = ContentFile(text.encode('utf8'), name='temp.txt')
            alignment.save()
            print("Fsffsdasda")

        params = {
            'async': 'false',
        }

        files = {
            'audio': open(f"./media/{alignment.audio_file}", 'rb'),
            'transcript': open(f"./media/{alignment.text_file}", 'rb'),
        }

        response = requests.post('http://gentle:8765/transcriptions', params=params, files=files)
        
        alignment.transcription_json = response.json()
        alignment.save()

        return json.dumps(response.json())

    def speach_to_text(self, alignment):
        # initialize the recognizer
        r = sr.Recognizer()

        # open the file
        with sr.AudioFile(alignment.audio_file) as source:
            # listen for the data (load audio to memory)
            audio_data = r.record(source)
            # recognize (convert from speech to text)
            text = r.recognize_google(audio_data)
            return text
        
    def create_lazykh_folder(self, alignment):

        new_dir = f"./media/transcriptions/transcription_{alignment.id}/"
        os.mkdir(new_dir)
        samplerate, data = wavfile.read(f"./media/{alignment.audio_file}")
        wavfile.write(f"{new_dir}t.wav", samplerate, data.astype(np.int16))

        shutil.copy(f"./media/{alignment.text_file}", f"{new_dir}t.txt")

        with open(f"{new_dir}t.json", "w") as outfile:
            json_object = json.dumps(alignment.transcription_json, indent=4)
            outfile.write(json_object)

        os.system(f"python /app/backend/myapp/services/lazykh/code/scheduler.py --input_file {new_dir}t")
        os.system(f"python /app/backend/myapp/services/lazykh/code/videoDrawer.py --input_file {new_dir}t --use_billboards F --jiggly_transitions F")
        os.system(f"python /app/backend/myapp/services/lazykh/code/videoFinisher.py --input_file {new_dir}t --keep_frames F")

        alignment.video_file = f"transcriptions/transcription_{alignment.id}/t_final.webm"
        alignment.save()

import requests
import json
from django.core.files.base import ContentFile, File
import os
from scipy.io import wavfile
import numpy as np
import shutil

class LipSyncService:
    def sync_audio_and_text(self, alignment):

        params = {
            'async': 'false',
        }

        files = {
            'audio': open(f"./media/{alignment.audio_file}", 'rb'),
            'transcript': open(f"./media/{alignment.text_file}", 'rb'),
        }

        response = requests.post('http://host.docker.internal:8003/transcriptions', params=params, files=files)

        print(response.json())
        
        alignment.transcription_json = response.json()

        alignment.save()

        return json.dumps(response.json())

        
    def create_lazykh_folder(self, alignment):

        new_dir = f"./media/transcriptions/transcription_{alignment.id}/"
        os.mkdir(new_dir)
        samplerate, data = wavfile.read(f"./media/{alignment.audio_file}")
        wavfile.write(f"{new_dir}t.wav", samplerate, data.astype(np.int16))

        newPath = shutil.copy(f"./media/{alignment.text_file}", f"{new_dir}t.txt")

        # with open(f"./media/{alignment.audio_file}") as f:
        #     lines = f.readlines()
        #     lines = [l for l in lines if "ROW" in l]
        #     with open(f"{new_dir}t.txt", "w") as f1:
        #         f1.writelines(lines)


        with open(f"{new_dir}t.json", "w") as outfile:
            json_object = json.dumps(alignment.transcription_json, indent=4)
            outfile.write(json_object)

        # text_file = open(f"./media/{alignment.audio_file}", "r")
        
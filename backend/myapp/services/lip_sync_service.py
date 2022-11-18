import requests
import json


class LipSyncService:
    def sync_audio_and_text(self, audio, text, alignment):

        params = {
            'async': 'false',
        }

        files = {
            'audio': open(f"./media/{alignment.audio_file}", 'rb'),
            'transcript': open(f"./media/{alignment.text_file}", 'rb'),
        }

        response = requests.post('http://host.docker.internal:8003/transcriptions', params=params, files=files)

        print(response.json())

        return json.dumps(response.json())

        
import numpy as np
import pyfoal
import wave
import scipy.io.wavfile


class LipSyncService:
    def sync_audio_and_text(self, audio, text, alignment):
        rate, data = scipy.io.wavfile.read(f"./media/{alignment.audio_file}")
        sin_data = np.sin(data)


        f = open(f"./media/{alignment.text_file}", "r")
        string = f.read()
        
        with wave.open(alignment.audio_file, "rb") as wave_file:
            frame_rate = wave_file.getframerate()
            print("FSAFASF", frame_rate, alignment.text_file, alignment.audio_file)
        alignment = pyfoal.align(string, data, rate)
        return alignment

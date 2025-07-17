import os
import numpy as np
import librosa
import soundfile as sf 


input_folder = "/home/vksit/Documents/Samsung_Prism_2025/Hearing_Impaired_Data/New_DataSet/kn_in_female"
output_folder = "/home/vksit/Documents/Samsung_Prism_2025/Hearing_Impaired_Data/New_DataSet/Augmented/Pitch2"


os.makedirs(output_folder, exist_ok=True)


bins_per_octave = 12
pitch_pm = 2  # maximum pitch shift in semitones (±2)
sample_rate = 16000  # or use None to let librosa detect


for filename in os.listdir(input_folder):
    if filename.endswith(".wav"):
        filepath = os.path.join(input_folder, filename)
        
       
        y, sr = librosa.load(filepath, sr=sample_rate)
        
        
       # pitch_change = pitch_pm * 2 * (np.random.rand() - 0.5)
        pitch_change = pitch_pm * 2 
        print(f"{filename}: pitch_change = {pitch_change:.2f} semitones")

        # Apply pitch shift
        y_shifted = librosa.effects.pitch_shift(y=y, sr=sr, n_steps=pitch_change, bins_per_octave=bins_per_octave)
        
        
        output_path = os.path.join(output_folder, f"pitch_{filename}")
        sf.write(output_path, y_shifted, sr)

print("Pitch shifting complete. Check the 'output_audio' folder.")

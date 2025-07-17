# Pitch Augmentation 
This script performs **pitch shifting** on `.wav` audio files using the `librosa` library. It augments your dataset by applying a fixed pitch change and saves the modified audio files to a separate folder — useful for speech recognition and audio processing tasks.


#  What It Does
- Loads audio files from an input directory
- Applies a fixed pitch shift (e.g., +2 semitones)
- Saves the pitch-shifted audio to a specified output directory
- Helps expand training data for ASR systems


# Folder Structure
  pitch-augmentation\

- pitch_augmentation.py # Main Python script
- README.md # Documentation
- .gitignore # (optional) To ignore .wav or cache files



# Setup Instructions

1. Install Dependencies
```bash
pip install librosa soundfile numpy
```

2. Modify the Input and Output Paths
   a)input_folder = "/path/to/your/input/audio"
   b)output_folder = "/path/to/save/augmented/audio"
  
3. Adjust Parameters (optional)

  - pitch_pm = 2: Pitch shift range in semitones (±2);  

  - sample_rate = 16000: Audio sampling rate;

  - bins_per_octave = 12: Used for pitch resolution


 ## Run the Script
    python pitch_augmentation.py


#  outputs will be like:
  - sample1.wav: pitch_change = 4.00 semitones
  - sample2.wav: pitch_change = 4.00 semitones

 #  Files will be saved as:
 - pitch_sample1.wav
 - pitch_sample2.wav

# License
This project is intended for educational and research purposes. The librosa and soundfile libraries are licensed separately.

# Acknowledgements
1. librosa
2. soundfile


  



 


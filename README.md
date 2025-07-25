DSP Fundamentals in Python
This repository contains fundamental concepts of Digital Signal Processing (DSP) implemented in Python. Discrete-time Fourier operations are used extensively throughout. More details about each implementation can be found in the designinfo/ folder.

Main Highlight: FIR Filter (Low-Pass)
    The FIR/ folder demonstrates a low-pass filter using Finite Impulse Response techniques.

    Record Audio
    Run RecordYourVoice.py to record your own audio. The file is saved as my_recording.wav.

    Filter and Visualize
    Run FIR.py to:
    View the frequency spectrum and time-domain signals of both the original and filtered audio.
    After closing the plots, two audio files are saved: Unfiltered_Input_Signal.wav and Filtered_Signal.wav.

    Modify Filter Settings
    You can change the sampling range and cutoff frequency in the FIR.py file to observe different outputs.

Requirements
    pip install numpy matplotlib sounddevice soundfile

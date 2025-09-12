# DSP Fundamentals in Python

This repository contains fundamental concepts of **Digital Signal Processing (DSP)** implemented in Python. Discrete-time Fourier operations are used extensively throughout. More details about each implementation can be found in the `designinfo/` folder.  

---

## ## Folder Overview: LPF_FIR

The `FIR/` folder demonstrates a **low-pass filter** using Finite Impulse Response techniques.

### Record Audio
Run `RecordYourVoice.py` to record your own audio. The file is saved as `my_recording.wav`.  

### Filter and Visualize
Run `FIR.py` to:  
- View the **frequency spectrum** and **time-domain signals** of both the original and filtered audio.  
- After closing the plots, two audio files are saved:  
  - `Unfiltered_Input_Signal.wav`  
  - `Filtered_Signal.wav`  

### Modify Filter Settings
You can change the **sampling range** and **cutoff frequency** in the `FIR.py` file to observe different outputs.

> **Note:** Make sure you are in the `FIR` folder while running the code, otherwise the program cannot access the audio file which is inside the folder.  

> **Dual Channel Audio:** Make sure the `.wav` file is dual channel. If not, replace line 50:  
> ```python
> x = discrete_signal[start_sample:end_sample, 0]
> ```  
> with  
> ```python
> x = discrete_signal[start_sample:end_sample]
> ```  

### Requirements
```bash
pip install numpy matplotlib sounddevice soundfile
```
# BPF_FIR: Band Pass Filter 

This folder demonstrates a **band pass filter**, which limits the frequency components of a signal and allows only a specific frequency range to pass through. It contains all the necessary code and examples to visualize and apply the filter on audio signals.  

---



- **BandPassFilter.py**  
  Contains the code for the **impulse response** of the band pass filter with visualization plots.

- **signalProcessing.py**  
  Contains the code for **convolution** of the input signal with the ideal impulse response.  
  - The impulse response is shifted to make the system **causal**.  
  - Example plots are provided for reference.  

---

## Usage

### Run Bandpass Filter
1. Place your `.wav` file in this folder and name it `my_recording.wav`.  
2. Run `signalProcessing.py` to:  
   - Apply the band pass filter to your audio.  
   - Visualize the original and filtered signals in  **frequency domains**.  

> **Note:** The filtering process involves large computations, so it may take some time to run and display the plots.  

---

## Modify Filter Settings
You can modify the filter parameters such as:  
- **Cutoff frequencies**  
- **Sampling rate**  

These changes can be made directly in `BandPassFilter.py` to observe different filter behaviors.

---

## Requirements
```bash
pip install numpy matplotlib sounddevice soundfile

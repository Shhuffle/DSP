# DSP Fundamentals in Python

This repository contains fundamental concepts of **Digital Signal Processing (DSP)** implemented in Python. Discrete-time Fourier operations are used extensively throughout. More details about each implementation can be found in the `designinfo/` folder.  

---

## Main Highlight: FIR Filter (Low-Pass)

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
BPF_FIR: Band Pass Filter

Band Pass Filter limits the frequency component of a signal. It allows passing of signal with certain frequency limits.

The BandPassFilter.py file contains the code for the impulse response of the band pass filter with plots for visualization.

The signalProcessing.py file contains the code for the convolution of the input signal and the ideal impulse response. The ideal impulse response is shifted so that the system becomes causal. Example plots are also provided in the same folder.

Run Bandpass Filter

To see the bandpass filter in action, run signalProcessing.py.

You can filter your own .wav file: just name the file my_recording.wav and save it under the same folder.

Since it performs large computations, it may take some time to run the code and plot the graph.

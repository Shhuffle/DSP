#This code contains a function to boost the energy of high frequency signal by applying the high pass filter 

#Reasons on boosting the high frequency signal:-
#Human speech naturally has a spectral tilt, energy is stronger at low frequency(<1khz) while it drops off at higher freqeuncies(2-8khz)
#even though those contain important formants (resonanes that distinguish vowel and consonants)


import numpy as np
import soundfile as sf

filename = "my_recording.wav"
discrete_input, sampling_rate = sf.read(filename)


def PreEmphasis(x_n,alpha = 0.97):
    y = np.zeros(len(x_n))
    y[0] = x_n[0]
    for n in range(1,len(x_n)):
        y[n] = x_n[n] - alpha * x_n[n-1] #first order high pass filter 
    return y

#Framing - 25ms

frame_length = 0.025 #25ms
hop_length = 0.01 #10ms
hop_size = int(sampling_rate * hop_length)
sample_size = int(sampling_rate * frame_length)



def frames(start):
    next_frame = start+hop_size
    return next_frame,discrete_input[start:start+sample_size]


next_framestart,x = frames(0)
total_frames = int((len(discrete_input) - sample_size) / hop_size)
print(next_framestart," & ",x)
print("Total frames: ",total_frames)


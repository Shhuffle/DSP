#This program will perform the convolution on the input signal and the bandpass ideal impulse response taken form the function 
#located in the BandPassFilter.py

from BandPassFilter import hn
import numpy as np
import matplotlib.pylab as plt
import soundfile as sf


#load audio file
filename = "my_recording.wav"
discrete_signal, sampling_rate = sf.read(filename)
print(f"Sampling rate: {sampling_rate} Hz")
print(f"Total samples: {len(discrete_signal)}")
print(f"Total Duration: {len(discrete_signal) / sampling_rate:.2f} seconds")

def conv(h,x):
    L = len(h) + len(x) - 1
    y = np.zeros(L,dtype=complex)
    for n in range (L):
        for k in range (len(x)):
            if 0<= n-k < len(h):
                y[n] += x[k] * h[n-k]

    return y,L
#even though i have created conv function later i have use the numpy convolve as it is much faster.


#Parameters Definition
#cutoff frequency in hz
f1 = 8000
f2 = 15000
N = 401      #ideal impulse response length
fs = sampling_rate   #sampling frequency with Nyquist Criteria
start_sample , end_sample = 440, 220500 #for the audio file





#Signal definition 
h = hn(f1,f2,fs,N)
x = discrete_signal[start_sample:end_sample] #0 means mono/single channel audio data, if the audio is mono channel then remove ,0
y = np.convolve(x,h)


print(x[890:1200])

#Transforms
H = np.fft.fft(h)
X = np.fft.fft(x)
Y = np.fft.fft(y)


sf.write('Filtered_signal.wav',np.real(y),sampling_rate)
sf.write('Unfiltered_input_signal.wav',x,sampling_rate)
        
        
#plots
fig,axs =plt.subplots(3,2,figsize=(6,6))
plt.tight_layout(pad=2, h_pad=4, w_pad=3)
plt.figtext(0.5, 0.01, f"Cutoff Frequencies: f1 = {f1} Hz, f2 = {f2} Hz", ha="center", fontsize=10)


k=np.arange(len(H))
axs[0,0].stem((k*fs) / (len(H) * 1000),np.absolute(H))
axs[0,0].set_title("Magnitude of H[w]")
axs[0,0].set_xlabel("KHz")
axs[0,0].set_ylabel("Magnitude")

axs[0,1].stem((k*fs) / (len(H) * 1000),np.angle(H))
axs[0,1].set_title("Phase of H[w]")
axs[0,1].set_xlabel("Khz")
axs[0,1].set_ylabel("Phase")



k = np.arange(len(Y))
axs[1,0].stem((k*fs) / (len(Y) * 1000),np.absolute(Y))
axs[1,0].set_title("Magnitude of Y[w]")
axs[1,0].set_xlabel("KHz")
axs[1,0].set_ylabel("Magnitude")

axs[1,1].stem((k*fs) / (len(Y) * 1000),np.angle(Y))
axs[1,1].set_title("Phase of Y[w]")
axs[1,1].set_xlabel("Khz")
axs[1,1].set_ylabel("Phase")

import numpy as np

k = np.arange(1,len(X)//2)  # only up to Nyquist and ignore the dc component i.e w = 0
freq = (k * fs) / (len(X) * 1000)  # in kHz

axs[2,0].stem(freq, np.abs(X[1:len(X)//2]))
axs[2,0].set_title("Magnitude of X[w]")
axs[2,0].set_xlabel("KHz")
axs[2,0].set_ylabel("Magnitude")

axs[2,1].stem(freq, np.angle(X[1:len(X)//2]))
axs[2,1].set_title("Phase of X[w]")
axs[2,1].set_xlabel("KHz")
axs[2,1].set_ylabel("Phase")


plt.show()






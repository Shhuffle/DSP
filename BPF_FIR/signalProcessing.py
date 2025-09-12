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

#Parameters Definition
#cutoff frequency in hz
f1 = 4000
f2 = 8000
N = 400      #ideal impulse response length
fs = sampling_rate   #sampling frequency with Nyquist Criteria
start_sample , end_sample = 440, 22050 #for the audio file




#Signal definition 
h = hn(f1,f2,fs,N)
x = discrete_signal[start_sample:end_sample,0] #0 means mono/single channel audio data
y,L = conv(h,x)

#Transforms
Y = np.fft.fft(y)
X = np.fft.fft(x)
H = np.fft.fft(h)


sf.write('Unfiltered_input_signal.wav',x,sampling_rate)
sf.write('Filtered_signal.wav',np.real(y),sampling_rate)
        
        
#plots
fig,axs =plt.subplots(3,2,figsize=(6,6))
plt.tight_layout(pad=2, h_pad=4, w_pad=3)



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

k = np.arange(len(X))
axs[2,0].stem((k*fs) / (len(X) * 1000),np.absolute(X))
axs[2,0].set_title("Magnitude of X[w]")
axs[2,0].set_xlabel("KHz")
axs[2,0].set_ylabel("Magnitude")

axs[2,1].stem((k*fs) / (len(X) * 1000),np.angle(X))
axs[2,1].set_title("Phase of X[w]")
axs[2,1].set_xlabel("KHz")
axs[2,1].set_ylabel("Phase")

plt.show()






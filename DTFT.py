#In this code I have taken a discrete time signal  and performed fourier transform on it. 
#For more info check out DesignInfo.txt

import numpy as np 
import matplotlib.pyplot as plt
import soundfile as sf
import math 
import cmath

#import .wav file and print basic info
filename = "piano.wav"
discrete_signal, sample_rate = sf.read(filename) #discrete_signal => x[n]
Total_Sample = len(discrete_signal)
print(f"Total Sample: {Total_Sample}")
print(f"Sample Rate {sample_rate}")
print(f"Total duration : {Total_Sample/sample_rate} seconds")





#perform DTFT
def dft(x):
    N = len(x)
    X = []
    for k in range(N):
        Xk =0
        for n in range(N):
            omega = (-2j * math.pi * k * n) / N #w = j * 2pi/N 
            Xk += x[n] * cmath.exp(omega)
        X.append(Xk)
    return X

x = discrete_signal[200:420,0]           #Single channel values of original signal sample form 200 to 220.

X = dft(x)
print(f"Transform value is- {np.round(X,9)}")


k = np.arange(len(X))
X = np.array(X)                          #converting to np array enables us to calculate magitude and phase
magnitude = np.abs(X)
phase = np.angle(X)
n = np.arange(len(x))      #cretes an array of evenly space values in the range form 0 to discrete signal

#Original signal graph 
plt.subplot(3,1,1)
plt.stem(n,x)
plt.title("Original Signal")
plt.xlabel("N")
plt.ylabel("Amplitude")


#Magnitude plot
plt.subplot(3,1,2)
plt.stem(k,magnitude)
plt.title("Magnitude Plot")
plt.xlabel("K")
plt.ylabel("Magnitude")

#  Phase Spectrum
plt.subplot(3, 1, 3)
plt.stem(k, phase)
plt.title('Phase Spectrum ∠X(k)')
plt.xlabel('Frequency Index (k)')
plt.ylabel('Phase (radians)')

plt.tight_layout()
plt.show()
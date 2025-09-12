import numpy as np 
import matplotlib.pyplot as plt

def hn(f1,f2,fs,n):
    w1 = 2 * np.pi * (f1 / fs)
    w2 = 2 * np.pi * (f2 / fs)
    h = []
    for i in range (n):
        if i == 0:
            h.append((w2-w1) / (2 * np.pi))
        else:
            h.append(np.exp(1j * ((w2+w1) / 2) * i) * np.sin((w2-w1)/2 * i))
    return h


def fft(h):
    return np.fft.fft(h)




#Parameters 
f1 = 40     #Lower cutoff frequency in htz
f2 = 80     #upper cutoff freqeuncy in htz
n = 40      #total length of h[n]
fs = 2*f2     #sampling frequency


#Impulse Response h
h = hn(f1,f2,fs,n)
hA = np.absolute(h) #amplitude
hP = np.angle(h)    #phase

#Fourier Transform
Hejw = fft(h)
Hejw_A = np.absolute(Hejw)
Hejw_P = np.angle(Hejw)

#Plots
fig,axs = plt.subplots(2,2,figsize=(5,6))
plt.tight_layout(pad=5, h_pad=4, w_pad=2)

#x axis = k
k = np.linspace(0,n-1,n)

axs[0,0].stem(k, hA)
axs[0,0].set_title("Amplitude of impulse response h")
axs[0,0].set_xlabel("n")
axs[0,0].set_ylabel("Amplitude")


axs[0,1].stem(k, hP)
axs[0,1].set_title("Phase of impulse response h")
axs[0,1].set_xlabel("n")
axs[0,1].set_ylabel("Phase")



#The x axis after the fft is changed to wk form n. Where wk = (2*pi*k) / N. Also to make x axis as a function of frequency 
# then set the x axis as f = k*fs / N , where fs is the sampling freqeuncy and N is the periodic length for this case N = len(Hejw)

axs[1,1].stem((k*2*np.pi / len(Hejw)), Hejw_P)
axs[1,1].set_title("Phase of impulse response Hejw")
axs[1,1].set_xlabel("w")
axs[1,1].set_ylabel("Phase")

axs[1,0].plot((k*2*np.pi / len(Hejw)), Hejw_A)
axs[1,0].set_title("Amplitude of impulse response Hejw")
axs[1,0].set_xlabel("w")
axs[1,0].set_ylabel("Magnitude")



plt.show()


import numpy as np 
import matplotlib.pyplot as plt

def hn(f1,f2,fs,N):
    w1 = 2 * np.pi * (f1 / fs)
    w2 = 2 * np.pi * (f2 / fs)
    print("The cutoff freqeucy in rad/sample is ",w1," upper ",w2)
    h = []
    for n in range (N):
        k = n - (N-1)/2
        if k == 0:
            h.append((w2-w1) / (2 * np.pi))
        else:
            h.append((np.exp(1j * ((w2+w1) / 2) * k) * np.sin((w2-w1)/2 * k)) / (np.pi * k))
    wd = np.hamming(N)
    return h * wd


def fft(h):
    return np.fft.fft(h)



if __name__ == "__main__":
    #Parameters 
    f1 = 40     #Lower cutoff frequency in hz
    f2 = 80     #upper cutoff freqeuncy in hz
    N = 91      #total length of h[n] make sure it is odd number because we are shifting the ideal response by (n-1)/2 to make system causal
    fs = 2*f2     #sampling frequency Nyquist criteria


    #Impulse Response h
    h = hn(f1,f2,fs,N)
    hA = np.absolute(h) #amplitude
    hP = np.angle(h)    #phase

    #Fourier Transform of ideal impulse response centered at (N-1)/2
    Hejw = fft(h)
    Hejw_A = np.absolute(Hejw)
    Hejw_P = np.angle(Hejw)



    #Plots
    fig,axs = plt.subplots(2,2,figsize=(5,6))
    plt.tight_layout(pad=5, h_pad=4, w_pad=2)
    plt.figtext(0.5, 0.01, f"Cutoff Frequencies: f1 = {f1} Hz, f2 = {f2} Hz", ha="center", fontsize=10)

    #x axis = k
    k = np.linspace(0,N-1,N)

    axs[0,0].stem(k, hA)
    axs[0,0].set_title("Amplitude of impulse response h")
    axs[0,0].set_xlabel("N")
    axs[0,0].set_ylabel("Amplitude")


    axs[0,1].stem(k, hP)
    axs[0,1].set_title("Phase of impulse response h")
    axs[0,1].set_xlabel("N")
    axs[0,1].set_ylabel("Phase")



    #The x axis after the fft is changed to wk form N. Where wk = (2*pi*k) / N. Also to make x axis as a function of frequency 
    # then set the x axis as f = k*fs / N , where fs is the sampling freqeuncy and N is the periodic length for this case N = len(Hejw)

    axs[1,1].stem((k*fs / len(Hejw)), Hejw_P)
    axs[1,1].set_title("Phase of impulse response Hejw")
    axs[1,1].set_xlabel("Hz")
    axs[1,1].set_ylabel("Phase")

    axs[1,0].plot((k*fs / len(Hejw)), Hejw_A)
    axs[1,0].set_title("Amplitude of impulse response Hejw")
    axs[1,0].set_xlabel("Hz")
    axs[1,0].set_ylabel("Magnitude")



    plt.show()


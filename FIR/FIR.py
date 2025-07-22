import numpy as np 
import matplotlib.pyplot as plt
import soundfile as sf 

# Load audio file
filename = "highfreq.wav"
discrete_signal, sampling_rate = sf.read(filename)

print(f"Sampling rate: {sampling_rate} Hz")
print(f"Total samples: {len(discrete_signal)}")
print(f"Total Duration: {len(discrete_signal) / sampling_rate:.2f} seconds")

# -------------------------
# Ideal Low-Pass Filter
# -------------------------
def ideal_lpf(cutoff_hz, N):
    if N % 2 == 0:
        raise ValueError("Filter length N must be odd")

    hd = np.zeros(N)
    M = (N - 1) // 2  # Center of symmetry
    wc = 2 * np.pi * cutoff_hz / sampling_rate  # normalized rad/s

    for n in range(N):
        if n == M:
            hd[n] = wc / np.pi
        else:
            hd[n] = np.sin(wc * (n - M)) / (np.pi * (n - M))
    
    return hd

def convolution(x, h):
    N = len(x)
    M = len(h)
    L = N + M - 1
    y = np.zeros(L)
    for n in range(L):
        for k in range(M):
            if 0 <= n - k < N:
                y[n] += h[k] * x[n - k]
    return y

# -------------------------
# Parameters
# -------------------------
cutoff_hz = 1000  # desired cutoff in Hz
filter_length = 101  # should be odd
start_sample, end_sample = 440, 166640
x = discrete_signal[start_sample:end_sample, 0]  # mono

# Design filter and perform convolution
h = ideal_lpf(cutoff_hz, filter_length)
y = convolution(x, h)

# -------------------------
# Compute FFTs
# -------------------------
N_fft = 1024  # Zero-padding for better resolution

# FFT of input signal
X = np.fft.fft(x, N_fft)
freq_x = np.fft.fftfreq(N_fft, d=1/sampling_rate)[:N_fft//2] / 1000
X_mag = np.abs(X[:N_fft//2])

# FFT of filter
H = np.fft.fft(h, N_fft)
freq_h = np.fft.fftfreq(N_fft, d=1/sampling_rate)[:N_fft//2] / 1000
H_mag = np.abs(H[:N_fft//2])

# FFT of filtered signal
N_fft_y = len(y)
Y = np.fft.fft(y)
freq_y = np.fft.fftfreq(N_fft_y, d=1/sampling_rate)[:N_fft_y//2] / 1000
Y_mag = np.abs(Y[:N_fft_y//2])

# -------------------------
# Plotting
# -------------------------
fig, axs = plt.subplots(3, 2, figsize=(12, 6))

# 1. Original signal (time domain)
n = np.arange(len(x))
axs[0, 0].stem(n, x, basefmt=" ")
axs[0, 0].set_title("Original Signal (Time Domain)")
axs[0, 0].set_xlabel("n")
axs[0, 0].set_ylabel("Amplitude")

# 2. Impulse response of LPF
n = np.arange(len(h))
axs[0, 1].stem(n, h, basefmt=" ")
axs[0, 1].set_title(f"Impulse Response h[n] (cutoff={cutoff_hz}Hz)")
axs[0, 1].set_xlabel("n")
axs[0, 1].set_ylabel("Amplitude")

# 3. FFT of Original Signal
axs[1, 0].plot(freq_x, X_mag)
axs[1, 0].set_title("FFT of Original Signal")
axs[1, 0].set_xlabel("Frequency (kHz)")
axs[1, 0].set_ylabel("|X[k]|")
axs[1, 0].grid(True)
axs[1, 0].set_xlim(0, sampling_rate / 2000)

# 4. FFT of Filter
axs[1, 1].plot(freq_h, H_mag)
axs[1, 1].set_title("FFT of Ideal Low-Pass Filter h[n]")
axs[1, 1].set_xlabel("Frequency (kHz)")
axs[1, 1].set_ylabel("|H[k]|")
axs[1, 1].grid(True)
axs[1, 1].set_xlim(0, sampling_rate / 2000)

# 5. Output filtered signal (time domain)
n = np.arange(len(y))
axs[2, 0].stem(n, y, basefmt=" ")
axs[2, 0].set_title("Filtered Output Signal (Time Domain)")
axs[2, 0].set_xlabel("n")
axs[2, 0].set_ylabel("Amplitude")

# 6. FFT of Filtered Output Signal
axs[2, 1].plot(freq_y, Y_mag)
axs[2, 1].set_title("FFT of Filtered Signal")
axs[2, 1].set_xlabel("Frequency (kHz)")
axs[2, 1].set_ylabel("|Y[k]|")
axs[2, 1].grid(True)
axs[2, 1].set_xlim(0, sampling_rate / 2000)

plt.tight_layout()
plt.show()


# Normalize both signals to float32
x_out = (x / np.max(np.abs(x))).astype(np.float32)
y_out = (y / np.max(np.abs(y))).astype(np.float32)

sf.write('Unfiltered_Input_Signal.wav', x_out, sampling_rate)
sf.write('Filtered_Signal.wav', y_out, sampling_rate)

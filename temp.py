import numpy as np
import matplotlib.pyplot as plt

# --- Parameters ---
filter_length = 513  # Must be odd to center at zero
fc = 0.2             # Normalized cutoff frequency (0 < fc < 0.5)
N_fft = 2048         # FFT length for frequency resolution

# --- Generate h[n] = 2 * fc * sinc(2 * fc * n) ---
n = np.arange(-(filter_length // 2), (filter_length // 2) + 1)
h = 2 * fc * np.sinc(2 * fc * n)

# Optional: apply window (for less ripple, optional)
# window = np.hamming(filter_length)
# h = h * window

# --- Compute FFT ---
H = np.fft.fft(h, N_fft)
H_mag = np.abs(H[:N_fft // 2])  # Take positive frequencies
H_mag /= np.max(H_mag)          # Normalize

# --- Frequency Axis ---
freq = np.linspace(0, 0.5, N_fft // 2)  # Normalized frequency (0 to 0.5)

# --- Plot ---
plt.figure(figsize=(10, 5))
plt.plot(freq, H_mag, color='blue', lw=2)
plt.title("Magnitude of Fourier Transform of h[n] = sinc(n)")
plt.xlabel("Normalized Frequency (×π rad/sample)")
plt.ylabel("Magnitude")
plt.grid(True)
plt.ylim(0, 1.1)
plt.show()

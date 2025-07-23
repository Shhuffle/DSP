import numpy as np
from scipy.io.wavfile import write

# Parameters
start_freq = 100        # Start at 100 Hz
end_freq = 40000        # End at 40,000 Hz (upper hearing limit)
duration = 10           # Duration of the sweep in seconds
sampling_rate = 192000  # High sample rate to capture up to 40kHz (above Nyquist)

# Time vector
t = np.linspace(0, duration, int(sampling_rate * duration))

# Generate logarithmic frequency sweep
k = np.log(end_freq / start_freq) / duration
instantaneous_phase = 2 * np.pi * start_freq * (np.exp(k * t) - 1) / k
sweep_signal = 0.8 * np.sin(instantaneous_phase)  # 0.8 to avoid clipping

# Normalize and convert to 16-bit PCM
sweep_signal_int16 = np.int16(sweep_signal * 32767)

# Save as WAV
write("sweep_100Hz_to_40kHz.wav", sampling_rate, sweep_signal_int16)

print("WAV file generated: sweep_100Hz_to_40kHz.wav")

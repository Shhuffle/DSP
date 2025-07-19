import matplotlib.pyplot as plt
import soundfile as sf
import numpy as np

# Load the audio file
filename = "piano.wav"  # Enter .wav file name
discretesignal, sample_rate = sf.read(filename)

print(f"Sample Rate: {sample_rate}")
print(f"Total Sample Size: {len(discretesignal)}")
print(f"Total Audio Duration: {len(discretesignal) / sample_rate:.2f} seconds")

# Define the duration to plot (20 ms)
duration_to_plot = 0.02
samples_to_plot = int(duration_to_plot * sample_rate)

# Create time axis
time_axis = np.linspace(0, duration_to_plot, samples_to_plot)

# Shift the signal
shifted_discrete_signal = np.zeros_like(discretesignal)
N0 = 100  # Shifting factor (in samples)

for n in range(len(discretesignal)):
    if (n - N0) >= 0:
        shifted_discrete_signal[n, 0] = discretesignal[n - N0, 0]
        shifted_discrete_signal[n, 1] = discretesignal[n - N0, 1]

# Plot original and shifted signals side by side
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(14, 4))

# Original signal
axs[0].plot(time_axis, discretesignal[:samples_to_plot, 0], label='Left Channel')
axs[0].plot(time_axis, discretesignal[:samples_to_plot, 1], label='Right Channel')
axs[0].set_title("Original Signal (First 20ms)")
axs[0].set_xlabel("Time [s]")
axs[0].set_ylabel("Amplitude")
axs[0].legend()
axs[0].grid(True)

# Shifted signal
axs[1].plot(time_axis, shifted_discrete_signal[:samples_to_plot, 0], label='Left Channel')
axs[1].plot(time_axis, shifted_discrete_signal[:samples_to_plot, 1], label='Right Channel')
axs[1].set_title("Shifted Signal (First 20ms)")
axs[1].set_xlabel("Time [s]")
axs[1].set_ylabel("Amplitude")
axs[1].legend()
axs[1].grid(True)

plt.tight_layout()
plt.show()

#This code will create a .wav sound form the recording during the programme execution. 


import sounddevice as sd
import soundfile as sf

# Set parameters
duration = 5  # seconds to record
filename = 'my_recording.wav'
sampling_rate = 44100  # CD quality

# Start recording
print("Recording started...")
audio_data = sd.rec(int(duration * sampling_rate), samplerate=sampling_rate, channels=2, dtype='float32')
sd.wait()  # Wait until recording is finished
print("Recording finished.")

# Save the recorded data to a .wav file
sf.write(filename, audio_data, sampling_rate)
print(f"Audio saved to {filename}")

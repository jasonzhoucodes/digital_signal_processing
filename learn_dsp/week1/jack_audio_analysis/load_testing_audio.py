import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy as np
import sounddevice as sd

sample_rate, jack_audio = wavfile.read("jack_audio.wav")

print(f"Sample rate: {sample_rate}, Data type: {jack_audio.dtype}, # Samples: {len(jack_audio)}")
duration = len(jack_audio) / sample_rate
print(f"Duration: {duration}")


start = int(1 * sample_rate)
end = int(2 * sample_rate)

sd.play(jack_audio, sample_rate)
sd.wait()

print("just played original audio clip")

sd.play(jack_audio[start:end], sample_rate)
sd.wait()

print("just played the spliced audio clip between seconds 1 and 2")

# remember the arange method for creating the numpy array of times for corresponding samples
ts = np.arange(len(jack_audio)) / sample_rate
plt.plot(ts, jack_audio)
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.show()

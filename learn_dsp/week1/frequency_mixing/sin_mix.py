import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np

sample_rate = 44100
duration = 2
freq1 = 440
freq2 = 880

ts = np.arange(duration * sample_rate) / sample_rate
sig1 = np.sin(2 * np.pi * freq1 * ts)
sig2 = np.sin(2 * np.pi * freq2 * ts)

mixed_sig = sig1 + sig2
sd.play(mixed_sig, sample_rate)
sd.wait()

# when only plotting part of the total signal, make sure ts and signal array splices are same (same size arrays)
plt.plot(ts[:int(0.1 * sample_rate)], mixed_sig[:int(0.1 * sample_rate)])
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.show()
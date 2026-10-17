import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

sample_rate = 44100
frequency = 220
duration = 2

ts = np.arange(0, duration, 1/sample_rate)
ys = np.sin(2 * np.pi * frequency * ts)

sd.play(ys, sample_rate)
sd.wait()


plt.plot(ts[:1000], ys[:1000])
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.show()
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd

duration = 2
sample_rate = 44100
freq1 = 440
freq2 = 880

ts = np.arange(duration * sample_rate) / sample_rate
sin_sig1 = np.sin(2 * np.pi * freq1 * ts)
sin_sig2 = np.sin(2 * np.pi * freq2 * ts)

mixed_sig = sin_sig1 + sin_sig2

# here we are converting the signal mixed_sig into its corresponding specturm using rfft method 
# which is part of numpy's fft class
spectrum = np.fft.rfft(mixed_sig)
frequencies = np.fft.rfftfreq(len(mixed_sig), 1 / sample_rate)
magnitude = np.abs(spectrum)

plt.plot(frequencies, magnitude)
plt.xlim(0, 2000)
plt.xlabel("Frequencies (Hz)")
plt.ylabel("Amplitude")
plt.show()
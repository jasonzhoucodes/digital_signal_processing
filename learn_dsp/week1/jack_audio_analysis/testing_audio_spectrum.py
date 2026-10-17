from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np

sample_rate, jack_audio = wavfile.read("jack_audio.wav")

ts = np.arange(len(jack_audio)) / sample_rate
spectrum = np.fft.rfft(jack_audio)
magnitudes = np.abs(spectrum)
frequencies = np.fft.rfftfreq(len(jack_audio), 1 / sample_rate)

plt.plot(frequencies, magnitudes)
plt.xlim(0, 2000)
plt.xlabel("Frequencies (Hz)")
plt.ylabel("Amplitude")
plt.show()

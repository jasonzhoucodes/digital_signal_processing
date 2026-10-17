import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

sampling_rate = 8000 # Nyquist theorm says that highest representable frequency is 4000Hz
freq = 5000
duration = 2

ts = np.arange(duration * sampling_rate) / sampling_rate
ys = np.sin(freq * 2 * np.pi * ts)

spectrum = np.fft.rfft(ys)
freqs = np.fft.rfftfreq(len(ys), 1 / sampling_rate)
spectrum = np.abs(spectrum)

# this create 1 row 2 column subplots using matplotlib
fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.plot(ts[:10], ys[:10])
ax1.set_title("Waveform")

ax2.plot(freqs, spectrum)
ax2.set_title("Spectrum")

plt.tight_layout()
plt.show()
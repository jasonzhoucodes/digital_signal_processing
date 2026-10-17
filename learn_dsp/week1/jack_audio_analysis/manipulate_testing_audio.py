from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import time

sample_rate, jack_audio = wavfile.read("jack_audio.wav")

# when decreasing audio volume, MUST ensure that elements are still same data type (in this case 16 bit integers)
# in order to avoid implicit data type conversion errors and audio distortion
quiet = (jack_audio * 0.5).astype(np.int16)
loud = jack_audio * 2

sd.play(jack_audio, sample_rate)
sd.wait()

time.sleep(3)

sd.play(loud, sample_rate)
sd.wait()

ts = np.arange(len(jack_audio)) / sample_rate
plt.plot(ts, loud)
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.show()

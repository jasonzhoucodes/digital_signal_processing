import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

sample_rate, samples = wavfile.read("bassoon_D3_15_forte_normal.wav")


# note that samples is a numpy array where each sample was taken at corresponding time interval
print(f"Sample Rate: {sample_rate}")
print(f"Shape: {samples.shape}")
print(f"Data type: {samples.dtype}")
print(f"Number of samples: {len(samples)}")

duration = len(samples) / sample_rate

print(f"Duration: {duration} seconds")

ts = np.arange(len(samples)) / sample_rate
plt.plot(ts, samples)
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.show()
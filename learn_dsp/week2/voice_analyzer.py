import matplotlib.pyplot as plt
from scipy.signal import butter, sosfilt
import numpy as np
from scipy.io import wavfile
import sounddevice as sd
import time

sampling_rate, got_audio = wavfile.read(r"C:\Users\qingo\digital_signal_processing\learn_dsp\week2\got_s3e9_rw1.wav")

num_samples = len(got_audio)
bit_depth = got_audio.dtype
duration = num_samples / sampling_rate
print(f"Sampling rate: {sampling_rate}, Duration: {duration}, # samples: {num_samples}, bit-depth: {bit_depth}")

frames = np.arange(num_samples) / sampling_rate
freqs = np.fft.rfftfreq(num_samples, 1 / sampling_rate)
spectrum = np.abs(np.fft.rfft(got_audio))


"""
lines 22-30 create the plots for showing the waveform and spectrum of the audio
using matplotlib and a 1 row 2 column subplot
"""

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(frames, got_audio)
ax1.set_title("Waveform")

ax2.plot(freqs, spectrum)
ax2.set_title("Spectrum")

plt.tight_layout()
plt.show()


# sd.play(got_audio, sampling_rate)
# sd.wait()

# time.sleep(3)

# quieter = (got_audio * 0.5).astype(np.int16)
# sd.play(quieter, sampling_rate)
# sd.wait()

# time.sleep(3)

sos_coefficients = butter(
    N=4,
    Wn=1000,
    btype="lowpass",
    fs=sampling_rate,
    output="sos"
)

normalized_audio = got_audio.astype(np.float64) / 32768.0
lowpass_filtered = sosfilt(sos_coefficients, normalized_audio)
# plt.plot(freqs, np.abs(np.fft.rfft(lowpass_filtered)))
# plt.xlabel("Frequencies (Hz)")
# plt.ylabel("Magnitude/Intensity")
# plt.show()

sd.play(lowpass_filtered, sampling_rate)
sd.wait()

from scipy.signal import butter, sosfilt
import numpy as np
import matplotlib.pyplot as plt

sampling_rate = 16000
duration = 1.5

ts = np.arange(duration * sampling_rate) / sampling_rate
ys = np.sin(2 * np.pi * 300 * ts) + np.sin(2 * np.pi * 1000 * ts) + np.sin(2 * np.pi * 3000 * ts)

# the following uses a butterworth filter to return second-order-section coefficients for enabling 
# the filter (lowpass or highpass)
sos_coefficients = butter(
    N=4,
    Wn=2000,
    btype="lowpass",
    fs=sampling_rate,
    output="sos"
)

lowpass_filtered = sosfilt(sos_coefficients, ys)

freqs = np.fft.rfftfreq(len(ts), 1 / sampling_rate)
default_spect = np.abs(np.fft.rfft(ys))
filtered_spect = np.abs(np.fft.rfft(lowpass_filtered))

plt.plot(freqs, default_spect, label="Original")
plt.plot(freqs, filtered_spect, label="Filtered")
plt.xlim(0, 6000)

plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude (Magnitude)")
plt.show()


import numpy as np
import sounddevice as sd


# Parameters
sampling_rate = 44100
length = 2
frequency = 440.0

# Buffer
buffer = np.zeros(sampling_rate * length)

for sample_idx in range(buffer.shape[0]):
    t = sample_idx / sampling_rate  # sample time in seconds
    A = np.sin(2 * np.pi * t * frequency)

    buffer[sample_idx] = A


sd.play(buffer, sampling_rate)
sd.wait()
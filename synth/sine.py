import numpy as np

from synth import DEFAULT_SAMPLING_RATE


class SineSynth:
    sampling_rate = DEFAULT_SAMPLING_RATE

    def __init__(self, frequency):
        self.frequency = frequency

    def generate(self, length):
        buffer = np.zeros(self.sampling_rate * length)

        for sample_idx in range(buffer.shape[0]):
            t = sample_idx / self.sampling_rate  # sample time in seconds
            amp = np.sin(2 * np.pi * t * self.frequency)

            buffer[sample_idx] = amp

        return buffer

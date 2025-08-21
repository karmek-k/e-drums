import numpy as np

from synth import DEFAULT_SAMPLING_RATE


class BaseSynth:
    """Base class for synthesizers."""

    sampling_rate = DEFAULT_SAMPLING_RATE
    time_unit = 1000

    def generate(self, length):
        """Generate a buffer of synthesized samples."""

        buffer = np.zeros(self.sampling_rate * length // self.time_unit)

        for sample_idx in range(buffer.shape[0]):
            t = sample_idx / self.sampling_rate  # sample time in seconds
            amp = self.function(t)

            buffer[sample_idx] = amp

        return buffer

    def function(self, t):
        """Synthesis function."""

        return 0.0

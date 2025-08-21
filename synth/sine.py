import numpy as np

from synth import DEFAULT_SAMPLING_RATE
from synth.base import BaseSynth


class SineSynth(BaseSynth):
    """Synthesizer that generates a constant sine wave."""

    sampling_rate = DEFAULT_SAMPLING_RATE

    def __init__(self, frequency):
        self.frequency = frequency

    def function(self, t):
        return np.sin(2 * np.pi * t * self.frequency)

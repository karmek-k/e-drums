import numpy as np

from synth.base import BaseSynth


class NoiseSynth(BaseSynth):
    """Synthesizer that generates noise."""

    def __init__(self):
        self.rng = np.random.default_rng()

    def function(self, t):
        return self.rng.random() * 2.0 - 1.0
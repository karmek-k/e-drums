import numpy as np
import sounddevice as sd

from synth.sine import SineSynth


# Parameters
length = 1000  # milliseconds
frequency = 220.0  # Hz

# Synthesize
synth = SineSynth(frequency)
buffer = synth.generate(length)

# Fade out
tension = 3

fade_buffer = np.linspace(1.0, 0.00001, buffer.shape[0])
fade_buffer = fade_buffer ** tension
buffer *= fade_buffer

# Play
sd.play(buffer, synth.sampling_rate)
sd.wait()

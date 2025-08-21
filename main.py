import numpy as np
import sounddevice as sd

from synth.sine import SineSynth


# Parameters
length = 1000
frequency = 220.0

# Synthesize
synth = SineSynth(frequency)
buffer = synth.generate(length)

# Fade out
sqrt_tension = 4

fade_buffer = np.linspace(1.0, 0.00001, buffer.shape[0])
fade_buffer = np.sqrt(fade_buffer ** sqrt_tension)
buffer *= fade_buffer

# Play
sd.play(buffer, synth.sampling_rate)
sd.wait()

import sounddevice as sd

from synth.sine import SineSynth


# Parameters
length = 2
frequency = 440.0

# Synthesize
synth = SineSynth(frequency)
buffer = synth.generate(length)

# Play
sd.play(buffer, synth.sampling_rate)
sd.wait()
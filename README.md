# E-Drums

Generates sound using science and logic.

## Features

- simple synthesizers (sine wave, noise)
- fade out an existing waveform
- playback (`sounddevice` library)

## Waveform

It looks like this (it's not the exact formula used). In reality, the sine wave is generated first,
then multiplied by a polynomial factor, so that it fades out.

![waveform](readme/waveform.png)

waveform graph generated using [desmos.com](https://desmos.com)
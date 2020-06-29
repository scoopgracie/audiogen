# genaudio

The `genaudio` package provides time domain audio processing tools
using Python generators. 

This makes some types of audio sample generation and processing pretty 
easy::

	# mix 440 Hz and 445 Hz tones to get 5 Hz beating
	beats = genaudio.mixer(
		(genaudio.tone(440), genaudio.tone(445)),
		[(constant(1), constant(1)),]
	)

The actual samples won't be generated or stored in memory until they're 
actually consumed – for instance, when they're being written out to disk 
in a wave \file::

    with open("output.wav", "wb") as f:
        genaudio.sampler.write_wav(f, beats)

Generators' at-consumption-time computation also allows creating 
infinitely long output, e.g. to stream to speakers rather than a file on
disk::

    genaudio.sampler.write_wav(sys.stdout, genaudio.tone(440))

Or just:

    genaudio.sampler.play(genaudio.tone(440))

You can also use standard generator tools, e.g. the itertools module, to 
handle audio data:

	beep_silence = itertools.chain(genaudio.beep(), genaudio.silence(0.5))
	infinite_beeps = itertools.cycle(beep_silence)
    
    genaudio.sampler.write_wav(sys.stdout, infinite_beeps)
	
## Soundcard output
The easiest way to play directly to a soundcard output is to use the 
`genaudio.sampler.play` function, which will play your samples using 
PyAudio:

    import genaudio
    import itertools
    import sys
    
    genaudio.sampler.play(
        itertools.cycle(itertools.chain(genaudio.beep(), genaudio.silence(0.5)))
    )

Alternatively, you could write your wave data to `stdout`, e.g. `myaudio.py`::

    import genaudio
    import itertools
    import sys
    
    genaudio.sampler.write_wav(
        sys.stdout,
        itertools.cycle(itertools.chain(genaudio.beep(), genaudio.silence(0.5)))
    )

Then pipe to a command line audio player like [Sox](http://sox.sourceforge.net):

    python myaudio.py | play -t wav -

## Installation
Install with::

    $ pip install genaudio
    $ pip install --allow-external PyAudio --allow-unverified PyAudio PyAudio

PyAudio is optional. If it's not installed, playing audio via the soundcard with
`genaudio.sampler.play()` will not be available, but generating Wave files – 
including for piping to an external player, like `sox` – will work just fine. 

Note that to install PyAudio on Mac OS X, you'll need to first install `portaudio`::

    $ brew install portaudio

## Contributing
Get the source and report any bugs on Github:

    https://github.com/scoopgracie/genaudio


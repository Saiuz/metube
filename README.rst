MeTube
======

A small Python script for downloading YouTube videos from the commandline.  MeTube is just a thin convenience wrapper around the `pafy <http://np1.github.io/pafy>`_ library, which does all the heavy lifting.

Usage::

    python gimme.py -u <YouTube video URL> [optional flags]

Optional flags::

    -o, --output:
        Path of folder for downloaded file(s).

    -a, --audio:
        Download audio only.

    -f, --format:
        Preferred file format.  Default is ``mp4`` for video and ``ogg`` for audio-only.

    -q, --quiet:
        Do not show progress in terminal.

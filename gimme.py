#!/usr/bin/env python
"""
Commandline tool for downloading YouTube videos.  MeTube is a thin convenience
wrapper around the pafy library.

Usage:

    python gimme.py -u <YouTube video URL> [optional flags]

Optional flags:

    -o, --output:
        Path of folder for downloaded file(s).
    -a, --audio:
        Download audio only.
    -f, --format:
        Preferred file format.  Default is mp4 for video and ogg for audio-only.
    -q, --quiet:
        Do not show progress in terminal.

@author Jack Peterson (jack@tinybike.net)

"""
import sys
import os
import getopt
import pafy

OUTPATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "downloads")

def download(url=None, outpath=OUTPATH, preftype=None, quiet=False, audio=False):
    if url is not None:
        if not quiet: print("Checking " + url + "...")
        try:
            video = pafy.new(url)
            if not quiet:
                print(video.title + " | " + video.author + " [" + video.duration + "]")
            if audio:
                if preftype is None: preftype = "ogg"
                outfile = video.getbestaudio(preftype=preftype).download(quiet=quiet, filepath=outpath)
            else:
                if preftype is None: preftype = "mp4"
                outfile = video.getbest(preftype=preftype).download(quiet=quiet, filepath=outpath)
            if not quiet:
                print("\nDownload complete: " + outfile)
        except IOError as exc:
            print(exc)
    else:
        print("Error: URL required!")
        print(__doc__)

def main(argv=None):
    if argv is None: argv = sys.argv
    try:
        short_opts = "hqau:o:f:"
        long_opts = ["help", "quiet", "audio", "url=", "outpath=", "format="]
        opts, vals = getopt.getopt(argv[1:], short_opts, long_opts)
    except getopt.GetoptError as e:
        sys.stderr.write(e.msg)
        sys.stderr.write("for help use --help")
        return 2
    params = {}
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(__doc__)
            return 0
        elif opt in ("-q", "--quiet"):
            params["quiet"] = True
        elif opt in ("-a", "--audio"):
            params["audio"] = True
        elif opt in ("-u", "--url"):
            params["url"] = arg
        elif opt in ("-o", "--outpath"):
            params["outpath"] = arg
        elif opt in ("-f", "--format"):
            params["preftype"] = arg
    download(**params)

if __name__ == "__main__":
    sys.exit(main())

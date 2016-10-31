#!/usr/bin/env python
"""
Usage:
    python me.py -u <URL> [optional flags]

Optional flags:
    -o, --output:
        Path of folder where downloaded file will go.
    -a, --audio:
        Download audio only.
    -q, --quiet:
        Do not show progress in terminal.

@author Jack Peterson (jack@tinybike.net)

"""
import sys
import os
import getopt
import pafy

OUTPATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "downloads")

def download(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
             outpath=OUTPATH,
             quiet=False,
             audio=False):
    if url is not None:
        if not quiet: print("Checking " + url + "...")
        try:
            video = pafy.new(url)
            if not quiet:
                print(video.title + " | " + video.author + " [" + video.duration + "]")
            if audio:
                outfile = video.getbestaudio(preftype="ogg").download(quiet=quiet, filepath=outpath)
            else:
                outfile = video.getbest(preftype="mp4").download(quiet=quiet, filepath=outpath)
            if not quiet:
                print("\nDownload complete: " + outfile)
        except IOError as exc:
            print(exc)

def main(argv=None):
    if argv is None: argv = sys.argv
    try:
        short_opts = "hqau:o:"
        long_opts = ["help", "quiet", "audio", "url=", "outpath="]
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
    download(**params)

if __name__ == "__main__":
    sys.exit(main())

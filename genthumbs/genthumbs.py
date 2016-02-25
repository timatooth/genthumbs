#!/usr/bin/env python3
# Simple batch script to generate a folder of thumbnails images
# Usage: python genthumbs.py <input dir> [output dir] (default is 'output')
# Also generates a printer friendly HTML file for viewing.
# requires Pillow library (replacement for PIL)

import glob
import os
import sys
from PIL import Image

def create_output_dir():
    outputPath = "output"  # default path
    if len(sys.argv) > 2:  # if custom output dir was supplied
        outputPath = sys.argv[2]
        if not os.path.exists(outputPath):
             os.makedirs(outputPath)
    else:  # Create the 'output' folder at CWD
        if not os.path.exists(outputPath):
            os.makedirs(outputPath)

    return outputPath


def gen_thumbnails(outputPath, long_edge=400):
    size = (long_edge, long_edge)
    for image in glob.glob(sys.argv[1] + "/*.jpg"):
        outputdir = os.path.join(outputPath, os.path.basename(image));
        im = Image.open(image)
        im.thumbnail(size, Image.LANCZOS)
        im.save(outputdir)


def gen_html(outputPath):
    css = """
    * {padding: 0px; margin: 0px;}
    body {
        font-family: 'Helvetica Neue', 'Open Sans', sans-serif;
        font-weight: 300;
        color: #EEE;
        background-color: #FFF;
        margin: auto;
        width: 98%;
    }
    img {
        margin: 1.5em;
        float: left;
    }
    """

    htmlfile = open(os.path.join(outputPath, "index.html"), "w")

    htmlfile.write("""<html><head><title>{} Thumbnails</title>
    <style type='text/css' media='all'>{}</style></head>
    <body>""".format(sys.argv[1], css))

    for image in glob.glob(outputPath + '/*.jpg'):
        htmlfile.write("<img src='{}' />".format(os.path.basename(image)))

    htmlfile.write("</body></html>")
    htmlfile.close()


def main():
    if len(sys.argv) < 2:
        print ("Usage: " + sys.argv[0] + " <input jpeg dir> [output dir]")
        exit(1)

    #check input folder
    if not os.path.exists(sys.argv[1]):
        print("Input folder '{} not found".format(sys.argv[1]))
        exit(1)

    path = create_output_dir()
    gen_thumbnails(path)
    gen_html(path)


if __name__ == "__main__":
    main();

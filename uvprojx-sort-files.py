#!/usr/bin/env python

import argparse
import os
import sys
from lxml import etree


def parseArgs():
    parser = argparse.ArgumentParser(
        description="Sort the groups of files in a Keil uVision .uvprojx file. Modifies the file in-place.",
        epilog="Example: %(prog)s MyProject.uvprojx")
    parser.add_argument('uvprojx', help="The path to the .uvprojx file.")
    return parser.parse_args()


def sortFiles(uvprojxPath):
    uvprojxDoc = etree.parse(uvprojxPath)
    scriptDir = os.path.dirname(os.path.realpath(__file__))
    xslDoc = etree.parse(os.path.join(scriptDir, 'uvprojx-sort-files.xsl'))
    transform = etree.XSLT(xslDoc)
    result = transform(uvprojxDoc)
    result.write(uvprojxPath, encoding="UTF-8", xml_declaration=True)


def main():
    args = parseArgs()
    uvprojxPath = args.uvprojx
    if not os.path.exists(uvprojxPath):
        sys.stderr.write("File not found: '{}'\n".format(uvprojxPath))
        return 1

    sortFiles(uvprojxPath)

    print("Done.")
    return 0


if __name__ == '__main__':
    sys.exit(main())

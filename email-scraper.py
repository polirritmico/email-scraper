#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import getopt
from src.pagesCollection import PagesCollection
from src.page import Page

def processUrl(arg):
    page = Page(arg)
    return page.processUrl()

def processFile(arg):
    page = Page(arg)
    page.readFile()
    return page.getMails()

def processList(arg):
    collection = PagesCollection(arg)
    collection.processAllUrls()
    print(collection.mails)
    return collection.mailsToString()

def writeOutFile(out):
    with open("out.txt", "w") as file:
        file.write(out)

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"u:l:f:",["url=","list=","file="])
    except getopt.GetoptError:
        print("Utilice -l <file.txt> para procesar un archivo de lista\nUtilice -u <url> para procesar una lista.")
        return 2

    out = ""
    for opt, arg in opts:
        if opt in ("-u", "--url"):
            print("Abriendo url: {0}".format(arg))
            out = processUrl(arg)
        elif opt in ("-l", "--list"):
            print("Abriendo archivo de lista")
            out = processList(arg)
        elif opt in ("-f","--file"):
            out = processFile(arg)

    writeOutFile(out)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import getopt
from src.pagesCollection import PagesCollection
from src.page import Page

def scrapUrl(arg):
    page = Page(arg)
    page.readHTML()
    page.processHTML()

    return page.getMail()

def scrapHtmlFile(arg):
    page = Page(arg)
    page.readFile()
    page.processHTML()

    return page.getMail()

def scrapList(arg):
    collection = PagesCollection(arg)
    collection.scrapUrlList()

    return collection.getMailList()

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
            print("Procesando url: {0}".format(arg))
            out = scrapUrl(arg)

        elif opt in ("-f","--file"):
            print("Procesando archivo html: {0}".format(arg))
            out = scrapHtmlFile(arg)

        elif opt in ("-l", "--list"):
            print("Abriendo archivo de lista: {0}")
            out = scrapList(arg)

    writeOutFile(out)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

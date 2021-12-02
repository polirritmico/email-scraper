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

    return page.getMatchData()

def scrapHtmlFile(arg):
    page = Page(arg)
    page.readFile()
    page.processHTML()

    return page.getMatchData()

def scrapListUrl(arg, verbose = True):
    collection = PagesCollection(arg, verbose)
    collection.scrapUrlList()

    return collection.getDataList()

def writeOutFile(out):
    with open("out.txt", "w") as file:
        file.write(out)

def main(argv):
    # Check input parameters
    try:
        opts, args = getopt.getopt(argv,"u:l:f",["url=","list=","file="])
    except getopt.GetoptError:
        print("Utilice -l <file.txt> para procesar un archivo de lista\nUtilice -u <url> para procesar una lista.")
        return 2

    # Parameters behaviour
    out = ""
    for opt, arg in opts:
        if opt in ("-u", "--url"):
            print("Procesando url: {0}".format(arg))
            out = scrapUrl(arg)

        elif opt in ("-f","--file"):
            print("Procesando archivo html: {0}".format(arg))
            out = scrapHtmlFile(arg)

        elif opt in ("-l", "--list"):
            print("Procesando archivo de lista: {0}".format(arg))
            out = scrapListUrl(arg)


    if out == "":
        print("ERROR: No se procesaron datos.")
        return -1
    
    print("Procesado OK\nEscribiendo archivo out.txt")
    try:
        writeOutFile(out)
    except:
        print("ERROR: No se pudo escribir el archivo out.txt")
        return -1
    
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import getopt
from src.pagesCollection import PagesCollection
from src.page import Page
from src.browser import Browser


def scrapUrl(verbose, javascript, url):
    page = Page(url)
    if javascript:
        page.readFile()
    else:
        page.readHTML_JS(Browser())
    page.processHTML()
    if verbose: print(page.getMatchData())

    return page.getMatchData()

def scrapFile(verbose, javascript, input_file):
    page = Page(input_file)
    if javascript:
        page.readFile()
    else:
        page.readHTML_JS(Browser())
    page.processHTML()
    if verbose: print(page.getMatchData())

    return page.getMatchData()

def scrapListUrl(verbose, delay, javascript, input_file):
    collection = PagesCollection(input_file, verbose, delay, javascript)
    collection.scrapUrlList()

    return collection.getDataList()

def writeOutFile(out_data, outfile):
    with open(outfile, "w") as file:
        file.write(out_data)

def usage():
    print("Utilice -l <file.txt> para procesar un archivo de lista\nUtilice -u <url> para procesar una lista.")


def main(argv):
    # Check input parameters
    try:
        opts, args = getopt.getopt( sys.argv[1:], "vd:jluf",       \
                                    [ "--verbose"    , "--delay="  \
                                    , "--javascript" , "--list"    \
                                    , "--url"        , "--file" ])
    except getopt.GetoptError:
        print("Simple-scraper: Opción inválida.")
        usage()
        return 2

    verbose     = False
    delay       = 0.125
    javascript  = False
    out_file    = "out.txt"
    in_file     = ""
    out_data    = ""

    # Setting input/output
    try: in_file = args[0]
    except:
        print("Simple-scraper: Falta archivo o url objetivo.")
        return 2
    if len(args) == 2:
        out_file = args[1]
    elif len(args) > 2:
        print("Simple-scraper: Demasiados argumentos.")
        usage()
        return 2

    for opt, arg in opts:
        # Setting up the options
        if opt in ("-v", "--verbose"):
            verbose = True
        elif opt in ("-d", "--delay"):
            delay = float(arg)
        elif opt in ("-j", "--javascript"):
            javascript = True

        # Run the proper mode
        elif opt in ("-l", "--list"):
            out_data = scrapList(in_file, verbose, delay, javascript)
            break
        elif opt in ("-u", "--url"):
            out_data = scrapURL(in_file, verbose, javascript)
            break
        elif opt in ("-f", "--file"):
            out_data = scrapFile(in_file, verbose, javascript)
            break

        else:
            print("Simple-scraper: Opción inválida.")
            usage()
            return 2

    if out_data == "":
        print("ERROR: No se procesaron datos.")
        return -1
    
    print("Procesado OK\nEscribiendo archivo {0}".format(out_file))
    try:
        writeOutFile(out_data, out_file)
    except:
        print("ERROR: No se pudo escribir el archivo.")
        return -1
    print("Archivo de salida escrito correctamente.")

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

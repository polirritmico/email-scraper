#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import getopt
from src.pagesCollection import PagesCollection, SEP
from src.page import Page
from src.browser import Browser

def launchBrowser(page):
    browser = Browser()
    page.readHTML_JS(browser)
    browser.quit()

def scrapUrl(url, verbose, javascript):
    if verbose: print(SEP + "RegEx matches:\n" + SEP)

    page = Page(url)
    if javascript:
        launchBrowser(page)
    else:
        page.readFile()
    page.processHTML()
    if verbose: print(page.getMatchData())

    if verbose: print(SEP)

    return page.getMatchData()

def scrapFile(input_file, verbose, javascript):
    page = Page(input_file)
    if javascript:
        launchBrowser(page)
    else:
        page.readFile()
    page.processHTML()
    if verbose: print(page.getMatchData())

    return page.getMatchData()

def scrapListUrl(input_file, verbose, javascript, delay):
    collection = PagesCollection(input_file, verbose, delay, javascript)
    collection.scrapUrlList()

    return collection.getDataList()

def writeOutFile(out_data, outfile):
    with open(outfile, "w") as file:
        file.write(out_data)

def usage():
    print("""
Uso: simple-scraper.py <Opciones> <Modo> <Archivo/URL> <Salida>
Busca en cada página y devuelve los resultados en un archivo de texto.

Opciones:
   -h, --help        Muestra este texto y cierra el programa.
   -v, --verbose     Para activar la salida en consola.
   -d, --delay       Para añadir un tiempo en segundos de espera entre
                     cada url. No funciona en el modo JavaScript.
   -j, --javascript  Obtiene el HTML a través de un "navegador virtual".

Modo:
   -l, --list        Para procesar un archivo de lista.
   -u, --url         Para procesar una lista.
   -f, --file        Para procesar un HTML descargado.

Ejemplo de uso:
./simple-scraper.py -vj -d 2 --url http://www.pagina.com salida.txt
""")


def main(argv):
    # Check input parameters
    try:
        opts, args = getopt.getopt( sys.argv[1:] , "hvjd:luf", ["help", "verbose", "javascript", "delay=" , "list" , "url", "file"])
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
    try:
        in_file = args[0]
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
        if opt in ("-h", "--help"):
            usage()
        elif opt in ("-v", "--verbose"):
            verbose = True
        elif opt in ("-j", "--javascript"):
            javascript = True
        elif opt in ("-d", "--delay"):
            delay = float(arg)

        # Run the proper mode
        elif opt in ("-l", "--list"):
            out_data = scrapListUrl(in_file, verbose, javascript, delay)
            break
        elif opt in ("-u", "--url"):
            out_data = scrapUrl(in_file, verbose, javascript)
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
    
    print("Procesado OK\nEscribiendo archivo {0}...".format(out_file))
    try:
        writeOutFile(out_data, out_file)
    except:
        print("ERROR: No se pudo escribir el archivo.")
        return -1
    print("Archivo escrito correctamente.")

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
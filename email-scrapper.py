#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from src.page import Page

class PagesCollection:
    def __init__(self, _file):
        # Read the list file
        self.list_file = ""
        with open (_file, "r") as file:
            self.list_file = file.read()

def main(argv):
    print("Leyendo lista de páginas en archivo: ")
    print(str(sys.argv[1]))
    #read the file
    pages_collection = PagesCollection(sys.argv[1])
    
    #make the collection
    
    #process each



    print("Lista de páginas leída")
    print(pages_collection.list_file)
    print("Procesando las páginas:")

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

#!/usr/bin/env python
# -*- coding: utf-8 -*-

class PagesCollection:
    def __init__(self, _file):
        self.url_raw = ""
        self.url_list = []

        # Read the list file
        try:
            with open (_file, "r") as file:
                self.url_raw = file.read()
        except:
            print("Error leyendo el archivo")
            return -1

    def urlToList(self):
        for line in self.url_raw.split("\n"):
            stripped = line.strip()
            if stripped == "":
                continue
            self.url_list.append(line)

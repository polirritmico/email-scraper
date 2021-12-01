#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from src.page import Page

class PagesCollection:
    def __init__(self, _file):
        self.list_raw = ""
        self.url_list = []
        self.collected_data = []

        try:
            with open (_file, "r") as file:
                self.list_raw = file.read()
            for line in self.list_raw.splitlines():
                if line.strip() == "":
                    continue
                self.url_list.append(line)
        except:
            print("Error leyendo el archivo")
            return -1

    def scrapUrlList(self, delay = 0.125):
        for url in self.url_list:
            page = Page(url)
            page.readHTML()
            page.processHTML()
            self.collected_data.append(page.getMatchData())
            # Add a delay to avoid bans
            time.sleep(delay)

    def getDataList(self):
        out_string = ""
        for mail in self.collected_data:
            out_string += mail + "\n"

        return out_string[:-1] # return without last string

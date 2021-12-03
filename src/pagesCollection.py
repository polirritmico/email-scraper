#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from src.page import Page
from src.browser import Browser

SEP = "----------------------------------\n"

class PagesCollection:
    def __init__(self, _file, _verb = False, js = False, delay = 0.125):
        self.verbose        = _verb
        self.delay          = delay
        self.javascript     = js

        self.list_raw       = ""
        self.url_list       = []
        self.collected_data = []

        self.browser = Browser() if self.javascript else None

        try:
            with open (_file, "r") as file:
                self.list_raw = file.read()
            for line in self.list_raw.splitlines():
                self.url_list.append(line)
        except:
            print("Error leyendo el archivo [{0}]\n".format(_file))
            if self.javascript:
                self.browser.quit()
            return -1

    def scrapUrlList(self):
        if self.verbose:
            print(SEP + "RegEx matches:\n" + SEP)
            counter = 1

        for url in self.url_list:
            counter += 1
            #data_buffer.append("===========") # When a sep is needed
            if url == "":
                self.collected_data.append("")
                if self.verbose: print("")
                continue
            page = Page(url)

            if self.javascript:
                page.readHTML_JS(self.browser)
            else:
                page.readHTML()
            page.processHTML()
            self.collected_data.append(page.getMatchData())

            if self.verbose: print(page.getMatchData())
            # Add a delay to avoid bans
            time.sleep(self.delay)

        if self.verbose:
            print(SEP)
            print("Procesadas {0} páginas".format(counter))

        # Browser must be closed or will remain running on background
        if self.javascript: self.browser.quit()

    def getDataList(self):
        out_string = ""
        for mail in self.collected_data:
            out_string += mail + "\n"

        return out_string[:-1] # return without last string

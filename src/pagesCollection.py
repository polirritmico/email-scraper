#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from src.page import Page
from src.browser import Browser

SEP = "----------------------------------\n"

class PagesCollection:
    def __init__(self, _file, _verb = False, delay = 0.125, js = False):
        self.verbose        = _verb
        self.delay          = delay
        self.javascript     = js

        self.list_raw       = ""
        self.url_list       = []
        self.collected_data = []

        self.browser = None if self.javascript else Browser()

        try:
            with open (_file, "r") as file:
                self.list_raw = file.read()
            for line in self.list_raw.splitlines():
                self.url_list.append(line)
        except:
            print("Error leyendo el archivo")
            return -1

    def scrapUrlList(self):
        if self.verbose: print(SEP + "RegEx matches:\n" + SEP)

        for url in self.url_list:
            if url == "":
                self.collected_data.append("")
                if self.verbose: print("")
                continue
            page = Page(url)
            # page.readHTML_JS(self.browser) if self.javascript else page.readHTML()
            if self.javascript:
                page.readHTML_JS(self.browser)
            else:
                page.readHTML()
            page.processHTML()
            self.collected_data.append(page.getMatchData())

            if self.verbose: print(page.getMatchData())
            # Add a delay to avoid bans
            time.sleep(self.delay)

        if self.verbose: print(SEP)
        # Browser must be closed or will remain running on background
        if self.javascript: browser.quit()

    def getDataList(self):
        out_string = ""
        for mail in self.collected_data:
            out_string += mail + "\n"

        return out_string[:-1] # return without last string

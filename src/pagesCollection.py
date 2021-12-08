#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from src.page import Page
from src.browser import Browser
from src.usage import SEP
from config import SEARCH


class PagesCollection:
    def __init__( self      , input_file   , verb  = False
                , js = False, delay = 0.125, regex = SEARCH):
        self.verbose        = verb
        self.delay          = delay
        self.javascript     = js
        self.regex_search   = regex

        self.url_list       = []
        self.collected_data = []

        self.browser = Browser() if self.javascript else None

        try:
            with open (input_file, "r") as file:
                list_raw = file.read()
            for line in list_raw.splitlines():
                self.url_list.append(line)
        except:
            print("Error leyendo el archivo [{0}]\n".format(input_file))
            if self.javascript:
                self.browser.quit()
            return -1

    def scrapUrlList(self):
        if self.verbose:
            print(SEP + "RegEx matches:\n" + SEP)
            counter = 0

        for url in self.url_list:
            if url == "":
                self.collected_data.append("")
                if self.verbose: print("")
                continue
            page = Page(url, self.regex_search)

            if self.javascript:
                page.readHTML_JS(self.browser)
            else:
                page.readHTML()
            page.processHTML()
            self.collected_data.append(page.getMatchData())

            if self.verbose:
                print(self.collected_data[-1])
                counter += 1
            # Add a delay to avoid bans
            time.sleep(self.delay)

        if self.verbose:
            print(SEP)
            print("Procesadas {0} páginas".format(counter))

        # Browser MUST BE CLOSED or will remain running on background!!
        if self.javascript: self.browser.quit()

    def getDataList(self):
        out_string = ""
        for data in self.collected_data:
            out_string += data + "\n"

        return out_string[:-1] # return without last string

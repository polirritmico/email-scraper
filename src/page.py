#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import requests

class Page:
    def __init__(self, _url, regex):
        self.url          = _url
        self.html_text    = ""
        self.regex_search = regex
        self.page_data    = []

    def readHTML(self):
        # Get the web from internet
        raw_page = requests.get(self.url)
        # Get the HTML code
        self.html_text = raw_page.text

    def readHTML_JS(self, browser):
        # Get the web from the internet
        self.html_text = browser.loadWeb(self.url)

    def readFile(self):
        try:
            with open (self.url, "r") as file:
                self.html_text = file.read()
        except:
            print("ERROR: No se ha podido leer el archivo {0}".format(\
                   self.url))
            return -1

    def processHTML(self):
        data_buffer = []
        for match in re.finditer(self.regex_search, self.html_text):
            data_buffer.append(match.group(0))

        # Filter the result and remove duplicates
        self.page_data = list(filter(None, data_buffer))
        self.page_data = list(dict.fromkeys(self.page_data))

    def getMatchData(self):
        data_list = ""
        if len(self.page_data) == 1:
            return self.page_data[0].strip()
        for data in self.page_data:
            data_list += data.strip() + "\t"
        # Return without the last \t
        return data_list[:-1]

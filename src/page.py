#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import requests

EMAIL_REGEX  = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""

class Page:
    def __init__(self, _url):
        self.url = _url
        self.html_text = ""
        self.page_data = []

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
        for match in re.finditer(EMAIL_REGEX, self.html_text):
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

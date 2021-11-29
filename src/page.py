#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import requests

class Page:
    def __init__(self, _url)
        self.url = _url
        self.html = ""
        self.mails = []

    def readHTML(self):
        try:
            raw_page = requests.get(url)
        except:
            print("Unable to load the page")

        print(raw_page)



#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import requests

EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""

class Page:
    def __init__(self, _url):
        self.url = _url
        self.raw_page = None
        self.html_text = ""
        self.mail = []

    def readHTML(self):
        self.raw_page = requests.get(self.url)
        self.html_text = self.raw_page.text

    def readFile(self):
        try:
            with open (self.url, "r") as file:
                self.html_text = file.read()
        except:
            print("Error leyendo el archivo")
            return -1

    def processHTML(self):
        mail_temp = []
        for match in re.finditer(EMAIL_REGEX, self.html_text):
            mail_temp.append(match.group(0))

        # filter the result and remove duplicates
        self.mail = list(filter(None, mail_temp))
        self.mail = list(dict.fromkeys(self.mail))

    def getMail(self):
        mail_list = ""
        if len(self.mail) == 1:
            return self.mail[0]
        for mail in self.mail:
            mail_list += mail + "\t"

        return mail_list

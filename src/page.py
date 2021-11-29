#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import requests

EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""

class Page:
    def __init__(self, _url):
        self.url = _url
        self.html = ""
        self.mails = []
        self.raw_page = [] # type?

    def readHTML(self):
        raw_page = requests.get(self.url)
        self.html = raw_page.text

        return self.html

    def getMails(self):
        mails_raw = []
        for match in re.finditer(EMAIL_REGEX, self.html):
            mails_raw.append(match.group(0))

        # filter the result
        self.mails = list(filter(None, mails_raw))
        # remove duplicates
        self.mails = list(dict.fromkeys(self.mails))

        if len(self.mails) == 1:
            return self.mails[0]
        return self.mails

    def getMailList(self):
        mail_list = ""
        for mail in self.mails:
            mail_list = mail_list + "\n" + mail

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.page import Page

class PagesCollection:
    def __init__(self, _file):
        self.list_raw = ""
        self.url_list = []
        self.mails = []

        try:
            with open (_file, "r") as file:
                self.list_raw = file.read()
            for line in self.list_raw.split("\n"):
                if line.strip() == "":
                    continue
                self.url_list.append(line)
        except:
            print("Error leyendo el archivo")
            return -1

    def scrapUrlList(self):
        for url in self.url_list:
            page = Page(url)
            page.readHTML()
            page.processHTML()
            self.mails.append(page.getMail())

    def getMailList(self):
        out_string = ""
        for mail in self.mails:
            out_string += mail + "\n"

        return out_string[:-1] # return without last string

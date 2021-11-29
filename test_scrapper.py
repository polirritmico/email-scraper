#!/usr/bin/env python
#  -*- coding: utf-8 -*-

import unittest
import os
# import classes from the script
from src.page import Page

class TestInputs(unottest.TestCase):
    def setUp(self):
        self.html_collection = []
        for filename in sorted(os.listdir("testFiles/")):
            file = open(("testFiles/" + filename), "r")
            html = file.read()
            file.close()
            page = Page("testFiles/" + filename)
            self.html_collection.append(page)

    def test_uc01(self):
        url = "http://derecho.uc.cl/es/profesores/nomina-por-departamento/departamento-de-derecho-privado/581-lyon-puelma-alberto"
        expected = "alyonp@uc.cl"
        for page in html_collection:
            if page.filename != url:
                continue
            mail = page.getMail()
            self.assert_equal(expected, mail)


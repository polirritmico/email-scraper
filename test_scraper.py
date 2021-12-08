#!/usr/bin/env python
#  -*- coding: utf-8 -*-

import unittest
import os

# import classes from the script
from src.page import Page
from src.pagesCollection import PagesCollection
from src.browser import Browser

@unittest.skip
class TestInputs(unittest.TestCase):
    def test_get_web_file(self):
        url = "http://derecho.uc.cl/es/profesores/nomina-por-departamento/departamento-de-derecho-privado/581-lyon-puelma-alberto"
        page = Page(url)
        page.readHTML()
        out = page.html_text

        self.assertIsNotNone(out)

    def test_get_local_file(self):
        file = "testFiles/test_uc01.html"
        expected = "alyonp@uc.cl"

        page = Page(file)
        page.readFile()
        page.processHTML()
        out = page.getMatchData()

        self.assertEqual(expected, out)

@unittest.skip
class TestMails(unittest.TestCase):
    def test_get_mail_uc01(self):
        url = "http://derecho.uc.cl/es/profesores/nomina-por-departamento/departamento-de-derecho-privado/581-lyon-puelma-alberto"
        expected = "alyonp@uc.cl"

        page = Page(url)
        page.readHTML()
        page.processHTML()
        out = page.getMatchData()

        self.assertEqual(expected, out)

    def test_get_mail_uchile(self):
        url = "https://www.uchile.cl/portafolio-academico/perfilAcademico.jsf?username=fabbott"
        expected = "fabbott@derecho.uchile.cl\tmesadeayuda@uchile.cl"

        page = Page(url)
        page.readHTML()
        page.processHTML()
        out = page.getMatchData()

        self.assertEqual(expected, out)

    def test_get_mail_udp(self):
        url = "https://www.udp.cl/academico/carlos-pizarro-wilson/"
        expected = "carlos.pizarro@udp.cl\tprensa@mail.udp.cl\tmesa.ayuda@mail.udp.cl"

        browser = Browser()
        page = Page(url)
        page.readHTML_JS(browser)
        page.processHTML()
        out = page.getMatchData()
        browser.quit()

        self.assertEqual(expected, out)

    def test_simple_web_scrap(self):
        file = "testFiles/simple_list.txt"
        expected = """alejandro.vergara@uc.cl\naferman@uc.cl"""

        collection = PagesCollection(file)
        collection.scrapUrlList()
        out = collection.getDataList()

        self.assertEqual(expected, out)

@unittest.skip
class TestList(unittest.TestCase):
    def test_get_page_url_list(self):
        file = "testFiles/simple_list.txt"
        expected="""http://derecho.uc.cl/es/profesores/nomina-por-departamento/departamento-de-derecho-publico/2201-vergara-blanco-alejandro\nhttp://derecho.uc.cl/es/profesores/nomina-por-departamento/departamento-de-derecho-publico/459-fermandois-vohringer-arturo"""

        collection = PagesCollection(file)
        out = "\n".join(collection.url_list)

        self.assertEqual(expected, out)

    def test_skip_list_element_01(self):
        file = "testFiles/skip_list_element-01.txt"
        expected = """alyonp@uc.cl\n\nalejandro.vergara@uc.cl\naferman@uc.cl"""

        collection = PagesCollection(file)
        collection.scrapUrlList()
        out = collection.getDataList()

        self.assertEqual(expected, out)

    def test_skip_list_element_02(self):
        file = "testFiles/skip_list_element-02.txt"
        expected = """fabbott@derecho.uchile.cl\tmesadeayuda@uchile.cl\nsaccorsi@derecho.uchile.cl\tmesadeayuda@uchile.cl\n\npaguayo@derecho.uchile.cl\tmesadeayuda@uchile.cl\nfaguero@derecho.uchile.cl\tmesadeayuda@uchile.cl\n\n\nlaguirre@derecho.uchile.cl\tmesadeayuda@uchile.cl"""

        collection = PagesCollection(file)
        collection.scrapUrlList()
        out = collection.getDataList()

        self.assertEqual(expected, out)

#@unittest.skip
class TestSearches(unittest.TestCase):
    def test_get_magister_uandes(self):
        url = "https://www.uandes.cl/personas/manuel-bernet-paez/"
        expected = "<li>Máster en Derecho Privado, Ilustre Colegio de Abogados de Madrid, España.</li>"

        page = Page(url)
        page.readHTML()
        page.processHTML()
        out = page.getMatchData()

        self.assertEqual(expected, out)


if __name__ == "__main__":
    unittest.main()

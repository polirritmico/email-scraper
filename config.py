#!/usr/bin/env python
# -*- coding: utf-8 -*-

# #####################################################################
#                  SELENIUM MOZILLA GECKODRIVER PATHS
# #####################################################################
#
# First install Mozilla Firefox and download the Geckodriver from
#   https://github.com/mozilla/geckodriver
# It should go in the WebDriver folder (currently shared on the repo).
# Then adjust the FIREFOX_PATH for your system:
#

FIREFOX_PATH   = r"/usr/bin/firefox-bin" # Linux
#FIREFOX_PATH   = r"C:\\Program Files\\Mozilla Firefox\\"
GECKO_PATH     = r"WebDriver/geckodriver"
GECKO_LOG_PATH = r"WebDriver/geckodriver.log"



# #####################################################################
#                         REGEX SEARCH PATTERN
# #####################################################################
#
# Adjust the SEARCH value to search what you want.
# May fail without the r and the triple quotes: r""""""
#
# More info about Regex:
#   https://docs.python.org/3/library/re.html#regular-expression-syntax
# To do some tests:
#   https://regex101.com/
# 

# Template
#SEARCH = r""""""

# This should download the page:
#SEARCH = r""".*"""

# Email search
# Taken from https://emailregex.com/
#SEARCH = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""

# Buscar correos sin = ni /
#SEARCH = r"""(?:[a-z0-9!#$%&'*+?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""

# Master
#SEARCH = r""">(.*)(M[aá](g[ií])?ster)(.*)<"""

# Doctorado UCHILE
#SEARCH = r"""li>(.*?)((Doctora?)|([Ph]\.?[Hh]\.?[Dd]\.?)) (.*?)</li"""
SEARCH = r""">(.*?)((Doctora?)|([Ph]\.?[Hh]\.?[Dd]\.?)) (.*?)</"""

# Licenciatura UC
#SEARCH = r""">(.*?)Licenciad[oa] (.+?)<"""
# Licenciatura UCHILE
#SEARCH = r""">((ABOGAD[OA])|(CON TITULO)|(LICENCIAD[OA]))[a-zA-ZáéíóúÁÉÍÓÚñÑ ,\.;\-']*</td><td class=\"\">(.*?)</td><td class=\"\">(.*?)/td></tr>"""

# Todos los datos académicos de la UCHILE. DIFICIL DE SEPARAR
#SEARCH = r"""<h2 id=\"h2Titulos\">(.*)[\s\S]*?(?=\n.*?(<script>))"""

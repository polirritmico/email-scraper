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
#FIREFOX_PATH   = r"C:\\Program Files\\Mozilla Firefox\\" # Win
GECKO_PATH     = r"WebDriver/geckodriver"
GECKO_LOG_PATH = r"WebDriver/geckodriver.log"



# #####################################################################
#                         REGEX SEARCH PATTERN
# #####################################################################
#
# Adjust the SEARCH value to search what you want or uncomment one of
# the current ones.
# Must be inside a raw string: r""""""
#
# More info about Regex:
#   https://docs.python.org/3/library/re.html#regular-expression-syntax
# To do some tests:
#   https://regex101.com/
# 

# ####################################
# Generales

# Default:
SEARCH = r""

# Download the source code (same as -s -u)
#SEARCH = r""".*"""

# Email search
# Taken from https://emailregex.com/
#SEARCH = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""

# Buscar correos sin = ni /
#SEARCH = r"""(?:[a-z0-9!#$%&'*+?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""

# Pregrados
#SEARCH = r"""([Aa]bogad[oa])|(ABOGAD[OA])|(Licenciad[oa])"""

# Master
#SEARCH = r"""<li(.*?)>(.*?)(M[aá](g[ií])?ster)(.*?)[ \n\t]*?</li>"""

# Doctorado
#SEARCH = r""">(.*?)((Doctora?)|([Ph]\.?[Hh]\.?[Dd]\.?)) (.*?)</"""

# Posdoctorado
#SEARCH = r"""<li>(([Pp]ost? ?[Dd]octorado)|([Ph]\.?[Hh]\.?[Dd]\.?)) (.*?)</li>"""

# Abogado
#SEARCH = r"""([Aa]bogad[oa])|(ABOGAD[OA])"""

# ####################################
# UCHILE

# Doctorado UCHILE
#SEARCH = r"""li>(.*?)((Doctora?)|([Ph]\.?[Hh]\.?[Dd]\.?)) (.*?)</li"""

# Licenciatura UCHILE
#SEARCH = r""">((ABOGAD[OA])|(CON TITULO)|(LICENCIAD[OA]))[a-zA-ZáéíóúÁÉÍÓÚñÑ ,\.;\-']*</td><td class=\"\">(.*?)</td><td class=\"\">(.*?)/td></tr>"""

# ####################################
# PUC

# Licenciatura UC
#SEARCH = r""">(.*?)Licenciad[oa] (.+?)<"""

# Todos los datos académicos de la UCHILE. DIFICIL DE SEPARAR
#SEARCH = r"""<h2 id=\"h2Titulos\">(.*)[\s\S]*?(?=\n.*?(<script>))"""

# Departamentos UC
#SEARCH = r"""<p class="teacher-title-category">Departamento (.+?)</p>"""

# Cargo UC
#SEARCH = r"""<p class="teacher-title-position">(.+?)</p>"""

# ####################################
# UAI

# Cargo
#SEARCH = r"""<h3>(.+?)</h3>"""

# Sede
#SEARCH = r"""<strong>Sede:</strong>(.+?)</span>"""

# ####################################
# UDP

# Académicos
#SEARCH = r"""<a class=\"card persona\" href=\"(.*?)\">(.*?)</div>"""

# Departamento
#SEARCH = r"""<p class=\"cargo\">\n?(.+?)<br> *</p>"""

# Doctorados NO FUNCIONA
#SEARCH = r""">(.*?)((Doctora?)|([Ph]\.?[Hh]\.?[Dd]\.?)) (.*?)</"""

# Pregrados
#SEARCH = r"""<p>(.*?)(([Aa]bogad[oa])|(ABOGAD[OA])|(Licenciad[oa]))(.*?)</"""

# Curriculum pdf
#SEARCH = r"""https://(.+?).pdf"""

# ####################################
# UANDES

# Cargos. Descomentar pagesCollection.py línea 42 para añadir separador
#SEARCH = r"""(<p class=\"person-title\">[ \n\t]*(.+?)</p>)|(<p>[ \n\t]*<strong>Dedicación:</strong>[ \n\t]*</p>[ \n\t]*<ul>[ \n\t]*<li>[ \n\t]*(.*?)[ \n\t]*</li>)|(<h2>[ \n\t]*Categoría Académica</h2>[ \n\t]*<ul>[ \n\t]*<li>[ \n\t]*(.*?)</li>)"""

# Master
#SEARCH = r"""<li(.*?)>(.*?)(M[aá](g[ií])?ster)(.*?)[ \n\t]*?</li>"""

# Pregrados
#SEARCH = r"""<li(.*?)>(.*?)([Aa]bogad[oa])|(ABOGAD[OA])|(Licenciad[oa])(.*?)</li>"""

# ####################################
# PUCV

# Doctorados
#SEARCH = r""">(.*?)((Doctora?)|([Ph]\.?[Hh]\.?[Dd]\.?)) (.*?)</"""

# Master
#SEARCH = r""">(M[aá](g[ií])?ster)(.*?)[ \n\t]*?</"""

# Pregrados
#SEARCH = r""">(([Aa]bogad[oa])|(ABOGAD[OA])|(Licenciad[oa]))(.+?)<"""

# ####################################
# Otros

# Lista Best Lawyers
SEARCH = r"""<div class="lawyer-title">(.*?)</"""
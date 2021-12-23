# simple-scraper
Un scraper sencillo que permite hacer búsquedas RegEx en el código html de páginas web. Las búsquedas pueden ser a páginas individuales o una lista dentro de un archivo de texto plano.

----------------------------------------

## Modo de empleo:
```
simple-scraper.py [OPCIÓN] [MODO] [ARCHIVO/URL] [SALIDA]
```

Busca y descarga las páginas especificadas en el ARCHIVO/URL y devuelve los resultados dentro del archivo de texto SALIDA.

## Opciones:
- **-h**, *--help*        Muestra este texto y cierra el programa.
- **-v**, *--verbose*     Para activar la salida en consola.
- **-d**, *--delay[=SEG]* Para añadir un tiempo en segundos de espera entre cada url. No funciona en el modo gecko.
- **-g**, *--gecko*       Obtiene el HTML a través de un "navegador virtual".
                          Para funcionar se debe configurar en **config.py**.
- **-s**, *--source*      Descarga el código fuente de la página. Funciona solo para el modo --url.

## Modo:
- **-l**, *--list*        Para procesar un archivo de lista.
- **-u**, *--url*         Para procesar una lista.
- **-f**, *--file*        Para procesar un HTML descargado.

## Ejemplo de uso:
```
./simple-scraper.py -vg -d 2 --url http://www.url.com salida.txt
```

----------------------------------------

### Archivo de entrada:
Un archivo txt con una url por línea. El programa respeta las líneas vacías para que se alinee la salida con bases de datos o tablas.

### Archivo de salida:
El archivo contendrá por cada línea las coincidencias de la búsqueda separadas por un tabulador (\\t). Las líneas vacías coincidirán con las líneas vacías del archivo de entrada.
Si no se proporciona un archivo de salida el archivo de salida por defecto es [out.txt].

### Archivo de Configuración:
Dentro de **config.py** se puede configurar para que funcione el modo gecko y los parámetros de búsqueda (RegEx). Dentro del archivo hay más información.


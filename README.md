# simple-scraper
A simple web scraper.
Currently for mails only.

----------------------------------------

## Usage
```
$ python simple-scraper.py <option> <arg>
```

**Avaliable options:**
- `-l <file>`, `--list <file>` for list.txt files. Each line must contain a url.
- `-f` `--file <file>` for downloaded HTML files.
- `-u <url>` `--url <url>` for "http://www.page.com" (without quotes).

Then the script will generate an `out.txt` file.

Check the `src/page.py` file to change the REGEX scrap.


## About

Scraper for downloading icons for libreoffice from freedesktop

### Create virtualenv for python3
#virtualenv -p /usr/bin/python3 py3env

### Switch to python3
#source py3env/bin/activate

### Notes
scrapy doesnt support python3, yet

### Scrapy shell
scrapy shell "https://cgit.freedesktop.org/libreoffice/core/tree/icon-themes/elementary/svg"

### Running
scrapy crawl icon
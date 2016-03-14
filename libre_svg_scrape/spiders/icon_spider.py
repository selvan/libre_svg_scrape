import scrapy
import os

class IconSpider(scrapy.Spider):
    name = "icon"
    start_urls = [
        "https://cgit.freedesktop.org/libreoffice/core/plain/icon-themes"
    ]

    def parse(self, response):
        selector = "ul>li>a::attr('href')"
        refs = response.css(selector)

        ## Delete link to parent dir
        del refs[0]

        for href in refs:
            url = response.urljoin(href.extract())
            if(url.endswith("/")):
                yield scrapy.Request(url, callback=self.parse)
            else:
                yield scrapy.Request(url, callback=self.download_file)
                                    
    def download_file(self, response):
        assets_dir = os.getcwd() + "/assets"
        file_path = response.url.split("icon-themes")[-1]
        asset_path = assets_dir + "/" + file_path

        try:
            if not os.path.exists(asset_path):
                os.makedirs(os.path.dirname(asset_path))
        except:
            pass
            
        with open(asset_path, 'wb') as f:
            f.write(response.body)

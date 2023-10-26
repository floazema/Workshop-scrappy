import scrapy

class ParesseuxSpider(scrapy.Spider):
    name = "paresseux"
    allowed_domains = ["www.monde-animal.fr"]
    start_urls = ["https://www.monde-animal.fr/fiches-animaux/bradypus-variegatus/"]

    def parse(self, response):
        title = response.css('.elementor-heading-title.elementor-size-default')
        titletext = title.css('::text').get()
        print(titletext)
        description = response.css('.elementor-element.elementor-element-6f094ed.elementor-widget.elementor-widget-text-editor .elementor-text-editor.elementor-clearfix p')
        descriptiontext = description.css('::text').getall()
        for text in descriptiontext:
            print(text, end ="")
        pass
import scrapy
import csv

class AllanimalsSpider(scrapy.Spider):
    name = "allanimals"
    allowed_domains = ["www.monde-animal.fr"]
    start_urls = ["https://www.monde-animal.fr/liste-animaux-a-z/"]

    def __init__(self):
        self.csv_file = "animals.csv"
        with open(self.csv_file, 'w', newline='') as file:
            pass

    def parse(self, response):
        elements = response.css('.elementor-section-wrap .elementor-widget-wrap p a')
        links = elements.css('::attr(href)').getall()

        for link in links:
            if "https://" not in link:
                continue
            yield scrapy.Request(link, callback=self.parse_animal)

    def parse_animal(self, response):
        title = response.css('.elementor-heading-title.elementor-size-default')
        titletext = title.css('::text').get()
        description = response.css('.elementor-element.elementor-element-6f094ed.elementor-widget.elementor-widget-text-editor .elementor-text-editor.elementor-clearfix p')
        descriptiontext = description.css('::text').getall()
        data = [titletext, "".join(descriptiontext)]

        with open(self.csv_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class AraniaCrawlOnu(CrawlSpider):
    name = 'crawl_onu'

    titulos_css = 'div.field-item > h4::text'

    allowed_domains = [
        'un.org'
    ]

    start_urls = [
        'https://www.un.org/en/sections/about-un/funds-programmes-specialized-agencies-and-others/'
    ]

    regla_uno = ( #  Busque todo
        Rule(
            LinkExtractor(),
            callback = 'parse_page'
            ),

    )

    url_segmento_permitido = (
        'funds-programmes-specialized-agencies-and-others'
    )

    regla_dos = (
        Rule(
            LinkExtractor(
                allow_domains= allowed_domains,
                allow= url_segmento_permitido
                ),
            callback='parse_page'
        ),

    )

    url_segmentos_restringidos = (
        'ar/sections',
        'zh/sections',
        'ru/sections'
    )

    regla_tres = (
        Rule(
            LinkExtractor(
                allow_domains= allowed_domains,
                allow= url_segmento_permitido,
                deny= url_segmentos_restringidos
            ), 
            callback = 'parse_page'
        ),

    )


    rules = regla_tres

    def parse_page(self, response):
        lista_programas_onu = response.css(self.titulos_css).extract()
        for agencia in lista_programas_onu:
            with open('onu_agencias_regla3.txt' , 'a+', encoding="utf-8") as archivo:
                archivo.write(agencia + '\n')
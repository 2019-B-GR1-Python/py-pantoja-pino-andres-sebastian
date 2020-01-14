import scrapy

class IntroSpider(scrapy.Spider):
    name = 'introduccion_spider'
    page_header = 'div.page-header.action>h1::text'
    titulos_css = 'article.product_pod>h3 > a::text'
    precios_str_css = 'article.product_pod>div.product_price>p.price_color::text'
    imagenes_css = 'article.product_pod>div.image_container>a>img.thumbnail::attr(src)'
    web_page_books_index_css = 'div.side_categories>ul>li>a::attr(href)'
    categories_sites_css = 'div.side_categories>ul>li>ul>li>a::attr(href)'
    books_index_additional_path = '/catalogue/category/'
    categories_additional_path = '/catalogue/category/books/'
    urls = [
        'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
        ]
    new_urls = []
    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)

    
    def parse(self, response):
        if(len(self.new_urls) == 0):
            self.new_urls = self.new_urls + self.get_other_url_to_visit(response)
        category = response.css(self.page_header).extract_first()
        titulos =  response.css(self.titulos_css).extract()
        precios_str =  response.css(self.precios_str_css).extract()
        precios_float = self.handle_prices(precios_str)
        imagenes_img = response.css(self.imagenes_css).extract()
        urls_images = self.handle_url(imagenes_img, 4)

        print("Category: " + category + " started writting")
        with open('info.txt', 'a+') as file:
            file.write('Category: ' + category + '\n')
            for i in range(len(titulos)):
                linea = 'Title: ' + titulos[i] + ' ,Price: ' + str(precios_float[i]) + ' , Image URL: ' + urls_images[i] + '\n'
                file.write(linea) 

        print("Category: " + category + " finished writting")
        for url in self.new_urls:
            yield scrapy.Request(
                url = url,
                callback = self.parse)

    def handle_prices(self, prices):
        prices_float = []
        for price in prices:
            try:
                new_price = price[1:]
                price_number = float(new_price)
                prices_float.append(price_number)
            except ValueError:
                print("Unable to convert")      
        return prices_float

    def handle_url(self, urls, times, aditional_path = '/'):
        new_urls = []
        web_page_name = 'http://books.toscrape.com'
        path = web_page_name + aditional_path
        relative_path = '../'*times
        for url in urls:
            if (url == 'index.html'):
                continue
            else:
                new_url = url.replace(relative_path,path)
            new_urls.append(new_url)       
        return new_urls

    def get_other_url_to_visit(self, response):
        url_index_relative = response.css(self.web_page_books_index_css).extract()
        url_index = self.handle_url(url_index_relative, 2, self.books_index_additional_path)
        url_categories_relative = response.css(self.categories_sites_css).extract()
        url_categories = self.handle_url(url_categories_relative, 1, self.categories_additional_path)
        urls_sides = url_index + url_categories
        return urls_sides
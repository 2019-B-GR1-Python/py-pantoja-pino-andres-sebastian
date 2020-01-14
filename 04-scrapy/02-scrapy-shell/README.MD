# Scrapy
## Scrapy instalación

Ejecutar dentro del `Anaconda promt`
```
$ pip install scrapy
```
## Comandos generales

```
$ scrapy bench
```
Permite conocer las características para poder hacer Web Scraping o Web Crawling de determinado computador

```
$ scrapy settings
```
Indica las configuraciones extra de Scrapy
```
$ scrapy version
```
Devuelve la versión de scrapy con la que se está trabajando.
La versión para la fecha 01/11/2020 es la 1.8.0

## Visitar un página web
```
$ scrapy view url
```

Visualizar la página web con scrapy para ver si podemos trabajar con esa página


```
$ scrapy shell url
```

Permite interactuar con la respuesta de scrapy


```
$ response.css('id|clase|etiqueta')
```


```
$ response.css('id|clase|etiqueta').extract()
```


```
$ response.css('id|clase|etiqueta::propiedad')
```


```
$ response.css('id|clase|etiqueta::propiedad')
```


```
$ response.css('.row > div > div:nth-child(2) > .text::text').extract()
```

## Xpath

```
$ response.xpath("/html/body/div/div[2]/div[2]/h2").extract_first()
```

```
$ response.xpath("//div[@class='quote']/span[@class='text']").extract_first()
```

```
$ response.xpath("//div[@class='quote']/span/a/@href").extract_first()
```

## Spiders


#### Se usa 'scrapy startproject nombreProyecto'
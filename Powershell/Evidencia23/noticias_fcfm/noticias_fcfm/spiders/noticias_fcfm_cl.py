import scrapy



class NoticiasSpider(scrapy.Spider):

    name = "noticias"

    allowed_domains = ["fcfm.uanl.mx"]

    start_urls = ["https://www.fcfm.uanl.mx/noticias/"]



    def __init__(self, termino="FCFM", **kwargs):

        super().__init__(**kwargs)

        self.termino = termino.upper()

        self.archivo = open("resultados.txt", "w", encoding="utf-8")



    def parse(self, response):

        # Extraer títulos de noticias

        for noticia in response.css("h3"):

            titulo = noticia.css("::text").get()

            if titulo and self.termino in titulo.upper():

                limpio = titulo.strip()

                print("-- ", limpio)

                self.archivo.write(limpio + "\n")



        # Buscar enlace a la siguiente página

        siguiente = response.css("a.next.page-numbers::attr(href)").get()

        if siguiente and "noticias" in siguiente:

            yield response.follow(siguiente, callback=self.parse)



    def closed(self, reason):

        self.archivo.close()
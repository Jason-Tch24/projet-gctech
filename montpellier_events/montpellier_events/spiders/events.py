import scrapy

class EventsSpider(scrapy.Spider):
    name = "events"
    
    def start_requests(self):
        URL = "https://www.montpellier-tourisme.fr/sejourner/loisirs-et-activites/tous-les-loisirs-et-activites/"
        yield scrapy.Request(url=URL, callback=self.response_parser)

    def response_parser(self, response):
        for selector in response.css('article.rc_lego'):
            yield {
                'id': selector.css('::attr(data-sheet-id)').extract_first(),
                'title': selector.css('img.main-img::attr(title)').extract_first(),
                'image': selector.css('img.main-img::attr(src)').extract_first(),
                'category': selector.css('p.item-infos-type::text').extract_first(),
                'description': selector.css("p.item-infos-desc::text").extract_first(),
                'location': selector.css('adress::text').extract_first(),
                'presentation': selector.css('a::attr(href)').extract_first(),
                'reservation': selector.css('div.responsive-chip::attr(data-link)').extract_first(),
                'prix': selector.css('span.item-tariffs-value::text').extract_first(),
            }

        next_page = response.css('li.page-item.active + li.page-item a.page-link::attr(href)').get()

        # Vérifier si une page suivante existe et effectuer une requête
        if next_page:
            yield response.follow(next_page, callback=self.response_parser)
import csv
import scrapy
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher

import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore

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

def events_spider_result():
    event_results = []

    def crawler_results(item):
        event_results.append(item)

    dispatcher.connect(crawler_results, signal=signals.item_scraped)
    crawler_process = CrawlerProcess()
    crawler_process.crawl(EventsSpider)
    crawler_process.start()
    return event_results

def batch_data(iterable, n=1):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx:min(ndx + n, l)]


if __name__ == "__main__":
    events_data = events_spider_result()

    keys = events_data[0].keys()

    with open("event_data.csv", "w", newline="", encoding="utf-8") as output_file_name:
        writer = csv.DictWriter(output_file_name, keys)
        writer.writeheader()
        writer.writerows(events_data)
    
    print(events_data[0]['location'])
    cred = credentials.Certificate("./activity-6cc21-firebase-adminsdk-s3s1g-2c35f96f0c.json")
    app = firebase_admin.initialize_app(cred)

    store = firestore.client()
    for event in events_data :

        doc_ref = store.collection(u'activities')
        doc_ref.add({
            u'address': event['location'], 
            u'category': event['category'], 
            u'desciption': event['description'], 
            u'image': event['image'],
            u'link': event['presentation'],
            u'price': event['prix'],
            u'reservation': event['reservation'],
            u'title': event['title']
            })
        
    '''
    data = []
    headers = []
    collection_name = "activities"
    line_count = 0

    with open("./event_data.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                for header in row:
                    headers.append(header)
                line_count += 1
            else:
                obj = {}
                for idx, item in enumerate(row):
                    obj[headers[idx]] = item
                data.append(obj)
                line_count += 1
        print(f'Processed {line_count} lines.')

    for batched_data in batch_data(data, 499):
        batch = store.batch()
        for data_item in batched_data:
            doc_ref = store.collection(collection_name).document()
            batch.set(doc_ref, data_item)
        batch.commit()

    print('Done')'''
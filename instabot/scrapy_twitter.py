import scrapy


class TwitterScrapy(scrapy.Spider):
    name = 'twitter'
    start_urls = ['https://trends24.in/brazil/']
    hashtags_dia_lista = []

    def parse(self, response):
        hashtags_trends_response = response.xpath('//body//div//ol//li//a/text()').getall()

        for loop in range(5):
            hashtags_trend_bruto = hashtags_trends_response[loop].replace('#', '').replace(' ', '')
            hashtags_trend = "".join(hashtags_trend_bruto)
            self.hashtags_dia_lista.append(hashtags_trend)
            yield {'top_5': hashtags_trend}

        hashtags_dia = open("top_5_hashtags_do_dia.txt", "w")
        hashtags_dia.writelines(','.join(self.hashtags_dia_lista))
        hashtags_dia.close()

import scrapy


class AirbnbSpider(scrapy.Spider):

    name = 'airbnb'

    custom_settings = {
        "DOWNLOAD_DELAY": 3,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 3,
        "HTTPCACHE_ENABLED": True
    }

    start_urls = [
         'https://www.airbnb.com/s/Upper-Manhattan--NY/homes',
         'https://www.airbnb.com/s/Marble-Hill--NY/homes',
         'https://www.airbnb.com/s/Inwood--NY/homes',
         'https://www.airbnb.com/s/Fort-George--NY/homes',
         'https://www.airbnb.com/s/Washington-Heights--NY/homes',
         'https://www.airbnb.com/s/Hudson-Heights--NY/homes',
         'https://www.airbnb.com/s/West-Harlem--NY/homes',
         'https://www.airbnb.com/s/Hamilton-Heights--NY/homes',
         'https://www.airbnb.com/s/Manhattanville--NY/homes',
         'https://www.airbnb.com/s/Morningside-Heights--NY/homes',
         'https://www.airbnb.com/s/Central-Harlem--NY/homes',
         'https://www.airbnb.com/s/Harlem--NY/homes',
         "https://www.airbnb.com/s/Strivers'-Row--NY/homes",
         'https://www.airbnb.com/s/Astor-Row--NY/homes',
         'https://www.airbnb.com/s/Sugar-Hill--NY/homes',
         'https://www.airbnb.com/s/Marcus-Garvey-Park--NY/homes',
         'https://www.airbnb.com/s/Le-Petit-Senegal--NY/homes',
         'https://www.airbnb.com/s/East-Harlem--NY/homes',
         'https://www.airbnb.com/s/Upper-East-Side--NY/homes',
         'https://www.airbnb.com/s/Lenox-Hill--NY/homes',
         'https://www.airbnb.com/s/Carnegie-Hill--NY/homes',
         'https://www.airbnb.com/s/Yorkville--NY/homes',
         'https://www.airbnb.com/s/Upper-West-Side--NY/homes',
         'https://www.airbnb.com/s/Manhattan-Valley--NY/homes',
         'https://www.airbnb.com/s/Lincoln-Square--NY/homes',
         'https://www.airbnb.com/s/San-Juan-Hill--NY/homes',
         'https://www.airbnb.com/s/Midtown--NY/homes',
         'https://www.airbnb.com/s/Columbus-Circle--NY/homes',
         'https://www.airbnb.com/s/Sutton-Place--NY/homes',
         'https://www.airbnb.com/s/Rockefeller-Center--NY/homes',
         'https://www.airbnb.com/s/Diamond-District--NY/homes',
         'https://www.airbnb.com/s/Theater-District--NY/homes',
         'https://www.airbnb.com/s/Turtle-Bay--NY/homes',
         'https://www.airbnb.com/s/Tudor-City--NY/homes',
         'https://www.airbnb.com/s/Little-Brazil--NY/homes',
         'https://www.airbnb.com/s/Times-Square--NY/homes',
         'https://www.airbnb.com/s/Hudson-Yards--NY/homes',
         "https://www.airbnb.com/s/Hell's-Kitchen--NY/homes",
         'https://www.airbnb.com/s/Garment-District--NY/homes',
         'https://www.airbnb.com/s/Herald-Square--NY/homes',
         'https://www.airbnb.com/s/Koreatown--NY/homes',
         'https://www.airbnb.com/s/Murray-Hill--NY/homes',
         'https://www.airbnb.com/s/Tenderloin--NY/homes',
         'https://www.airbnb.com/s/Madison-Square--NY/homes',
         'https://www.airbnb.com/s/Hudson-Yards--NY/homes',
         'https://www.airbnb.com/s/Kips-Bay--NY/homes',
         'https://www.airbnb.com/s/Rose-Hill--NY/homes',
         'https://www.airbnb.com/s/NoMad--NY/homes',
         'https://www.airbnb.com/s/Peter-Cooper-Village--NY/homes',
         'https://www.airbnb.com/s/Gas-House-district--NY/homes',
         'https://www.airbnb.com/s/Chelsea--NY/homes',
         'https://www.airbnb.com/s/Flatiron-District--NY/homes',
         'https://www.airbnb.com/s/Gramercy-Park--NY/homes',
         'https://www.airbnb.com/s/Stuyvesant-Square--NY/homes',
         'https://www.airbnb.com/s/Union-Square--NY/homes',
         'https://www.airbnb.com/s/Stuyvesant-Town--NY/homes',
         'https://www.airbnb.com/s/Gas-House-district--NY/homes',
         'https://www.airbnb.com/s/Meatpacking-District--NY/homes',
         'https://www.airbnb.com/s/Waterside-Plaza--NY/homes',
         'https://www.airbnb.com/s/Downtown-Manhattan--NY/homes',
         'https://www.airbnb.com/s/Little-Germany--NY/homes',
         'https://www.airbnb.com/s/Alphabet-City-and-Loisaida--NY/homes',
         'https://www.airbnb.com/s/East-Village--NY/homes',
         'https://www.airbnb.com/s/Greenwich-Village--NY/homes',
         'https://www.airbnb.com/s/NoHo--NY/homes',
         'https://www.airbnb.com/s/Bowery--NY/homes',
         'https://www.airbnb.com/s/West-Village--NY/homes',
         'https://www.airbnb.com/s/Lower-East-Side--NY/homes',
         'https://www.airbnb.com/s/SoHo--NY/homes',
         'https://www.airbnb.com/s/Nolita--NY/homes',
         'https://www.airbnb.com/s/Little-Italy--NY/homes',
         'https://www.airbnb.com/s/Chinatown--NY/homes',
         'https://www.airbnb.com/s/Financial-District--NY/homes',
         'https://www.airbnb.com/s/Five-Points--NY/homes',
         'https://www.airbnb.com/s/Cooperative-Village--NY/homes',
         'https://www.airbnb.com/s/Two-Bridges--NY/homes',
         'https://www.airbnb.com/s/Tribeca--NY/homes',
         'https://www.airbnb.com/s/Civic-Center--NY/homes',
         'https://www.airbnb.com/s/Radio-Row--NY/homes',
         'https://www.airbnb.com/s/South-Street-Seaport--NY/homes',
         'https://www.airbnb.com/s/Battery-Park-City--NY/homes',
         'https://www.airbnb.com/s/Little-Syria--NY/homes'
    ]

    def parse(self, response):
        # Extract the links to the individual airbnb pages
        #start_url = response.url
        airbnb_names = response.xpath('//div[@class="_q8me0tf"]/div/a/span/text()').extract()
        airbnb_links = ['https://www.airbnb.com' + l for l in response.xpath('//div[@class="_q8me0tf"]/div/a/@href').extract()]
        airbnb_prices = response.xpath('//span[@class="_hylizj6"]/span[2]/text()').extract()
        airbnb_categories = response.xpath('//small[@class="_5y5o80m"]//text()').extract()[0::3]
        airbnb_beds = response.xpath('//small[@class="_5y5o80m"]//text()').extract()[2::3]

        for i in range(len(airbnb_links)):
            yield scrapy.Request(
                url=airbnb_links[i],
                callback=self.parse_airbnb, # defined later
                meta={'url': airbnb_links[i], 'name': airbnb_names[i], 'price': airbnb_prices[i],
                      'category': airbnb_categories[i], 'bed': airbnb_beds[i]} #'start_url': response.url
            )

        # Follow pagination links and repeat
        next_url = 'https://www.airbnb.com' + response.xpath('//li[@class="_b8vexar"]/a/@href').extract_first()


        yield scrapy.Request(
            url=next_url,
            callback=self.parse
        )

    def parse_airbnb(self, response):
        
        name = response.request.meta['name']
        url = response.request.meta['url']
        price = response.request.meta['price']
        category = response.request.meta['category']
        bed = response.request.meta['bed']
        city = (response.xpath('//a[@href="#neighborhood"]/text()').extract_first())
        guest = (response.xpath('//div[@class="_qtix31"]/div[2]/span/text()').extract()[0])
        bedroom = (response.xpath('//div[@class="_qtix31"]/div[2]/span/text()').extract()[1])
        bath = (response.xpath('//div[@class="_qtix31"]/div[2]/span/text()').extract()[-1])
        host = (response.xpath('//a[@href="#host-profile"]/text()').extract_first())
        detail = (response.xpath('//div[@id="details"]//text()').extract_first())
        amenity = (response.xpath('//div[@class="amenities"]//text()').extract()[2:])
        rule = (response.xpath('//div[@id="house-rules"]//text()').extract()[2:])
        n_review = (response.xpath('//span[@class="_1vbkutid"]//text()').extract_first())
        star = (response.xpath('//div[@class="star-rating-wrapper"]/@aria-label').extract_first())
        accuracy = (response.xpath('//div[@class="_1iu38l3"]//@aria-label').extract()[0])
        communication = (response.xpath('//div[@class="_1iu38l3"]//@aria-label').extract()[1])
        cleanliness = (response.xpath('//div[@class="_1iu38l3"]//@aria-label').extract()[2])
        location = (response.xpath('//div[@class="_1iu38l3"]//@aria-label').extract()[3])
        checkin = (response.xpath('//div[@class="_1iu38l3"]//@aria-label').extract()[4])
        value = (response.xpath('//div[@class="_1iu38l3"]//@aria-label').extract()[5])
        review = (response.xpath('//div[@class="review-text space-top-2"]//text()').extract())
        host_info = (response.xpath('//div[@id="host-profile"]/div/div[2]//text()').extract())
        language = (response.xpath('//div[@id="host-profile"]/div/span//text()').extract()[2:])
        response_rate = (response.xpath('//div[@id="host-profile"]/div/div[4]//text()').extract()[2])
        response_time = (response.xpath('//div[@id="host-profile"]/div/div[4]//text()').extract()[5])


        yield {
            'name': name,
            'url': url,
            'price': price,
            'category': category,
            'bed': bed,
            'city': city,
            'guest': guest,
            'bedroom': bedroom,
            'bath': bath,
            'host': host,
            'detail': detail,
            'amenity': amenity,
            'rule': rule,
            'n_review': n_review,
            'star': star,
            'accuracy': accuracy,
            'communication': communication,
            'cleanliness': cleanliness,
            'location': location,
            'checkin': checkin,
            'value': value,
            'review': review,
            'host_info': host_info,
            'language': language,
            'response_rate': response_rate,
            'response_time': response_time
        }



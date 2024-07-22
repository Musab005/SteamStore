import scrapy
from ..items import SteamstoreItem
from scrapy.loader import ItemLoader


class BestsellersSpider(scrapy.Spider):
    name = "bestsellers"
    allowed_domains = ["store.steampowered.com"]
    start_urls = ["https://store.steampowered.com/search/?filter=topsellers"]


    def parse(self, response):
        # write xpath of container of all games and hence loop over games
        games_container = response.xpath('//div[@id="search_resultsRows"]/a')
        for game in games_container:
            loader = ItemLoader(item=SteamstoreItem(), selector=game, response=response)
            print("\n \n")
            loader.add_xpath('game_url', './/@href')
            loader.add_xpath('image_url', './/div[@class="col search_capsule"]/img/@src')
            loader.add_xpath('game_name', './/div[@class="col search_name ellipsis"]/span/text()')
            loader.add_xpath('release_date', './/div[@class="col search_released responsive_secondrow"]/text()')
            loader.add_xpath('platform', './/span[contains(@class,"platform_img") or @class = "vr_supported"]/@class')
            loader.add_xpath('review', './/span[contains(@class, '
                                       '"search_review_summary")]/@data-tooltip-html')
            disc_percentage = game.xpath('.//div[@class = "discount_pct"]/text()').get()
            if disc_percentage is not None:
                loader.add_xpath('original_price', './/div[@class="discount_original_price"]/text()')
                loader.add_xpath('discount_rate', './/div[@class = "discount_pct"]/text()')
            loader.add_xpath('final_price', './/div[contains(@class,"discount_final_price")]//text()')
            yield loader.load_item()

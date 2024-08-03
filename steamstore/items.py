# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst, MapCompose


def get_platforms(item):
    platforms = []
    answer = item.split(' ')[-1]
    if answer == "group_separator":
        pass
    else:
        platforms.append(answer)
    return platforms


def clean_html(item):
    try:
        cleaned_item = item.replace('<br>', '. ')
    except TypeError:
        cleaned_item = "No review"
    return cleaned_item


def clean_spaces(item):
    try:
        cleaned_item = item.strip()
    except TypeError:
        cleaned_item = "No date specified"
    return cleaned_item


class SteamstoreItem(scrapy.Item):
    # define the fields for your item here like:
    game_url = scrapy.Field(
        output_processor=TakeFirst()
    )
    image_url = scrapy.Field(
        output_processor=TakeFirst()
    )
    game_name = scrapy.Field(
        output_processor=TakeFirst()
    )
    release_date = scrapy.Field(
        input_processor=MapCompose(clean_spaces),
        output_processor=TakeFirst()
    )
    platform = scrapy.Field(
        input_processor=MapCompose(get_platforms)
    )
    review = scrapy.Field(
        input_processor=MapCompose(clean_html),
        output_processor=TakeFirst()
    )
    original_price = scrapy.Field(
        output_processor=TakeFirst()
    )
    final_price = scrapy.Field(
        output_processor=TakeFirst()
    )
    discount_rate = scrapy.Field(
        output_processor=TakeFirst()
    )

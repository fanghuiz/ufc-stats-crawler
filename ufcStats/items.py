# -*coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Identity, TakeFirst, Compose, MapCompose, Join

STR_toInt = Compose(TakeFirst(), int)
STR_toFloat = Compose(TakeFirst(), float)


def stripPercent(str_input):
    number = str_input.strip('%')
    return float(number) / 100


class FightInfoItem(scrapy.Item):
    fight_id = scrapy.Field(output_processor=TakeFirst())
    date = scrapy.Field(output_processor=TakeFirst())
    location = scrapy.Field(output_processor=TakeFirst())
    fighter_1 = scrapy.Field(output_processor=TakeFirst())
    fighter_1_id = scrapy.Field(output_processor=TakeFirst())
    fighter_2 = scrapy.Field(output_processor=TakeFirst())
    fighter_2_id = scrapy.Field(output_processor=TakeFirst())
    winner = scrapy.Field(output_processor=TakeFirst())
    weight_class = scrapy.Field(output_processor=TakeFirst())
    #title_bout = scrapy.Field(output_processor=TakeFirst())
    decision_method = scrapy.Field(output_processor=TakeFirst())
    time_format = scrapy.Field(output_processor=TakeFirst())
    fight_duration_lastrnd = scrapy.Field(output_processor=STR_toInt)
    fight_duration_lastrnd_time = scrapy.Field(output_processor=TakeFirst())


class FightStatsItem(scrapy.Item):
    fight_id = scrapy.Field(output_processor=TakeFirst())
    fighter_id = scrapy.Field()
    fighter_name = scrapy.Field()
    fighter_status = scrapy.Field()
    kd = scrapy.Field()
    sig_str_land = scrapy.Field()
    sig_str_att = scrapy.Field()


class FighterSummaryItem(scrapy.Item):
    # define the fields for your item here like:
    fighter_id = scrapy.Field(output_processor=TakeFirst())
    name = scrapy.Field(output_processor=TakeFirst())
    height = scrapy.Field(output_processor=TakeFirst())
    weight = scrapy.Field(output_processor=TakeFirst())
    reach = scrapy.Field(output_processor=TakeFirst())
    stance = scrapy.Field(output_processor=TakeFirst())
    dob = scrapy.Field(output_processor=TakeFirst())
    active = scrapy.Field(output_processor=TakeFirst())
    n_win = scrapy.Field(output_processor=STR_toInt)
    n_loss = scrapy.Field(output_processor=STR_toInt)
    n_draw = scrapy.Field(output_processor=STR_toInt)
    sig_str_land_pM = scrapy.Field(output_processor=STR_toFloat)
    sig_str_land_pct = scrapy.Field(
        output_processor=Compose(TakeFirst(), stripPercent))
    sig_str_abs_pM = scrapy.Field(output_processor=STR_toFloat)
    sig_str_def_pct = scrapy.Field(
        output_processor=Compose(TakeFirst(), stripPercent))
    td_avg = scrapy.Field(output_processor=STR_toFloat)
    td_land_pct = scrapy.Field(
        output_processor=Compose(TakeFirst(), stripPercent))
    td_def_pct = scrapy.Field(
        output_processor=Compose(TakeFirst(), stripPercent))
    sub_avg = scrapy.Field(output_processor=STR_toFloat)

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


class FightsItem(scrapy.Item):
    fight_id = scrapy.Field(output_processor=TakeFirst())
    ## Fight summary, yields to csv
    date = scrapy.Field(output_processor=TakeFirst())
    location = scrapy.Field(output_processor=TakeFirst())
    fighter_1 = scrapy.Field(output_processor=TakeFirst())
    fighter_1_id = scrapy.Field(output_processor=TakeFirst())
    fighter_2 = scrapy.Field(output_processor=TakeFirst())
    fighter_2_id = scrapy.Field(output_processor=TakeFirst())
    winner = scrapy.Field(output_processor=TakeFirst())
    weight_class = scrapy.Field(output_processor=TakeFirst())
    decision_method = scrapy.Field(output_processor=TakeFirst())
    time_format = scrapy.Field(output_processor=TakeFirst())
    fight_duration_lastrnd = scrapy.Field(output_processor=STR_toInt)
    fight_duration_lastrnd_time = scrapy.Field(output_processor=TakeFirst())
    ## Fighter stats, yields to json
    fighter_id = scrapy.Field()
    fighter_name = scrapy.Field()
    fighter_status = scrapy.Field()
    kd = scrapy.Field()
    sig_str_land = scrapy.Field()
    sig_str_att = scrapy.Field()
    total_str_land = scrapy.Field()
    total_str_att = scrapy.Field()
    td_land = scrapy.Field()
    td_att = scrapy.Field()
    n_sub = scrapy.Field()
    n_pass = scrapy.Field()
    n_rev = scrapy.Field()
    head_land = scrapy.Field()
    head_att = scrapy.Field()
    body_land = scrapy.Field()
    body_att = scrapy.Field()
    leg_land = scrapy.Field()
    leg_att = scrapy.Field()
    distance_land = scrapy.Field()
    distance_att = scrapy.Field()
    clinch_land = scrapy.Field()
    clinch_att = scrapy.Field()
    ground_land = scrapy.Field()
    ground_att = scrapy.Field()
    sig_str_abs = scrapy.Field()
    sig_str_def = scrapy.Field()
    total_str_abs = scrapy.Field()
    total_str_def = scrapy.Field()
    td_abs = scrapy.Field()
    td_def = scrapy.Field()
    head_abs = scrapy.Field()
    head_def = scrapy.Field()
    body_abs = scrapy.Field()
    body_def = scrapy.Field()
    leg_abs = scrapy.Field()
    leg_def = scrapy.Field()
    distance_abs = scrapy.Field()
    distance_def = scrapy.Field()
    clinch_abs = scrapy.Field()
    clinch_def = scrapy.Field()
    ground_abs = scrapy.Field()
    ground_def = scrapy.Field()


class UpcomingFightsItem(scrapy.Item):
    fight_id = scrapy.Field(output_processor=TakeFirst())
    date = scrapy.Field(output_processor=TakeFirst())
    location = scrapy.Field(output_processor=TakeFirst())
    fighter_1 = scrapy.Field(output_processor=TakeFirst())
    fighter_1_id = scrapy.Field(output_processor=TakeFirst())
    fighter_2 = scrapy.Field(output_processor=TakeFirst())
    fighter_2_id = scrapy.Field(output_processor=TakeFirst())
    weight_class = scrapy.Field(output_processor=TakeFirst())


class FighterSummaryItem(scrapy.Item):
    # define the fields for your item here like:
    fighter_id = scrapy.Field(output_processor=TakeFirst())
    name = scrapy.Field(output_processor=TakeFirst())
    height = scrapy.Field(output_processor=TakeFirst())
    weight = scrapy.Field(output_processor=TakeFirst())
    reach = scrapy.Field(output_processor=TakeFirst())
    stance = scrapy.Field(output_processor=TakeFirst())
    dob = scrapy.Field(output_processor=TakeFirst())
    #active = scrapy.Field(output_processor=TakeFirst())
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

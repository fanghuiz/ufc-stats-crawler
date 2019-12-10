import scrapy
from scrapy.loader import ItemLoader
from ..items import *
from ..utils import *


class FightInfoSpider(scrapy.Spider):
    name = 'fightInfo'
    start_urls = ['http://ufcstats.com/statistics/events/completed']

    def parse(self, response):
        """
        Parse the event listing page, follow link to individual events page
        """

        events_url = response.css(
            'tbody .b-statistics__table-row ::attr(href)')

        for event in events_url:
            yield response.follow(event, callback=self.parse_event_link)

    def parse_event_link(self, response):
        """
        Parse the event page, follow link to each individual fight page
        """

        event_info = response.css('.b-list__box-list-item')
        date = event_info[0].css('::text').getall()[-1]
        location = event_info[1].css('::text').getall()[-1]
        fights_url = response.css(
            '.b-fight-details__table-row ::attr(data-link)')

        for fight in fights_url:
            yield response.follow(fight,
                                  callback=self.parse_fight_info,
                                  cb_kwargs=dict(date=date, location=location))

    def parse_fight_info(self, response, date, location):
        """
        Parse fight summary info
        """
        fight_id = response.url.split('/')[-1]
        # date and location carry over from events page
        date = date.strip()
        location = location.strip()

        status = response.css(
            '.b-fight-details__person-status ::text').getall()
        names = response.css('.b-fight-details__person-name a::text').getall()
        ids = response.css(
            '.b-fight-details__person-name ::attr(href)').getall()

        fighter_1 = names[0].strip()
        fighter_2 = names[1].strip()
        fighter_1_id = ids[0].split('/')[-1]
        fighter_2_id = ids[1].split('/')[-1]

        if status[0].strip() == 'W':
            winner = fighter_1
        elif status[1].strip() == 'W':
            winner = fighter_2
        elif status[0].strip() == 'D':
            winner = 'Draw'

        weight_class = response.css(
            '.b-fight-details__fight-title ::text').getall()

        if len(weight_class) > 1:
            weight_class = weight_class[-1].strip()
        if len(weight_class) == 1:
            weight_class = weight_class[0].strip()

        # TODO: get title bout info from weightclass / fight-title
        #title_bout = weight_class

        decision_method = response.css(
            "i.b-fight-details__text-item_first [style='font-style: normal'] ::text"
        ).get()

        fight_details = response.css('.b-fight-details__text-item')

        time_format = fight_details[2].css('::text').getall()[-1]
        fight_duration_lastrnd = fight_details[0].css('::text').getall()[-1]
        fight_duration_lastrnd_time = fight_details[1].css(
            '::text').getall()[-1]

        l = ItemLoader(item=FightInfoItem(), response=response)
        l.add_value('fight_id', fight_id)
        l.add_value('date', date)
        l.add_value('location', location)
        l.add_value('fighter_1', fighter_1)
        l.add_value('fighter_1_id', fighter_1_id)
        l.add_value('fighter_2', fighter_2)
        l.add_value('fighter_2_id', fighter_2_id)
        l.add_value('winner', winner)
        l.add_value('weight_class', weight_class)
        #l.add_value('title_bout', title_bout.strip())
        l.add_value('decision_method', decision_method.strip())
        l.add_value('time_format', time_format.strip())
        l.add_value('fight_duration_lastrnd', fight_duration_lastrnd.strip())
        l.add_value('fight_duration_lastrnd_time',
                    fight_duration_lastrnd_time.strip())

        yield l.load_item()

import scrapy
from scrapy.loader import ItemLoader
from ..items import *
from ..utils import *


class FightsSpider(scrapy.Spider):
    name = 'ufcFights'
    start_urls = ['http://ufcstats.com/statistics/events/completed']

    custom_settings = {
        'ITEM_PIPELINES': {
            'ufcStats.pipelines.FightSummaryPipeline': 400,
            'ufcStats.pipelines.FightStatsPipeline': 410
        }
    }

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
        Parse fight info - fight level summary, and fighter stats
        """

        ##### Fight summary ######
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
        else:
            winner = 'NC'

        weight_class = response.css(
            '.b-fight-details__fight-title ::text').getall()

        if len(weight_class) > 1:
            weight_class = weight_class[-1].strip()
        if len(weight_class) == 1:
            weight_class = weight_class[0].strip()

        decision_method = response.css(
            "i.b-fight-details__text-item_first [style='font-style: normal'] ::text"
        ).get()

        fight_details = response.css('.b-fight-details__text-item')

        time_format = fight_details[2].css('::text').getall()[-1]
        fight_duration_lastrnd = fight_details[0].css('::text').getall()[-1]
        fight_duration_lastrnd_time = fight_details[1].css(
            '::text').getall()[-1]

        l = ItemLoader(item=FightsItem(), response=response)
        l.add_value('fight_id', fight_id)
        l.add_value('date', date)
        l.add_value('location', location)
        l.add_value('fighter_1', fighter_1)
        l.add_value('fighter_1_id', fighter_1_id)
        l.add_value('fighter_2', fighter_2)
        l.add_value('fighter_2_id', fighter_2_id)
        l.add_value('winner', winner)
        l.add_value('weight_class', weight_class)
        l.add_value('decision_method', decision_method.strip())
        l.add_value('time_format', time_format.strip())
        l.add_value('fight_duration_lastrnd', fight_duration_lastrnd.strip())
        l.add_value('fight_duration_lastrnd_time',
                    fight_duration_lastrnd_time.strip())

        ##### Fighter Stats ######
        fighter_status = response.css(
            '.b-fight-details__person-status ::text').getall()
        fighter_status = [i.strip() for i in fighter_status]

        fighter_id = response.css(
            '.b-fight-details__person-name ::attr(href)').getall()
        fighter_id = [i.split('/')[-1] for i in fighter_id]

        stats = response.css('table:not(.js-fight-table)')
        stats_total = stats[0].css(
            '.b-fight-details__table-body .b-fight-details__table-col')
        stats_str = stats[1].css(
            '.b-fight-details__table-body .b-fight-details__table-col')

        fighter_name = stats_total[0].css('a ::text').getall()

        ## Totals
        kd = stats_total[1].css('p ::text').getall()
        kd = [int(i.strip()) for i in kd]

        sig_str = stats_total[2].css('p ::text').getall()
        total_str = stats_total[4].css('p ::text').getall()
        td = stats_total[5].css('p ::text').getall()

        n_sub = stats_total[7].css('p ::text').getall()
        n_sub = [int(i.strip()) for i in n_sub]

        n_pass = stats_total[8].css('p ::text').getall()
        n_pass = [int(i.strip()) for i in n_pass]

        n_rev = stats_total[9].css('p ::text').getall()
        n_rev = [int(i.strip()) for i in n_rev]

        ## Significant strikes
        head = stats_str[3].css('p ::text').getall()
        body = stats_str[4].css('p ::text').getall()
        leg = stats_str[5].css('p ::text').getall()
        distance = stats_str[6].css('p ::text').getall()
        clinch = stats_str[7].css('p ::text').getall()
        ground = stats_str[8].css('p ::text').getall()

        #l.add_value('fight_id', fight_id)
        l.add_value('fighter_id', fighter_id)
        l.add_value('fighter_name', fighter_name)
        l.add_value('fighter_status', fighter_status)
        l.add_value('kd', kd)
        l.add_value('sig_str_land', get_element_atk(sig_str, 'landed'))
        l.add_value('sig_str_att', get_element_atk(sig_str, 'attempt'))
        l.add_value('total_str_land', get_element_atk(total_str, 'landed'))
        l.add_value('total_str_att', get_element_atk(total_str, 'attempt'))
        l.add_value('td_land', get_element_atk(td, 'landed'))
        l.add_value('td_att', get_element_atk(td, 'attempt'))
        l.add_value('n_sub', n_sub)
        l.add_value('n_pass', n_pass)
        l.add_value('n_rev', n_rev)
        l.add_value('head_land', get_element_atk(head, 'landed'))
        l.add_value('head_att', get_element_atk(head, 'attempt'))
        l.add_value('body_land', get_element_atk(body, 'landed'))
        l.add_value('body_att', get_element_atk(body, 'attempt'))
        l.add_value('leg_land', get_element_atk(leg, 'landed'))
        l.add_value('leg_att', get_element_atk(leg, 'attempt'))
        l.add_value('distance_land', get_element_atk(distance, 'landed'))
        l.add_value('distance_att', get_element_atk(distance, 'attempt'))
        l.add_value('clinch_land', get_element_atk(clinch, 'landed'))
        l.add_value('clinch_att', get_element_atk(clinch, 'attempt'))
        l.add_value('ground_land', get_element_atk(ground, 'landed'))
        l.add_value('ground_att', get_element_atk(ground, 'attempt'))
        l.add_value('sig_str_abs', get_element_dmg(sig_str, 'absorbed'))
        l.add_value('sig_str_def', get_element_dmg(sig_str, 'defended'))
        l.add_value('total_str_abs', get_element_dmg(total_str, 'absorbed'))
        l.add_value('total_str_def', get_element_dmg(total_str, 'defended'))
        l.add_value('td_abs', get_element_dmg(td, 'absorbed'))
        l.add_value('td_def', get_element_dmg(td, 'defended'))
        l.add_value('head_abs', get_element_dmg(head, 'absorbed'))
        l.add_value('head_def', get_element_dmg(head, 'defended'))
        l.add_value('body_abs', get_element_dmg(body, 'absorbed'))
        l.add_value('body_def', get_element_dmg(body, 'defended'))
        l.add_value('leg_abs', get_element_dmg(leg, 'absorbed'))
        l.add_value('leg_def', get_element_dmg(leg, 'defended'))
        l.add_value('distance_abs', get_element_dmg(distance, 'absorbed'))
        l.add_value('distance_def', get_element_dmg(distance, 'defended'))
        l.add_value('clinch_abs', get_element_dmg(clinch, 'absorbed'))
        l.add_value('clinch_def', get_element_dmg(clinch, 'defended'))
        l.add_value('ground_abs', get_element_dmg(ground, 'absorbed'))
        l.add_value('ground_def', get_element_dmg(ground, 'defended'))

        yield l.load_item()

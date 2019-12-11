import datetime
import re
from dateparser import parse


def get_element_atk(stat, element):
    if stat is None:
        return None
    f1_att = stat[0].split('of')[1].strip()
    f1_land = stat[0].split('of')[0].strip()
    f2_att = stat[1].split('of')[1].strip()
    f2_land = stat[1].split('of')[0].strip()
    if element == 'attempt':
        element = list([int(f1_att), int(f2_att)])
    if element == 'landed':
        element = list([int(f1_land), int(f2_land)])
    return element


def get_element_dmg(stat, element):
    if stat is None:
        return None
    f1_att = stat[0].split('of')[1].strip()
    f1_land = stat[0].split('of')[0].strip()
    f2_att = stat[1].split('of')[1].strip()
    f2_land = stat[1].split('of')[0].strip()
    if element == 'absorbed':
        # Absorbed - # landed by opponent
        f1_abs = int(f2_land)
        f2_abs = int(f1_land)
        element = list([f1_abs, f2_abs])
    if element == 'defended':
        # Defended - # attempts - # landed by opponent
        f1_def = int(f2_att) - int(f2_land)
        f2_def = int(f1_att) - int(f1_land)
        element = list([f1_def, f2_def])
    return element


def IS_Active(last_fight_date):
    """
    Returns True if last fight date is less than 365 days from 
    the date data lst fetched
    """
    if last_fight_date is None:
        return True
    last_fight_date_delta = parse('today') - parse(last_fight_date)
    return last_fight_date_delta < datetime.timedelta(days=365)


def print_time(time):
    time = parse(time).replace(microsecond=0).isoformat().replace(':', '-')
    return time

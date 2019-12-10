def get_element_att(stat, element):
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

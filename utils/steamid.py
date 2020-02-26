"""Steam ID

This module helps process Steam IDs.
"""


import re


def is_valid_steamid(steam_id):
    return re.match(r'^STEAM_([0-5]):([0-1]):([0-9]+)$', steam_id) is not None


def steamid_to_steam64(steam_id):
    id64_base = 76561197960265728
    a = int(steam_id[8:9])
    b = int(steam_id[10:])
    steam64 = id64_base + (b * 2) + a
    return steam64

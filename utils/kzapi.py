"""KZAPI

This module fetches data from the KZ GlobalAPI.
"""


import requests


GAPI_URL = 'https://kztimerglobal.com/api/v1.0/'
GAPI_STATUS_URL = 'https://status.global-api.com'
MAP_IMG_URL = 'https://d2u7y93d5eagqt.cloudfront.net/mapImages/thumbs/tn_'
MAPS = {}
DIFFICULTIES = {
    1: 'Very Easy',
    2: 'Easy',
    3: 'Medium',
    4: 'Hard',
    5: 'Very Hard',
    6: 'Extreme',
    7: 'Death'
}
MODES = {
    'kzt': 'kz_timer',
    'skz': 'kz_simple',
    'vnl': 'kz_vanilla'
}
MODES_ALT = {value: key for key, value in MODES.items()}
MODE_IDS = {
    'kzt': 200,
    'skz': 201,
    'vnl': 202
}
RUNTYPES = {
    'pro': 'false',
    'tp': 'true'
}
JUMPTYPES = {
    'lj': 'longjump',
    'bhop': 'bhop',
    'mbhop': 'multibhop',
    'wj': 'weirdjump',
    'dbhop': 'dropbhop',
    'cj': 'countjump',
    'laj': 'ladderjump'
}
JUMPTYPES_ALT = {value: key for key, value in JUMPTYPES.items()}
BINDTYPES = {
    'nobind': 'false',
    'bind': 'true'
}


def get_status():
    """Check GlobalAPI Status Page"""
    try:
        r = requests.get(GAPI_STATUS_URL)
        r.raise_for_status()
    except requests.exceptions.RequestException:
        return

    data = r.content
    return data


def get_maplist():
    """Get all maps (name/difficulty) from the GlobalAPI"""
    payload = {}
    payload['is_validated'] = 'true'
    payload['limit'] = 999

    try:
        r = requests.get(f'{GAPI_URL}maps', params=payload)
        r.raise_for_status()
    except requests.exceptions.RequestException:
        return

    data = r.json()
    if not data:
        return

    for x in range(len(data)):
        difficulty = data[x]['difficulty']
        MAPS[data[x]['name']] = DIFFICULTIES[difficulty]


def get_maptop(mapname, mode, runtype):
    """Search GlobalAPI in /records/top"""
    payload = {}
    payload['map_name'] = mapname
    payload['stage'] = 0
    payload['modes_list_string'] = MODES[mode]
    payload['has_teleports'] = RUNTYPES[runtype]
    payload['limit'] = 10

    try:
        r = requests.get(f'{GAPI_URL}records/top', params=payload)
        r.raise_for_status()
    except requests.exceptions.RequestException:
        return

    data = r.json()
    return data


def get_jumptop(jumptype, bindtype):
    """Search GlobalAPI in /jumpstats"""
    payload = {}
    payload['less_than_distance'] = 300 if jumptype == 'longjump' else 400
    payload['is_crouch_boost'] = BINDTYPES[bindtype]
    payload['limit'] = 10

    try:
        r = requests.get(f'{GAPI_URL}jumpstats/{jumptype}/top', params=payload)
        r.raise_for_status()
    except requests.exceptions.RequestException:
        return

    data = r.json()
    return data


def get_ranktop(mode, runtype):
    """Search GlobalAPI in /player_ranks"""
    payload = {}
    payload['finishes_greater_than'] = 0
    payload['mode_ids'] = MODE_IDS[mode]
    payload['stages'] = 0
    payload['has_teleports'] = RUNTYPES[runtype]
    payload['limit'] = 10

    try:
        r = requests.get(f'{GAPI_URL}player_ranks', params=payload)
        r.raise_for_status()
    except requests.exceptions.RequestException:
        return

    data = r.json()
    return data


def get_wrtop(mode, runtype):
    """Search GlobalAPI in /records/top/world_records"""
    payload = {}
    payload['stages'] = 0
    payload['mode_ids'] = MODE_IDS[mode]
    payload['has_teleports'] = RUNTYPES[runtype]
    payload['limit'] = 10

    try:
        r = requests.get(f'{GAPI_URL}records/top/world_records', params=payload)
        r.raise_for_status()
    except requests.exceptions.RequestException:
        return

    data = r.json()
    return data


def get_pb(steam_id, mapname, mode, runtype):
    """Search GlobalAPI in /records/top"""
    payload = {}
    payload['steam_id'] = steam_id
    payload['map_name'] = mapname
    payload['stage'] = 0
    payload['modes_list_string'] = MODES[mode]
    payload['has_teleports'] = RUNTYPES[runtype]
    payload['limit'] = 1

    try:
        r = requests.get(f'{GAPI_URL}records/top', params=payload)
        r.raise_for_status()
    except requests.exceptions.RequestException:
        return

    data = r.json()
    return data


def get_jumppb(steam_id, jumptype, bindtype):
    """Search GlobalAPI in /jumpstats"""
    payload = {}
    payload['steam_id'] = steam_id
    payload['less_than_distance'] = 300 if jumptype == 'longjump' else 400
    payload['is_crouch_boost'] = BINDTYPES[bindtype]
    payload['limit'] = 1

    try:
        r = requests.get(f'{GAPI_URL}jumpstats/{jumptype}/top', params=payload)
        r.raise_for_status()
    except requests.exceptions.RequestException:
        return

    data = r.json()
    return data


def get_rank(steam64, mode, runtype):
    """Search GlobalAPI in /player_ranks"""
    payload = {}
    payload['steamid64s'] = steam64
    payload['finishes_greater_than'] = 0
    payload['mode_ids'] = MODE_IDS[mode]
    payload['stages'] = 0
    payload['has_teleports'] = RUNTYPES[runtype]
    payload['limit'] = 1

    try:
        r = requests.get(f'{GAPI_URL}player_ranks', params=payload)
        r.raise_for_status()
    except requests.exceptions.RequestException:
        return

    data = r.json()
    return data


def get_recent_bans():
    """Search GlobalAPI in /bans"""
    payload = {}
    payload['limit'] = 10

    try:
        r = requests.get(f'{GAPI_URL}bans', params=payload)
        r.raise_for_status()
    except requests.exceptions.RequestException:
        return

    data = r.json()
    return data


def get_recent_wrs():
    """Search GlobalAPI in /records/top/recent"""
    payload = {}
    payload['stage'] = 0
    payload['limit'] = 10

    try:
        r = requests.get(f'{GAPI_URL}/records/top/recent', params=payload)
        r.raise_for_status()
    except requests.exceptions.RequestException:
        return

    data = r.json()
    return data


def get_wr(mapname, mode, runtype):
    """Search GlobalAPI in /records/top"""
    payload = {}
    payload['map_name'] = mapname
    payload['stage'] = 0
    payload['modes_list_string'] = MODES[mode]
    payload['has_teleports'] = RUNTYPES[runtype]
    payload['limit'] = 1

    try:
        r = requests.get(f'{GAPI_URL}records/top', params=payload)
        r.raise_for_status()
    except requests.exceptions.RequestException:
        return

    data = r.json()
    return data


def valid_search_leaderboard(mode, runtype):
    if (
        mode in MODE_IDS and
        runtype in RUNTYPES
    ):
        return True
    return False


def valid_search_jumppb(bindtype):
    if (bindtype in BINDTYPES):
        return True
    return False


def valid_search_jumpstats(jumptype, bindtype):
    if (
        (jumptype in JUMPTYPES or jumptype in JUMPTYPES_ALT) and
        bindtype in BINDTYPES
    ):
        return True
    return False


def valid_search_records(mapname, mode, runtype):
    if not MAPS:
        get_maplist()

    if (
        mapname in MAPS and
        mode in MODES and
        runtype in RUNTYPES
    ):
        return True
    return False


def convert_time(seconds):
    """Convert time in seconds to hours:minutes:seconds

    Args:
        seconds (float): Time in seconds

    Returns:
        string: Time in the format hours:minutes:seconds
    """
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return f'{h:.0f}:{m:.0f}:{s:.3f}'

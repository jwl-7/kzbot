# KZBOT
a python discord bot for the CS:GO - Kreedz discord server

## Commands
* Info
    - **!apistatus** - Check KZ Global API status.
    - **!kzbothelp** - DM KZBOT command list.
    - **!kzbotstatus** - KZBOT stats.
    - **!ping** - Test BOT latency.

* Records
    - **!jumptop** *\<jumptype> \<bind/nobind>* - Get top jumpstats.
    - **!maptop** *\<map> \<mode> \<runtype>* - Get top times for map.
    - **!recentwrs** - Get recent WRs.
    - **!recentbans** - Get recent bans.
    - **!wr** *\<map> \<mode> \<runtype>* - Get world record for map.

* Leaderboard
    - **!top** *\<mode> \<runtype>* - Get top players on records leaderboard.
    - **!ranktop** *\<mode> \<runtype>* - Get top players on points leaderboard.

* Personal Best Commands
    - **!jumppb** *\<bind/nobind>* - Get personal best jumpstats.
    - **!pb** *\<map> \<mode> \<runtype>* - Get personal best time for map.
    - **!rank** *\<mode> \<runtype>* - Get personal rank on points leaderboard.
    - **!setaccount** *\<steam_id>* - Register Steam ID to use !pb command.

## Command Parameters
- *\<map>* - the filename of the map
    * Examples
        * bkz_apricity_v3
        * kz_colors_v2
        * kzpro_concrete_c02
        * xc_fox_shrine_japan_fr
- *\<mode>* - the kz movement mode
    * KZ Modes
        * kzt - KZTimer
        * skz - SimpleKZ
        * vnl - Vanilla
- *\<runtype>* - the type of run for the record
    * Runtypes
        * pro - no teleports used
        * tp - teleports used
- *\<jumptype>* - the type of jumpstat
    * Jumptypes
        * lj - longjump
        * bhop - bhop
        * mbhop - multibhop
        * wj - weirdjump
        * dbhop - dropbhop
        * cj - countjump
        * laj - ladderjump

## Admin Commands
- **!adminhelp** - DM KZBOT admin command list.
- **!load** *\<name>* - Load extension.
- **!unload** *\<name>* - Unload extension.
- **!reload** *\<name>* - Reload extension.
- **!restart** - Restart KZBOT.

## Requirements
* Python 3.8+
* [discord.py](https://pypi.org/project/discord.py/)
* [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
* [psutil](https://pypi.org/project/psutil/)
* [PyYAML](https://pypi.org/project/PyYAML/)
* [requests](https://pypi.org/project/requests/)

## License
This project is released under the GNU GPL License - see the [LICENSE](LICENSE) file for details
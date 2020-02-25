# KZBOT
a python discord bot for the CS:GO - Kreedz discord server

## Commands
* Info
    - **!kzbothelp** - dm bot command list
    - **!kzbotstatus** - kzbot stats
    - **!ping** - test bot latency

* KZ Global API
    - **!apistatus** - get current status of kz global api

* Map Records
    - **!maptop** *\<map> \<mode> \<runtype>* - get top times for map
    - **!wr** *\<map> \<mode> \<runtype>* - get world record for map

* Recent
    - **!recentwrs** - get recent WRs.
    - **!recentbans** - get recent bans.

* Leaderboard
    - **!top** *\<mode>* - get top players on records leaderboard
    - **!ranktop** *\<mode>* - get top players on points leaderboard

* Jumpstats
    - **!jumptop** *\<jumptype>* - get top jumpstats

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
- **!adminhelp** - dm bot admin command list
- **!load** *\<name>* - load extension
- **!unload** *\<name>* - unload extension
- **!reload** *\<name>* - reload extension
- **!restart** - restart bot

## Requirements
* Python 3.8+
* [discord.py](https://github.com/Rapptz/discord.py)

## License
This project is released under the GNU GPL License - see the [LICENSE](LICENSE) file for details
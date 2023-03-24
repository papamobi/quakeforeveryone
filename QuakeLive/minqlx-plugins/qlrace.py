# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.


import minqlx
import time
try:
    from geolite2 import geolite2
except ImportError:
    minqlx.CHAT_CHANNEL.reply("^1Error: ^7The ^4geolite2 ^7python library isn't installed.")
    minqlx.CHAT_CHANNEL.reply(
        "Run the following on your server to install: ^3sudo python3.5 -m pip install python-geoip-geolite2")
    raise ImportError


class country(minqlx.Plugin):
    database = minqlx.database.Redis

    def __init__(self):
        super().__init__()
        self.add_hook("player_connect", self.player_connect)
        self.add_command("country", self.cmd_country)

        self.connection = []


    def player_connect(self, player):
        match = geolite2.reader()
        pmatch = match.get("{}".format(player.ip))

        @minqlx.thread
        def connect(player):
            time.sleep(10)
            self.connection.remove(player.steam_id)

        if pmatch is not None and player.steam_id not in self.connection:
            self.connection.append(player.steam_id)
            pmatching = pmatch["country"]["names"]["en"]
            country = "^7{}".format(pmatching)
            message = "{} ^2has joined from ".format(player.name) + country
            self.msg("{}".format(message))
            connect(player)

    def cmd_country(self, player, msg, channel):
        match = geolite2.reader()
        if len(msg) == 1:
            pmatch = match.get("{}".format(player.ip))
            pmatching = pmatch["country"]["names"]["en"]
            country = "^7{}".format(pmatching)
            message = "{} ^2is from {}".format(player.name, country)
            self.msg(message)
        elif len(msg) >= 2:
            if msg[1].isdigit() and len(msg[1]) <= 2:
                try:
                    i = int(msg[1])
                    target_player = self.player(i)
                    if not (0 <= i < 64) or not target_player:
                        raise ValueError
                    player = target_player
                except ValueError:
                    player.tell("Invalid ID.")
                    return minqlx.RET_STOP_ALL
                except minqlx.NonexistentPlayerError:
                    player.tell("Invalid ID.")
                    return minqlx.RET_STOP_ALL
            else:
                if msg[1] == "all":
                    for p in self.players():
                        pmatch = match.get("{}".format(p.ip))
                        pmatching = pmatch["country"]["names"]["en"]
                        country = "^7{}".format(pmatching)
                        message = "{} ^2is from ".format(p.name) + country
                        self.msg("{}".format(message))
                    return minqlx.RET_STOP_ALL
                else:
                    found = False
                    playerslist = []
                    players = self.players()
                    name_prefix = ""
                    playername = ""
                    for a in range(1, len(msg)):
                        if a == len(msg) - 1:
                            name_prefix += msg[a]
                        else:
                            name_prefix += msg[a] + " "
                    for i in players:
                        if self.clean_text(i.name).lower().startswith(name_prefix):
                            playerslist.append(self.clean_text(i.name))
                    if len(playerslist) == 0:
                        channel.reply("No player found for < {} >!".format(name_prefix))
                        return
                    else:
                        playerslist.sort(key=lambda s: len(s))
                        for m in range(len(playerslist)):
                            if name_prefix == playerslist[m].lower():
                                playername = playerslist[m]
                                found = True
                        if not found:
                            playername = playerslist[0].lower()
                        for f in players:
                            if self.clean_text(f.name).lower() == playername.lower():
                                target_player = self.player(f)
                                player = target_player
            pmatch = match.get("{}".format(player.ip))
            pmatching = pmatch["country"]["names"]["en"]
            country = "^7{}".format(pmatching)
            message = "{} ^2is from ".format(player.name) + country
            self.msg("{}".format(message))
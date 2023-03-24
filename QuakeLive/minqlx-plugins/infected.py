# minqlx - A Quake Live server administrator bot.
# Copyright (C) 2015 Mino <mino@minomino.org>

# This file is part of minqlx.

# minqlx is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# minqlx is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with minqlx. If not, see <http://www.gnu.org/licenses/>.

import minqlx

class infected(minqlx.Plugin):
    def __init__(self):
        super().__init__()
        self.add_hook("death", self.handle_death)
        self.add_hook("round_countdown", self.handle_round_countdown)

        self.skip_top3 = False
        self.skip_top1 = False

    def handle_death(self, victim, killer, data):
        @minqlx.thread
        def handle_player_death():
            if self.game and self.game.state == 'in_progress':
                teams = self.teams()
                players = self.players()

                if len(teams["blue"]) < 4 and not self.skip_top3:
                    for blue_player in teams["blue"]:
                        blue_player.weapons(pg=True)
                        blue_player.ammo(pg=100)
                        self.skip_top3 = True

                    for player in players:
                        minqlx.send_server_command(player.id, "cp \"^3Survivors received the Plasma Gun!\"")

                if len(teams["blue"]) is 1 and not self.skip_top1:
                    for blue_player in teams["blue"]:
                        blue_player.weapons(bfg=True)
                        blue_player.ammo(bfg=5)
                        self.skip_top1 = True

                    for player in players:
                        minqlx.send_server_command(player.id, "cp \"^3Last survivor received the BFG!\"")

        handle_player_death()

    def handle_round_countdown(self, round_number):
        teams = self.teams()

        for player in teams["blue"] and teams["red"]:
            player.weapons(reset=True)

        self.skip_top1 = False
        self.skip_top3 = False

# coding: utf8
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
import random
import time
import re

from minqlx.database import Redis
_re_ = {}


def add_sound(key, regex, path):
    _re_[key] = [re.compile(regex, flags=re.IGNORECASE), path]


add_sound("hahaha yeah", r"^haha(?:ha)?,? yeah?\W?$", "sound/player/lucy/taunt.wav") # not works
add_sound("haha yeah haha", r"^haha(?:ha)?,? yeah?,? haha\W?$", "sound/player/biker/taunt.wav")
add_sound("yeah hahaha", r"^yeah?,? haha(?:ha)\W?$", "sound/player/razor/taunt.wav")
add_sound("duahaha", r"^duahaha(?:ha)?\W?$", "sound/player/keel/taunt.wav")
add_sound("hahaha", r"^hahaha\W?$", "sound/player/santa/taunt.wav")
add_sound("glhf", r"^(?:gl ?hf\W?)|(?:hf\W?)|(?:gl hf\W?)", "sound/vo/crash_new/39_01.wav")
add_sound("f3", r"^(?:(?:press )?f3)|ready(?: up)?\W?", "sound/vo/crash_new/36_04.wav")
add_sound("welcome", r"^welcome to (?:ql|quake live)\W?$", "sound/vo_evil/welcome")
add_sound("go", r"^go\W?$", "sound/vo/go")
add_sound("you win", r"^you win\W?$", "sound/vo_female/you_win.wav")
add_sound("you lose", r"^you lose\W?$", "sound/vo/you_lose.wav")
add_sound("beep boop", r"^beep boop\W?$", "sound/player/tankjr/taunt.wav")
add_sound("denied", r"^denied\W?$", "sound/vo/denied")
add_sound("balls out", r"^ball'?s out\W?$", "sound/vo_female/balls_out")
add_sound("one", r"^one\W?$", "sound/vo_female/one")
add_sound("two", r"^two\W?$", "sound/vo_female/two")
add_sound("three", r"^three\W?$", "sound/vo_female/three")
add_sound("fight", r"^fight\W?$", "sound/vo_evil/fight")
add_sound("gauntlet", r"^gauntlet\W?$", "sound/vo_evil/gauntlet")
add_sound("humiliation", r"^humiliation\W?$", "sound/vo_evil/humiliation1")
add_sound("perfect", r"^perfect\W?$", "sound/vo_evil/perfect")
add_sound("wah wah wah wah", r"^wa+h wa+h wa+h wa+h\W?$", "sound/misc/yousuck")
add_sound("ah ah ah", r"^a+h a+h a+h\W?$", "sound/player/slash/taunt.wav")
add_sound("oink", r"^oink\W?$", "sound/player/sorlag/pain50_1.wav")
add_sound("argh", r"^a+rgh\W?$", "sound/player/doom/taunt.wav")
add_sound("hah haha", r"^hah haha\W?$", "sound/player/hunter/taunt.wav")
add_sound("woohoo", r"^woo+hoo+\W?$", "sound/player/janet/taunt.wav")
add_sound("quakelive | ql", r"^(?:ql|quake live)\W?$", "sound/vo_female/quake_live")
add_sound("$ | € | £", "(?:\$|€|£)\d+", "sound/misc/chaching")
add_sound("uh ah", r"^uh ah$", "sound/player/mynx/taunt.wav")
add_sound("oohwee", r"^ooh+wee\W?$", "sound/player/anarki/taunt.wav")
add_sound("erah", r"^erah\W?$", "sound/player/bitterman/taunt.wav")
add_sound("yeahhh", r"^yeahhh\W?$", "sound/player/major/taunt.wav")
add_sound("scream", r"^scream\W?$", "sound/player/bones/taunt.wav")
add_sound("salute", r"^salute\W?$", "sound/player/sarge/taunt.wav")
add_sound("squish", r"^squish\W?$", "sound/player/orb/taunt.wav")
add_sound("oh god", r"^oh god\W?$", "sound/player/ranger/taunt.wav")
add_sound("snarl", r"^snarl\W?$", "sound/player/sorlag/taunt.wav")
add_sound("007", r"^007\W?$", "sound/funnysounds/007.wav")
add_sound("adamsfamily", r"^adamsfamily\W?$", "sound/funnysounds/adamsfamily.ogg")
add_sound("allahuakbar", r"^allahuakbar\W?$", "sound/funnysounds/allahuakbar.ogg")
add_sound("allstar", r"^allstar\W?$", "sound/funnysounds/allstar.ogg")
add_sound("asskicking", r"^asskicking\W?$", "sound/funnysounds/asskicking.ogg")
add_sound("baby baby", r"^baby baby\W?$", "sound/funnysounds/babybaby.ogg")
add_sound("babylaughing", r"^babylaughing\W?$", "sound/funnysounds/babylaughing.ogg")
add_sound("Ill be back", r"^I'?ll be back\W?$", "sound/funnysounds/beback.ogg")
add_sound("benny hill", r"^benny hill\W?$", "sound/funnysounds/bennyhill.ogg")
add_sound("boom headshot", r"^boom headshot\W?$", "sound/funnysounds/boomheadshot.ogg")
add_sound("brightsideoflife", r"^brightsideoflife\W?$", "sound/funnysounds/brightsideoflife.ogg")
add_sound("bullshitter", r"^bullshitter\W?$", "sound/funnysounds/bullshitter.ogg")
add_sound("cant touch this", r"^can'?t touch this\W?$", "sound/funnysounds/canttouchthis.ogg")
add_sound("champions", r"^champions\W?$", "sound/funnysounds/champions.ogg")
add_sound("cowards", r"^cowards\W?$", "sound/funnysounds/cowards.ogg")
add_sound("damnit", r"^damnit\W?$", "sound/funnysounds/damnit.ogg")
add_sound("deadsoon", r"^deadsoon\W?$", "sound/funnysounds/deadsoon.ogg")
add_sound("defeated", r"^defeated\W?$", "sound/funnysounds/defeated.ogg")
add_sound("freestyler", r"^freestyler\W?$", "sound/funnysounds/freestyler.ogg")
add_sound("fuckfuck", r"^fuckfuck\W?$", "sound/funnysounds/fuckfuck.ogg")
add_sound("fucking kids", r"^fucking kids\W?$", "sound/funnysounds/fuckingkids.ogg")
add_sound("gangnam", r"^gangnam\W?$", "sound/funnysounds/gangnam.ogg")
add_sound("get out the way", r"^get out the way\W?$", "sound/funnysounds/getouttheway.ogg")
add_sound("girl look", r"^girl look\W?$", "sound/funnysounds/girllook.ogg")
add_sound("gnr guitar", r"^gnr guitar\W?$", "sound/funnysounds/gnrguitar.ogg")
add_sound("goddamn right", r"^goddamn right\W?$", "sound/funnysounds/goddamnright.ogg")
add_sound("gotcha", r"^gotcha\W?$", "sound/funnysounds/gotcha.ogg")
add_sound("hakunamatata", r"^hakunamatata\W?$", "sound/funnysounds/hakunamatata.ogg")
add_sound("hello", r"^hello\W?$", "sound/funnysounds/hello.ogg")
add_sound("how are you", r"^how are you\W?$", "sound/funnysounds/howareyou.ogg")
add_sound("ibet", r"^ibet\W?$", "sound/funnysounds/ibet.ogg")
add_sound("imsexy", r"^imsexy\W?$", "sound/funnysounds/imsexy.ogg")
add_sound("incoming", r"^incoming\W?$", "sound/funnysounds/incoming.ogg")
add_sound("i see assholes", r"^i see assholes\W?$", "sound/funnysounds/iseeassholes.ogg")
add_sound("jump motherfucker", r"^jump motherfucker\W?$", "sound/funnysounds/jackpot.ogg")
add_sound("just do it", r"^just do it\W?$", "sound/funnysounds/jumpmotherfucker.ogg")
add_sound("jackpot", r"^jackpot\W?$", "sound/funnysounds/justdoit.ogg")
add_sound("keep on fighting", r"^keep on fighting\W?$", "sound/funnysounds/keeponfighting.ogg")
add_sound("lion king", r"^lion king\W?$", "sound/funnysounds/lionking.ogg")
add_sound("losing my religion", r"^losing my religion\W?$", "sound/funnysounds/losingmyreligion.ogg")
add_sound("mahnamahna", r"^mahnamahna\W?$", "sound/funnysounds/mahnamahna.ogg")
add_sound("mario", r"^mario\W?$", "sound/funnysounds/mario.ogg")
add_sound("mimimi", r"^mimimi\W?$", "sound/funnysounds/mimimi.ogg")
add_sound("moan", r"^moan\W?$", "sound/funnysounds/moan.ogg")
add_sound("my name", r"^my name\W?$", "sound/funnysounds/myname.ogg")
add_sound("no time for loosers", r"^no time for loosers\W?$", "sound/funnysounds/notimeforloosers.ogg")
add_sound("rocky", r"^rocky\W?$", "sound/funnysounds/rocky")
add_sound("samba", r"^samba\W?$", "sound/funnysounds/samba.ogg")
add_sound("scatman", r"^scatman\W?$", "sound/funnysounds/silence.ogg")
add_sound("silence", r"^silence\W?$", "sound/funnysounds/scatman.ogg")
add_sound("surprise", r"^surprise\W?$", "sound/funnysounds/stayinalive.ogg")
add_sound("teamwork", r"^teamwork\W?$", "sound/funnysounds/surprise.ogg")
add_sound("stayin alive", r"^stayin alive\W?$", "sound/funnysounds/teamwork.ogg")
add_sound("this is sparta", r"^this is sparta\W?$", "sound/funnysounds/thisissparta.ogg")
add_sound("tututu", r"^tututu\W?$", "sound/funnysounds/tuturu.ogg")
add_sound("tuturu", r"^tututu\W?$", "sound/funnysounds/tuturu.ogg")
add_sound("what is love", r"^what is love\W?$", "sound/funnysounds/whatislove.ogg")
add_sound("why mad", r"^why mad\W?$", "sound/funnysounds/whymad.ogg")
add_sound("yhehehe", r"^yhehehe\W?$", "sound/funnysounds/yhehehe.ogg")
add_sound("ymca", r"^ymca\W?$", "sound/funnysounds/ymca.ogg")
add_sound("you fucked mywife", r"^you fucked mywife\W?$", "sound/funnysounds/youfuckedmywife.ogg")
add_sound("all the things", r"^all the things\W?$", "sound/funnysounds/allthethings.ogg")
add_sound("amazing", r"^amazing\W?$", "sound/funnysounds/amazing.ogg")
add_sound("ameno", r"^ameno\W?$", "sound/funnysounds/ameno.ogg")
add_sound("america", r"^america\W?$", "sound/funnysounds/america.ogg")
add_sound("amerika", r"^amerika\W?$", "sound/funnysounds/amerika.ogg")
add_sound("and nothing else", r"^and nothing else\W?$", "sound/funnysounds/andnothingelse.ogg")
add_sound("animals", r"^animals\W?$", "sound/funnysounds/animals.ogg")
add_sound("just a scratch", r"^just a scratch\W?$", "sound/funnysounds/ascratch.ogg")
add_sound("ave", r"^ave\W?$", "sound/funnysounds/ave.ogg")
add_sound("baby baby", r"^baby baby\W?$", "sound/funnysounds/babybaby.ogg")
add_sound("baby evil", r"^baby evil\W?$", "sound/funnysounds/babyevillaugh.ogg")
add_sound("benzin", r"^benzin\W?$", "sound/funnysounds/benzin.ogg")
add_sound("blue wins", r"^blue wins\W?$", "sound/funnysounds/bluewins.ogg")
add_sound("bonkers", r"^bonkers\W?$", "sound/funnysounds/bonkers.ogg")
add_sound("booo", r"^booo\W?$", "sound/funnysounds/booo.ogg")
add_sound("boring", r"^boring\W?$", "sound/funnysounds/boring.ogg")
add_sound("boze", r"^boze\W?$", "sound/funnysounds/boze.ogg")
add_sound("buckdich", r"^buckdich\W?$", "sound/funnysounds/buckdich.ogg")
add_sound("burns burns", r"^burns burns\W?$", "sound/funnysounds/burnsburns.ogg")
add_sound("camel toe", r"^camel toe\W?$", "sound/funnysounds/cameltoe.ogg")
add_sound("cccp", r"^cccp\W?$", "sound/funnysounds/cccp.ogg")
add_sound("chicken", r"^chicken\W?$", "sound/funnysounds/chicken.ogg")
add_sound("chocolate rain", r"^chocolate rain\W?$", "sound/funnysounds/chocolaterain.ogg")
add_sound("coin", r"^coin\W?$", "sound/funnysounds/coin.ogg")
add_sound("come", r"^come\W?$", "sound/funnysounds/come.ogg")
add_sound("countdown", r"^countdown\W?$", "sound/funnysounds/countdown.ogg")
add_sound("crazy", r"^crazy\W?$", "sound/funnysounds/crazy.ogg")
add_sound("you are a cunt", r"^you are a cunt\W?$", "sound/funnysounds/cunt.ogg")
add_sound("devil", r"^devil\W?$", "sound/funnysounds/devil.ogg")
add_sound("doesnt love you", r"^doesn'?t love you\W?$", "sound/funnysounds/doesntloveyou.ogg")
add_sound("du hast", r"^du hast\W?$", "sound/funnysounds/duhast.ogg")
add_sound("du bist", r"^du bist\W?$", "sound/funnysounds/dubist.ogg")
add_sound("dumb ways", r"^dumb ways\W?$", "sound/funnysounds/dumbways.ogg")    # works	elif _re_['dumbways'].match(msg).play_sound("sound/funnysounds/dumbways.ogg")
add_sound("education", r"^education\W?$", "sound/funnysounds/education.ogg")   # does NOT work	elif _re_['education'].match(msg).play_sound("sound/funnysounds/education.ogg")
add_sound("einschrei", r"^einschrei\W?$", "sound/funnysounds/einschrei.ogg")
add_sound("electro", r"^electro\W?$", "sound/funnysounds/electro.ogg")
add_sound("elementary", r"^elementary\W?$", "sound/funnysounds/elementary.ogg")
add_sound("engel", r"^engel\W?$", "sound/funnysounds/engel.ogg")
add_sound("erstwenn", r"^erstwenn\W?$", "sound/funnysounds/erstwenn.ogg")
add_sound("exitlight", r"^exitlight\W?$", "sound/funnysounds/exitlight.ogg")
add_sound("faint", r"^faint\W?$", "sound/funnysounds/faint.ogg")
add_sound("fatality", r"^fatality\W?$", "sound/funnysounds/fatality.ogg")
add_sound("flesh wound", r"^flesh wound\W?$", "sound/funnysounds/fleshwound.ogg")
add_sound("for you", r"^for you\W?$", "sound/funnysounds/foryou.ogg")
add_sound("fucking burger", r"^fucking burger\W?$", "sound/funnysounds/fuckingburger.ogg")
add_sound("ganjaman", r"^ganjaman\W?$", "sound/funnysounds/ganjaman.ogg")
add_sound("gay", r"^gay\W?$", "sound/funnysounds/gay.ogg")
add_sound("get crowbar", r"^get crowbar\W?$", "sound/funnysounds/getcrowbar.ogg")
add_sound("ghostbusters", r"^ghostbusters\W?$", "sound/funnysounds/ghostbusters.ogg")
add_sound("girly", r"^girly\W?$", "sound/funnysounds/girly.ogg")
add_sound("goodby eandrea", r"^goodbye andrea\W?$", "sound/funnysounds/goodbyeandrea.ogg")
add_sound("goodbye sarah", r"^goodbye sarah\W?$", "sound/funnysounds/goodbyesarah.ogg")
add_sound("hammertime", r"^hammertime\W?$", "sound/funnysounds/hammertime.ogg")
add_sound("hellstestern", r"^hellstestern\W?$", "sound/funnysounds/hellstestern.ogg")
add_sound("holy", r"^holy\W?$", "sound/funnysounds/holy.ogg")
add_sound("hoppereiter", r"^hoppereiter\W?$", "sound/funnysounds/hoppereiter.ogg")
add_sound("hush", r"^hush\W?$", "sound/funnysounds/hush.ogg")
add_sound("i cant believe", r"^i can'?t believe\W?$", "sound/funnysounds/icantbelieve.ogg")
add_sound("ichtuedieweh", r"^ichtuedieweh\W?$", "sound/funnysounds/ichtuedieweh.ogg")
add_sound("i do parkour", r"^i do parkour\W?$", "sound/funnysounds/idoparkour.ogg")
add_sound("i hate all", r"^i hate all\W?$", "sound/funnysounds/ihateall.ogg")
add_sound("imperial", r"^imperial\W?$", "sound/funnysounds/imperial.ogg")
add_sound("im your father", r"^i'?m your father\W?$", "sound/funnysounds/imyourfather.ogg")
add_sound("indiana jones", r"^indiana jones\W?$", "sound/funnysounds/indianajones.ogg")
add_sound("in your head zombie", r"^in your head zombie\W?$", "sound/funnysounds/inyourheadzombie.ogg")
add_sound("i see dead people", r"^i see dead people\W?$", "sound/funnysounds/iseedeadpeople.ogg")
add_sound("its my life", r"^it'?s my life\W?$", "sound/funnysounds/itsmylife.ogg")
add_sound("its not", r"^it'?s not\W?$", "sound/funnysounds/itsnot.ogg")
add_sound("jesus", r"^jesus\W?$", "sound/funnysounds/jesus.ogg")
add_sound("johncena", r"^johncena\W?$", "sound/funnysounds/johncena.ogg")
add_sound("kamehameha", r"^kamehameha\W?$", "sound/funnysounds/kamehameha.ogg")
add_sound("keep your shirt on", r"^keep your shirt on\W?$", "sound/funnysounds/keepyourshirton.ogg")
add_sound("kommtdiesonne", r"^kommtdiesonne\W?$", "sound/funnysounds/kommtdiesonne.ogg")
add_sound("kungfu", r"^kungfu\W?$", "sound/funnysounds/kungfu.ogg")
add_sound("lately", r"^lately\W?$", "sound/funnysounds/lately.ogg")
add_sound("lets get ready", r"^lets get ready\W?$", "sound/funnysounds/letsgetready.ogg")
add_sound("lets put a smile", r"^lets put a smile\W?$", "sound/funnysounds/letsputasmile.ogg")
add_sound("lights out", r"^lights out\W?$", "sound/funnysounds/lightsout.ogg")
add_sound("live to win", r"^live to win\W?$", "sound/funnysounds/livetowin.ogg")
add_sound("loveme", r"^loveme\W?$", "sound/funnysounds/loveme.ogg")
add_sound("low", r"^low\W?$", "sound/funnysounds/low.ogg")
add_sound("luck", r"^luck\W?$", "sound/funnysounds/luck.ogg")
add_sound("lust", r"^lust\W?$", "sound/funnysounds/lust.ogg")
add_sound("meinland", r"^meinland\W?$", "sound/funnysounds/meinland.ogg")
add_sound("message", r"^message\W?$", "sound/funnysounds/message.ogg")
add_sound("mission", r"^mission\W?$", "sound/funnysounds/mission.ogg")
add_sound("mortal kombat", r"^mortal kombat\W?$", "sound/funnysounds/mortalkombat.ogg")
add_sound("move ass", r"^move ass\W?$", "sound/funnysounds/moveass.ogg")
add_sound("muppet opening", r"^muppet opening\W?$", "sound/funnysounds/muppetopening.ogg")
add_sound("my little pony", r"^my little pony\W?$", "sound/funnysounds/mylittlepony.ogg")
add_sound("never seen", r"^never seen\W?$", "sound/funnysounds/neverseen.ogg")
add_sound("nightmare", r"^nightmare\W?$", "sound/funnysounds/nightmare.ogg")
add_sound("nobody likes you", r"^nobody likes you\W?$", "sound/funnysounds/nobodylikesyou.ogg")
add_sound("nonie", r"^nonie\W?$", "sound/funnysounds/nonie.ogg")
add_sound("nooo", r"^nooo\W?$", "sound/funnysounds/nooo.ogg")
add_sound("numanuma", r"^numanuma\W?$", "sound/funnysounds/numanuma.ogg")
add_sound("nyancat", r"^nyancat\W?$", "sound/funnysounds/nyancat.ogg")
add_sound("o fuck", r"^o fuck\W?$", "sound/funnysounds/ofuck.ogg")
add_sound("oh my god", r"^oh my god\W?$", "sound/funnysounds/ohmygod.ogg")
add_sound("ohnedich", r"^ohnedich\W?$", "sound/funnysounds/ohnedich.ogg")
add_sound("oh no", r"^oh no\W?$", "sound/funnysounds/ohno.ogg")
add_sound("oh noe", r"^oh noe\W?$", "sound/funnysounds/ohnoe.ogg")
add_sound("pacman", r"^pacman\W?$", "sound/funnysounds/pacman.ogg")
add_sound("pick me up", r"^pick me up\W?$", "sound/funnysounds/pickmeup.ogg")
add_sound("pikachu", r"^pikachu\W?$", "sound/funnysounds/pikachu.ogg")
add_sound("pinkiepie", r"^pinkiepie\W?$", "sound/funnysounds/pinkiepie.ogg")
add_sound("pipe", r"^pipe\W?$", "sound/funnysounds/pipe.ogg")
add_sound("piss me off", r"^piss me off\W?$", "sound/funnysounds/pissmeoff.ogg")
add_sound("play a game", r"^play a game\W?$", "sound/funnysounds/playagame.ogg")
add_sound("pooping", r"^pooping\W?$", "sound/funnysounds/pooping.ogg")
add_sound("powerpuff", r"^powerpuff\W?$", "sound/funnysounds/powerpuff.ogg")
add_sound("radioactive", r"^radioactive\W?$", "sound/funnysounds/radioactive.ogg")
add_sound("rammsteinriff", r"^rammsteinriff\W?$", "sound/funnysounds/rammsteinriff.ogg")
add_sound("redwins", r"^redwins\W?$", "sound/funnysounds/redwins.ogg")
add_sound("renegade", r"^renegade\W?$", "sound/funnysounds/renegade.ogg")
add_sound("retard", r"^retard\W?$", "sound/funnysounds/retard.ogg")
add_sound("rockyouguitar", r"^rockyouguitar\W?$", "sound/funnysounds/rockyouguitar.ogg")
add_sound("sail", r"^sail\W?$", "sound/funnysounds/sail.ogg")
add_sound("sandstorm", r"^sandstorm\W?$", "sound/funnysounds/sandstorm.ogg")
add_sound("saymyname", r"^saymyname\W?$", "sound/funnysounds/saymyname.ogg")
add_sound("sellyouall", r"^sellyouall\W?$", "sound/funnysounds/sellyouall.ogg")
add_sound("senseofhumor", r"^senseofhumor\W?$", "sound/funnysounds/senseofhumor.ogg")
add_sound("shakesenora", r"^shakesenora\W?$", "sound/funnysounds/shakesenora.ogg")
add_sound("shut the fuckup", r"^shut the fuck up\W?$", "sound/funnysounds/shutthefuckup.ogg")
add_sound("shut your fucking mouth", r"^shut your fucking mouth\W?$", "sound/funnysounds/shutyourfuckingmouth.ogg")
add_sound("smooth criminal", r"^smooth criminal\W?$", "sound/funnysounds/smoothcriminal.ogg")
add_sound("socobatevira", r"^socobatevira\W?$", "sound/funnysounds/socobatevira.ogg")
add_sound("ssocobatevira end", r"^socobatevira end\W?$", "sound/funnysounds/socobateviraend.ogg")
add_sound("socobatevira fast", r"^socobatevira fast\W?$", "sound/funnysounds/socobatevirafast.ogg")
add_sound("socobatevira slow", r"^socobatevira slow\W?$", "sound/funnysounds/socobateviraslow.ogg")
add_sound("sogivemereason", r"^sogivemereason\W?$", "sound/funnysounds/sogivemereason.ogg")
add_sound("so stupid", r"^so stupid\W?$", "sound/funnysounds/sostupid.ogg")
add_sound("space unicorn", r"^space unicorn\W?$", "sound/funnysounds/spaceunicorn.ogg")
add_sound("spierdalaj", r"^spierdalaj\W?$", "sound/funnysounds/spierdalaj.ogg")
add_sound("stamp on", r"^stamp on\W?$", "sound/funnysounds/stampon.ogg")
add_sound("star wars", r"^star wars\W?$", "sound/funnysounds/starwars.ogg")
add_sound("stoning", r"^stoning\W?$", "sound/funnysounds/stoning.ogg")
add_sound("story", r"^story\W?$", "sound/funnysounds/story.ogg")
add_sound("swedish chef", r"^swedish chef\W?$", "sound/funnysounds/swedishchef.ogg")
add_sound("sweet dreams", r"^sweet dreams\W?$", "sound/funnysounds/sweetdreams.ogg")
add_sound("take me down", r"^take me down\W?$", "sound/funnysounds/takemedown.ogg")
add_sound("talk scotish", r"^talk scotish\W?$", "sound/funnysounds/talkscotish.ogg")
add_sound("technology", r"^technology\W?$", "sound/funnysounds/technology.ogg")
add_sound("thunderstruck", r"^thunderstruck\W?$", "sound/funnysounds/thunderstruck.ogg")
add_sound("to church", r"^to church\W?$", "sound/funnysounds/tochurch.ogg")
add_sound("tsunami", r"^tsunami\W?$", "sound/funnysounds/tsunami.ogg")
add_sound("unbelievable", r"^unbelievable\W?$", "sound/funnysounds/unbelievable.ogg")
add_sound("undderhaifisch", r"^undderhaifisch\W?$", "sound/funnysounds/undderhaifisch.ogg")
add_sound("up town girl", r"^up town girl\W?$", "sound/funnysounds/uptowngirl.ogg")
add_sound("valkyries", r"^valkyries\W?$", "sound/funnysounds/valkyries.ogg")
add_sound("wahwahwah", r"^wahwahwah\W?$", "sound/funnysounds/wahwahwah.ogg")
add_sound("want you", r"^want you\W?$", "sound/funnysounds/wantyou.ogg")
add_sound("wazzup", r"^wazzup\W?$", "sound/funnysounds/wazzup.ogg")
add_sound("wehmirohweh", r"^wehmirohweh\W?$", "sound/funnysounds/wehmirohweh.ogg")
add_sound("when angels", r"^when angels\W?$", "sound/funnysounds/whenangels.ogg")
add_sound("where are you", r"^where are you\W?$", "sound/funnysounds/whereareyou.ogg")
add_sound("whistle", r"^whistle\W?$", "sound/funnysounds/whistle.ogg")
add_sound("wimbaway", r"^wimbaway\W?$", "sound/funnysounds/wimbaway.ogg")
add_sound("windows", r"^windows\W?$", "sound/funnysounds/windows.ogg")
add_sound("would you like", r"^would you like\W?$", "sound/funnysounds/wouldyoulike.ogg")
add_sound("wtf", r"^wtf\W?$", "sound/funnysounds/wtf.ogg")
add_sound("yeee", r"^yeee\W?$", "sound/funnysounds/yeee.ogg")
add_sound("yesmaster", r"^yes master\W?$", "sound/funnysounds/yesmaster.ogg")
add_sound("holy shit", r"^holy shit\W?$", "sound/vo_female/holy_shit")
add_sound("impressive", r"^impressive\W?$", "sound/vo_female/impressive1.wav")
add_sound("excellent", r"^excellent\W?$", "sound/vo_evil/excellent1.wav")
add_sound("all skeet skeet", r"^all skeet skeet\W?$", "sound/funnysounds/allskeetskeet.ogg")
add_sound("bad boys", r"^bad boys\W?$", "sound/funnysounds/badboys.ogg")
add_sound("banana boat song", r"^banana boat song\W?$", "sound/funnysounds/bananaboatsong.ogg")
add_sound("come with me now", r"^come with me now\W?$", "sound/funnysounds/comewithmenow.ogg")
add_sound("danger zone", r"^danger zone\W?$", "sound/funnysounds/dangerzone.ogg")
add_sound("eat pussy", r"^eat pussy\W?$", "sound/funnysounds/eatpussy.ogg")
add_sound("eins zwei", r"^eins zwei\W?$", "sound/funnysounds/einszwei.ogg")
add_sound("feel good", r"^feel good\W?$", "sound/funnysounds/feelgood.ogg")
add_sound("jesus oh", r"^jesus oh\W?$", "sound/funnysounds/jesusoh.ogg")
add_sound("knocked down", r"^knocked down\W?$", "sound/funnysounds/knockeddown.ogg")
add_sound("legitness", r"^legitness\W?$", "sound/funnysounds/legitness.ogg")
add_sound("me", r"^me\W?$", "sound/funnysounds/me.ogg")
add_sound("oh my gosh", r"^oh my gosh\W?$", "sound/funnysounds/ohmygosh.ogg")
add_sound("pink panther", r"^pink panther\W?$", "sound/funnysounds/pinkpanther.ogg")
add_sound("salil", r"^salil\W?$", "sound/funnysounds/salil.ogg")
add_sound("space jam", r"^space jam\W?$", "sound/funnysounds/spacejam.ogg")
add_sound("stop", r"^stop\W?$", "sound/funnysounds/stop.ogg")
add_sound("will be singing", r"^will be singing\W?$", "sound/funnysounds/willbesinging.ogg")
add_sound("you", r"^you\W?$", "sound/funnysounds/you.ogg")


class funnysounds(minqlx.Plugin):
    database = Redis

    def __init__(self):
        super().__init__()
        self.add_hook("chat", self.handle_chat)
        self.add_command("cookies", self.cmd_cookies)
        self.last_sound = None
        self.add_command(("soundlist", "slist"), self.cmd_soundlist, client_cmd_perm=0, usage="<pagenum>")
        self.set_cvar_once("qlx_funSoundDelay", "3")


    def cmd_soundlist(self, player, msg, channel):
        """Prints a page of the sound list"""
        page = 0
        linesPerPage = 20
        totalpages = -(-len(_re_) // linesPerPage) -1  #ceil division trick to get pages for 10 items per page, -1 as 0= first.

        if len(msg) < 2:
            return minqlx.RET_USAGE

        if len(msg) > 1:
            try:
                page = int(msg[1])

            except ValueError:
                player.tell("Invalid page number.")
                return minqlx.RET_STOP_ALL

        page = page - 1
        if page > totalpages:
            page = totalpages
        if page < 1:
            page = 0
        player.tell("^5Sound list - page {} of {}".format(page + 1, totalpages + 1))
        for key in sorted(_re_)[page * linesPerPage:page * linesPerPage + linesPerPage]:  # slice for pagination
            player.tell("   ^2{}".format(key))

    def handle_chat(self, player, msg, channel):
        if channel != "chat":
            return

        msg = self.clean_text(msg)
        for key in _re_:
        	if _re_[key][0].match(msg):
        		self.play_sound(_re_[key][1])

    def play_sound(self, path):
        if not self.last_sound:
            pass
        elif time.time() - self.last_sound < self.get_cvar("qlx_funSoundDelay", int):
            return

        self.last_sound = time.time()
        for p in self.players():
            if self.db.get_flag(p, "essentials:sounds_enabled", default=True):
                super().play_sound(path, p)

    def cmd_cookies(self, player, msg, channel):
        x = random.randint(0, 100)
        if not x:
            channel.reply("^6? ^7Here you go, {}. I baked these just for you! ^6?".format(player))
        elif x == 1:
            channel.reply("What, you thought ^6you^7 would get cookies from me, {}? Hah, think again.".format(player))
        elif x < 50:
            channel.reply("For me? Thank you, {}!".format(player))
        else:
            channel.reply("I'm out of cookies right now, {}. Sorry!".format(player))
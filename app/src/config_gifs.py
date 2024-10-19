from typing import Dict

sailor_gifs = {
    "MOON": "https://media.giphy.com/media/26gBjmGEsrFQlj8g8/giphy.gif",
    "MERCURY": "https://media.giphy.com/media/CW0RoZIy3qiWc/source.gif",
    "MARS": "https://media.giphy.com/media/13IjmDjuI66Xi8/source.gif",
    "JUPITER": "https://media.giphy.com/media/mRhBJaXw74gb6/source.gif",
    "VENUS": "https://media.giphy.com/media/13RgZe9wmCgTv2/source.gif",
    "PLUTO": "https://media.giphy.com/media/11zpB5vBNwleIE/source.gif",
    "URANUS": "https://media.giphy.com/media/6KOXxR2nhRIIw/source.gif",
    "NEPTUNE": "https://media.giphy.com/media/ScwSlGdFoZksM/source.gif",
    "SATURN": "https://tenor.com/view/sailor-saturn-anime-spin-turn-around-gif-16581754",
    "CHIBI": "https://media.giphy.com/media/Rl6TvAg4JAWAM/source.gif"
}

thor_gifs = {
    "RAGNAROK": "https://media.giphy.com/media/l4FGni1RBAR2OWsGk/source.mp4",
    "BRO": "https://tenor.com/view/fat-thor-avengers-funny-chris-hemsworth-gif-14558486",
    "CACHAS": "https://tenor.com/view/thor-naked-ragnarok-chris-hemsworth-gif-11202908"
}

mob_psycho_gifs = {
    "REIGEN": "https://tenor.com/view/mob-psycho-reigen-gif-6090446",
    "MOB": "https://media.giphy.com/media/xUNda7dFmFjGmOpVv2/source.mp4"
}

goblin_slayer_gifs = {
    "YEAH": "https://tenor.com/view/goblinslayer-yeah-yes-gif-14523030",
    "ELF": "https://tenor.com/view/goblinslayer-drinking-angry-gif-14523029",
    "SMILE": "https://tenor.com/view/goblinslayer-gif-14523027",
    "BADASS": "https://tenor.com/view/badass-goblin-slayer-anime-gif-13056346",
    "PRIEST": "https://tenor.com/view/goblin-slayer-stressed-priestess-anime-you-get-used-to-it-gif-13752108",
    "THINK": "https://tenor.com/view/think-goblin-slayer-anime-gif-13070906"
}


def get(model: str) -> Dict:
    return globals()[model]


def items():
    return ["sailor_gifs", "thor_gifs", "mob_psycho_gifs", "goblin_slayer_gifs"]

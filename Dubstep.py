import re


def song_decoder(song):
    return re.sub('\s+', ' ', song.replace("WUB", " ")).strip()

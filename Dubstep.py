# https://www.codewars.com/kata/551dc350bf4e526099000ae5
def song_decoder(song):
    import re
    return re.sub('\s+', ' ', song.replace("WUB", " ")).strip()


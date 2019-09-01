def format_duration(seconds):
    if not seconds:
        return 'now'
    quotients = []
    dividers = (31536000, 86400, 3600, 60, 1)
    for divider in dividers:
        quotient, modulo = divmod(seconds, divider)
        quotients.append(quotient)
        seconds = modulo
    words = ['year', 'day', 'hour', 'minute', 'second']
    string_parts = list(filter(lambda part: int(part[0]), [
     '{} {}'.format(str(quotient), word) for quotient, word in zip(
        quotients, map(lambda word: '{}s'.format(word) if quotients[
            words.index(word)] > 1 else word, words))]))
    return '''{}{}{}'''.format(
        ", ".join(string_parts[:-1]), " and " if len(string_parts) > 1 else "", string_parts[-1])

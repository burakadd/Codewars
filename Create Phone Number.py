# https://www.codewars.com/kata/525f50e3b73515a6db000b83


def create_phone_number(n):
    string_number = "".join(map(str, n))
    return '({}{}{}) {}{}{}-{}{}{}'.format(*string_number)

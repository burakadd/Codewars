# https://www.codewars.com/kata/59df2f8f08c6cec835000012

def meeting(s):
    import re
    splitted = re.split('[:;]', s.upper())
    return "".join(sorted(['({}, {})'.format(splitted[i + 1], j) for i, j in enumerate(splitted) if not i % 2]))

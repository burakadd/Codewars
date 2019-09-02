# https://www.codewars.com/kata/550498447451fbbd7600041c


def comp(array1, array2):
    return sorted(array2) == list(map(lambda i: pow(i, 2), sorted(array1))) if all(
        array is not None for array in (array1, array2)) else False

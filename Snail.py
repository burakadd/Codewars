# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1


def snail(array):
    snail_array = []
    while True:
        for number in array.pop(0):
            snail_array.append(number)
        if not array:
            return snail_array
        for _list in array[:-1]:
            snail_array.append(_list.pop(-1))
        for number in array.pop(-1)[::-1]:
            snail_array.append(number)
        if not array:
            return snail_array
        for _list in array[-1::-1]:
            snail_array.append(_list.pop(0))

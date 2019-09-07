# https://www.codewars.com/kata/523a86aa4230ebb5420001e1


def anagrams(word, words):
    return [i for i in words if sorted(word) == sorted(i)]

# -*- coding: utf-8 -*-
import regex


def words(string):
    string = regex.findall(r'[\p{L}\w!&@$%^&?]+|[.,;:]', string)
    for i in range(len(string)):
        try:
            if isinstance(int(string[i]), int):
                string[i] = int(string[i])
        except Exception:
            pass
    howmany = {}
    for s in string:
        if s not in howmany:
            howmany[s] = 1
        else:
            howmany[s] += 1
    return howmany


# print words('¡Hola! ¿Qué tal? Привет!')

# -*- coding: utf-8 -*-
import re


def rus_to_unikod(matchobj):
    word = matchobj.group(0)
    res = ''
    for letter in unicode(word,"utf-8"):
        digit = str(hex(ord(letter)))
        res += re.sub("x", "", digit).upper()
    return "\X2\\" + res + "\X0\\"


pattern = r'[а-яА-ЯЁё]{1,}'
editor.rereplace(pattern, rus_to_unikod)

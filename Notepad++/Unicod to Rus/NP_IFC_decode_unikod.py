# -*- coding: utf-8 -*-
import re


def unikod_to_rus(matchobj):
    letters = re.findall(r"\w{4}", matchobj.group(1))
    res = ''
    for letter in letters:
        res += unichr(int(letter, base=16))
    return res.encode('utf8')


pattern = r'\\X2\\(\w{4,})\\X0\\'
editor.rereplace(pattern, unikod_to_rus)

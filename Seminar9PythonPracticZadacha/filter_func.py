#!/usr/bin/env python
# -*- coding: utf-8 -*-

def filter(text):
    filt = "абв"
    split_text = str(text).split()
    print(split_text)
    try:
        for i in range(len(split_text)[1:]-1):
            if filt in split_text[i]:
                split_text.pop(i)
    except IndexError:
        pass

    text = " ".join(split_text)
    print(text)
    return text

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, datetime as dt

def filter(text):
    filt = "абв"
    split_text = str(text).split()
    try:
        for i in range(len(split_text)-1):
            if filt in split_text[i]:
                split_text.pop(i)
    except IndexError:
        pass

    text = " ".join(split_text)
    return text


def filter_text(text):
    text = filter(text)
    save_print_show_text(text)
    return text

def save_print_show_text(text):
    f = open("log.txt", 'a+')
    f.write(f"{dt.datetime.now()}	\n{text}\n")
    f.close()
    print(text)
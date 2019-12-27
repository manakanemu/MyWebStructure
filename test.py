#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import wraps

def getmapping(path):
    print(path)
    def decorator(fun):
        def wrap(text):
            print('wrap'+text)
            fun(text)
        return wrap
    return decorator

@getmapping('lujing')
def hello(request):
    print(request)


# hello = getmapping(hello)
hello('beijing')
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import wraps


def getMapping(path):
    def decorator(func):
        @wraps(func)
        def wrapper(request):
            result = None
            if request['REQUEST_METHOD'] == 'GET':
                request_path = request['PATH_INFO']
                if path == request_path:
                    result = func(request)
            return result
        return wrapper
    return decorator

def postMapping(path):
    def decorator(func):
        @wraps(func)
        def wrapper(request):
            result = None
            if request['REQUEST_METHOD'] == 'POST':
                if path == request['PATH_INFO']:
                    result = func(request)
            return result
        return wrapper
    return decorator

def requestMapping(path):
    def decorator(func):
        @wraps(func)
        def wrapper(request):
            result = None
            if path == request['PATH_INFO']:
                result = func(request)
            return result
        return wrapper
    return decorator

def render(filePath):
    realPath = 'statics/'+filePath
    try:
        with open(realPath,'r') as file:
            return file.read()
    except:
        print('{} is not exist'.format(filePath))
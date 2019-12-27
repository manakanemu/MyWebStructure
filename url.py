#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from method import getMapping
from method import render


@getMapping('/a')
def welcompage(request):
    print('welcome function and path a')
    return 'this is welcome page'

@getMapping('/b')
def login(request):
    print('login function and path b')
    return 'this is login page'

@getMapping('/')
def index(request):
    return render('index.html')




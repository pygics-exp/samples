# -*- coding: utf-8 -*-
'''
Created on 2017. 10. 25.
@author: HyechurnJang
'''

from page import *
from page import W3

Page().header('Page Module Path')

Page('/abs').header('Page Absolute Path')

Page('rel').header('Page Relation Path')

import subpath

test_page = Page('/', cache=False)
test_page.header(
    W3.Div().html(
        W3.H(2).html('Header Section')
    )
)
test_page.footer(
    W3.Div().html(
        W3.H(2).html('Footer Section')
    )
)

@test_page.init
def page_init(req, *argv, **kargs):
    return W3.Div().html(
        W3.H(1).html('Test Page'),
    )

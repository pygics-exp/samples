# -*- coding: utf-8 -*-
'''
Created on 2017. 10. 25.
@author: HyechurnJang
'''

from page import *
from page.w3 import *

Page().header('Page Module Path')

Page('/abs').header('Page Absolute Path')

Page('rel').header('Page Relation Path')

import subpath

test_page = Page('/', cache=False)
test_page.header(
    Div().html(
        H(2).html('Header Section')
    )
)
test_page.footer(
    Div().html(
        H(2).html('Footer Section')
    )
)

@test_page.init
def page_init(req, *argv, **kargs):
    return Div().html(
        H(1).html('Test Page'),
    )

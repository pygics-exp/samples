# -*- coding: utf-8 -*-
'''
Created on 2017. 10. 25.
@author: HyechurnJang
'''

from page import Page, W3
from dashboard import Dashboard

dashboard = Dashboard(Page())

@dashboard.init('TEST INIT ICON')
def dashboard_init(req, *argv, **kargs):
    return W3.Div().html(
        W3.H(1).html('Test Dashboard'),
        W3.H(2).html('asdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdf'),
        W3.H(2).html('asdf'),
        W3.H(2).html('asdf'),
        W3.H(2).html('asdf'),
        W3.H(2).html('asdf'),
        W3.H(2).html('asdf'),
        W3.H(2).html('asdf'),
        W3.H(2).html('asdf'),
        W3.H(2).html('asdf'),
        W3.H(2).html('asdf'),
        W3.H(2).html('asdf'),
        W3.H(2).html('asdf'),
        W3.H(2).html('asdf'),
        W3.H(2).html('asdf'),
        W3.H(2).html('asdf'),
        W3.H(2).html('asdf'),
        W3.H(2).html('asdf'),
        W3.H(2).html('asdf'),
        W3.H(2).html('asdf'),
        W3.H(2).html('asdf'),
        W3.H(2).html('asdf'),
        W3.H(2).html('asdf'),
        W3.H(2).html('asdf'),
        W3.H(2).html('asdf'),
        W3.H(2).html('asdf'),
        W3.H(2).html('asdf'),
        W3.H(2).html('asdf'),
        W3.H(2).html('asdf'),
        W3.H(2).html('asdf'),
        W3.H(2).html('asdf'),
        W3.H(2).html('asdf'),
        W3.H(2).html('asdf'),
        W3.H(2).html('asdf'),
    )

@dashboard.menu('MENU NAV', 'TEST MENU ICON')
def dashboard_menu(req, *argv, **kargs):
    return W3.Div()
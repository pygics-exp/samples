# -*- coding: utf-8 -*-
'''
Created on 2017. 10. 25.
@author: HyechurnJang
'''

from dashboard import *

dashboard = Dashboard('/')
show = dashboard.category('Show', 'Show Icon')
analyze = dashboard.category('Analyze', 'Anal Icon')

@dashboard.menu(u'개요', 'Overview Icon')
def dashboard_overview(req, *argv, **kargs):
    return W3.Div() >> (
        W3.H(1) >> 'Overview Page',
        dashboard >> 'dashboard_overflow'
    )

@dashboard.menu('Status', 'Status Icon')
def dashboard_status(req, *argv, **kargs):
    return W3.Div() >> (
        W3.H(1) >> 'Status Page'
    )

@show
@dashboard.menu('Tenant', 'Tenant Icon')
def dashboard_tenant(req, *argv, **kargs):
    return W3.Div() >> (
        W3.H(1) >> 'Tenant Show Page'
    )

@show
@dashboard.menu('Device', 'Device Icon')
def dashboard_device(req, *argv, **kargs):
    return W3.Div() >> (
        W3.H(1) >> 'Device Show Page'
    )

@analyze
@dashboard.menu('EPG', 'EPG Icon')
def dashboard_epg(req, *argv, **kargs):
    return W3.Div() >> (
        W3.H(1) >> 'EPG Analyze Page'
    )

@analyze
@dashboard.menu('Endpoint', 'Endpoint Icon')
def dashboard_endpoint(req, *argv, **kargs):
    return W3.Div() >> (
        W3.H(1) >> 'Endpoint Analyze Page'
    )

@dashboard.menu('Setting', 'Setting Icon')
def dashboard_setting(req, *argv, **kargs):
    return W3.Div() >> (
        W3.H(1) >> 'Setting Page'
    )

@dashboard.view()
def dashboard_overflow(req, *argv, **kargs):
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
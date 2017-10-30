# -*- coding: utf-8 -*-
'''
Created on 2017. 10. 25.
@author: HyechurnJang
'''

from page import Page

Page().header('Page SubModule Path')

Page('/abs/subpath').header('Page SubModule Absolute Path')

Page('rel').header('Page SubModule Relation Path')

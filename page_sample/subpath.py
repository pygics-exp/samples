# -*- coding: utf-8 -*-
'''
Created on 2017. 10. 25.
@author: HyechurnJang
'''

from page import Page

Page().top('Subpath Page New Sample')

Page('/abs/subpath').top('Subpath Page Abstract Path')

Page('rel').top('Subpath Page Relation Path')

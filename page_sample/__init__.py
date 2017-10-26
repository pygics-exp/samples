# -*- coding: utf-8 -*-
'''
Created on 2017. 10. 25.
@author: HyechurnJang
'''

from page import *

Page().top('Page New Sample')

Page('/abs').top('Page Abstract Path')

Page('rel').top('Page Relation Path')

import subpath

p = Page('/', cache=False)

@main(p)
def page_main(req, *argv, **kargs):
    return DIV().html(
        HEAD(1).html('jang'),
        PARA().html('hyechurn')
    )


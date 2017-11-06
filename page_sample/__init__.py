# -*- coding: utf-8 -*-
'''
Created on 2017. 10. 25.
@author: HyechurnJang
'''

from page import *

#===============================================================================
# Path Sample
#===============================================================================
Page().header('Page Module Path')
Page('/abs').header('Page Absolute Path')
Page('rel').header('Page Relation Path')

import subpath

#===============================================================================
# Page Sample
#===============================================================================

class MyPage(Page):
    
    def __init__(self):
        Page.__init__(self, '/', 'MyPage', cache=False)
        self.count = 0

my_page = MyPage()
my_page.header(
    W3.Div().html(
        W3.H(1).html('Header Section')
    )
)
my_page.footer(
    W3.Div().html(
        W3.H(2).html('Footer Section')
    )
)

@my_page.init
def page_sample_init(req, *argv, **kargs):
    return W3.Div().html(
        W3.H(1).html('Init Section'),
        my_page.patch('page_sample_view_l1'),
        my_page.patch('page_sample_count'),
        my_page.patch('page_sample_post'),
        my_page.patch('page_sample_delete'),
    )

@my_page.view
def page_sample_count(req, *argv, **kargs):
    my_get = my_page.get('page_sample_count')
    my_page.count += 1
    return W3.Div().html(
        W3.H(1).html('Count : %d' % my_page.count),
        W3.Button(Text='text').opts(my_get.Send).html('Add'),
        my_get
    )

@my_page.view
def page_sample_post(req, *argv, **kargs):
    my_post = my_page.post('page_sample_post')
    
    if req.data:
        ph_username = req.data['username']
        ph_password = req.data['password']
    else:
        ph_username = ''
        ph_password = ''
    
    return W3.Div().html(
        W3.H(1).html('Post Section'),
        W3.Input(Type='text', Name='username', PlaceHolder=ph_username).opts(my_post.Data),
        W3.Input(Type='text', Name='password', PlaceHolder=ph_password).opts(my_post.Data),
        W3.Button(Text='text').opts(my_post.Send).html('Submit'),
        my_post,
        my_page.reload('page_sample_count'),
    )

@my_page.view
def page_sample_delete(req, *argv, **kargs):
    my_del = my_page.delete('page_sample_delete')
    return W3.Div().html(
        W3.H(1).html('Deleting'),
        W3.Button(Text='text').opts(my_del.Send).html('Delete'),
        my_del,
        my_page.reload('page_sample_count'),
    )

@my_page.view
def page_sample_view_l1(req, *argv, **kargs):
    return W3.Div(Class='page_sample_view_l1').html(
        W3.H(2).html('Sample View L1'),
        my_page.patch('page_sample_view_l2')
    )
    
@my_page.view
def page_sample_view_l2(req, *argv, **kargs):
    return W3.Div(Class='page_sample_view_l2').html(
        W3.H(4).html('Sample View L2'),
        my_page.reload('page_sample_count')
    )

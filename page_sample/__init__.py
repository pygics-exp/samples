# -*- coding: utf-8 -*-
'''
Created on 2017. 10. 25.
@author: HyechurnJang
'''

from page import *

class MyPage(Page):
    
    def __init__(self):
        Page.__init__(self, '/', 'MyPage', cache=True)
        self.count = 0

my_page = MyPage()

my_page.header(
    W3.Div() >> (
        W3.H(1) >> '######### Header Section #########',
        W3.P() >> u'헤더 섹션 유니코드'
    )
)
my_page.footer(
    W3.Div() >> (
        W3.H(1) >> '######### Footer Section #########',
        W3.P() >> u'푸터 섹션 유니코드'
    )
)

@my_page.init()
def page_sample_init(req, *argv, **kargs):
    return W3.Div() >> (
        W3.H(1) >> '######### Init Section #########',
        my_page('page_sample_count'),
        my_page('page_sample_post'),
        my_page('page_sample_delete'),
    )

@my_page.view()
def page_sample_count(req, *argv, **kargs):
    if req.method == 'DELETE': my_page.count -= 1
    else: my_page.count += 1
    my_get = my_page.get('page_sample_count')
    return W3.Div() >> (
        W3.H(3) >> 'Get Interactive Section',
        W3.H(5) >> u'카운트 = %d' % my_page.count,
        W3.Button() << my_get.event() >> 'Add',
        my_get
    )

@my_page.view()
def page_sample_post(req, *argv, **kargs):
    if req.data:
        ph_username = req.data['username']
        ph_password = req.data['password']
    else:
        ph_username = ''
        ph_password = ''
        
    my_post = my_page.post('page_sample_post')
    return W3.Div() >> (
        W3.H(3) >> 'Post Interactive Section',
        W3.Input(Type='text', Name='username', PlaceHolder=ph_username) << my_post.data(),
        W3.Input(Type='password', Name='password', PlaceHolder=ph_password) << my_post.data(),
        W3.Button() << my_post.event() >> 'Submit',
        my_page['page_sample_count'],
        my_post,
    )

@my_page.view()
def page_sample_delete(req, *argv, **kargs):
    my_del = my_page.delete('page_sample_count')
    return W3.Div() >> (
        W3.H(3) >> 'Delete Interactive Section',
        W3.Button() << my_del.event() >> 'Delete',
        my_del,
    )

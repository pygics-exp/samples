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
        DataTable.setup(self)
        self.count = 0

my_page = MyPage()
my_page.header(
    W3.Div() >> (
        W3.H(1) >> 'Header Section'
    )
)
my_page.footer(
    W3.Div() >> (
        W3.H(2) >> 'Footer Section'
    )
)

@my_page.init()
def page_sample_init(req, *argv, **kargs):
    return W3.Div() >> (
        W3.H(1) >> 'Init Section',
        my_page >> ('page_sample_view_l1', 'testarg'),
        my_page >> 'page_sample_count',
        my_page >> 'page_sample_post',
        my_page >> 'page_sample_delete',
        my_page >> 'page_sample_tables',
    )

@my_page.view()
def page_sample_view_l1(req, *argv, **kargs):
    return W3.Div() >> (
        W3.H(2) >> 'Sample View L1',
        my_page >> 'page_sample_view_l2',
    )
    
@my_page.view()
def page_sample_view_l2(req, *argv, **kargs):
    return W3.Div() >> (
        W3.H(4) >> 'Sample View L2',
        my_page == ('page_sample_count', 'page_sample_post'),
    )

@my_page.view()
def page_sample_count(req, *argv, **kargs):
    my_get = my_page.get('page_sample_count')
    my_page.count += 1
    return W3.Div() >> (
        W3.H(1) >> 'Count : %d' % my_page.count,
        W3.Button() << my_get.event >> 'Add',
        my_get
    )

@my_page.view()
def page_sample_post(req, *argv, **kargs):
    my_post = my_page.post('page_sample_post')
    
    if req.data:
        ph_username = req.data['username']
        ph_password = req.data['password']
    else:
        ph_username = ''
        ph_password = ''
    
    return W3.Div() >> (
        W3.H(1) >> 'Post Section',
        W3.Input(Type='text', Name='username', PlaceHolder=ph_username) << my_post.data >> None,
        W3.Input(Type='password', Name='password', PlaceHolder=ph_password) << my_post.data >> None,
        W3.Button() << my_post.event >> 'Submit',
        my_page == 'page_sample_count',
        my_post,
    )

@my_page.view()
def page_sample_delete(req, *argv, **kargs):
    my_del = my_page.delete('page_sample_delete')
    return W3.Div() >> (
        W3.H(1) >> 'Deleting',
        W3.Button() << my_del.event >> 'Delete',
        my_page == 'page_sample_count',
        my_del,
    )

@my_page.view()
def page_sample_tables(req, *argv, **kargs):
    return W3.Div() >> (
        DataTable.Flush('ID', 'Name', 'Addr') << DataTable.Style.Compact << DataTable.Style.Border
            >> ('1', 'David', 'Seoul') >> ('2', 'Brooke', 'New-York') >> ('3', 'David', 'Seoul') >> ('4', 'Brooke', 'New-York')
            >> ('5', 'David', 'Seoul') >> ('6', 'Brooke', 'New-York') >> ('7', 'David', 'Seoul') >> ('8', 'Brooke', 'New-York')
            >> ('9', 'David', 'Seoul') >> ('10', 'Brooke', 'New-York') >> ('11', 'David', 'Seoul') >> ('12', 'Brooke', 'New-York')
            >> ('13', 'David', 'Seoul') >> ('14', 'Brooke', 'New-York') >> ('15', 'David', 'Seoul') >> ('16', 'Brooke', 'New-York'),
        DataTable.Sync('ID', 'Name', 'Addr') << my_page['page_sample_sync_table_data'],
    )

@my_page.view()
def page_sample_sync_table_data(req, *argv, **kargs):
    return DataTable.Data(
    ).record('1', 'David', 'Seoul'
    ).record('2', 'Brooke', 'New-York'
    ).record('3', 'David', 'Seoul'
    ).record('4', 'Brooke', 'New-York'
    ).record('5', 'David', 'Seoul'
    ).record('6', 'Brooke', 'New-York'
    ).record('7', 'David', 'Seoul'
    ).record('8', 'Brooke', 'New-York'
    ).record('9', 'David', 'Seoul'
    ).record('10', 'Brooke', 'New-York'
    ).record('11', 'David', 'Seoul'
    ).record('12', 'Brooke', 'New-York'
    ).record('13', 'David', 'Seoul'
    ).record('14', 'Brooke', 'New-York'
    ).record('15', 'David', 'Seoul'
    ).record('16', 'Brooke', 'New-York')


















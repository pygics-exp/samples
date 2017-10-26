# -*- coding: utf-8 -*-
'''
Created on 2017. 6. 1.
@author: HyechurnJang
'''

import pygics
from page import *
from extag import *

sample_page = PAGE(template=PAGE.TEMPLATE.SIMPLE)
sample_page.addJS('/page_sample/resource/js/page_sample_dev.js')
sample_page.addCSS('/page_sample/resource/css/page_sample_dev.css')
sample_page.addCategory('Sample Category', 'plus')

GRID.set(sample_page)

@PAGE.MAIN(sample_page, 'Sample Page')
def sample_page_main(req):
    return DIV().html(
        HEAD(1).html("Sample Page's Main"),
        PARA().html('This is Sample Main Page'),
        GRID.DESK(STYLE='background-color:#eee;width:47%;border:1px solid #333;float:left;').html(
            GRID.WIDGET(2, 2, auto=True, STYLE='background-color:red;').html('Jang'),
            GRID.WIDGET(2, 1, auto=True, STYLE='background-color:#aaa;').html('Hyechurn'),
            GRID.WIDGET(1, 2, auto=True, STYLE='background-color:green;').html('Husband')
        ),
        GRID.DESK(STYLE='background-color:#eee;width:47%;border:1px solid #333;float:right;').html(
            GRID.WIDGET(2, 2, auto=True, STYLE='background-color:red;').html('Noh'),
            GRID.WIDGET(2, 1, auto=True, STYLE='background-color:#aaa;').html('Eunyoung'),
            GRID.WIDGET(1, 2, auto=True, STYLE='background-color:green;').html('Wife')
        )
    )
    
@PAGE.MENU(sample_page, 'Sample Category::Sample Menu', 'dashboard')
def sample_page_menu(req, data='Init'):
    return DIV(CLASS='page-sample-dev').html(
        HEAD(1).html('Sample Menu'),
        NAV().html(
            NAV.TAB('patch').html(
                DIV(STYLE='margin:5px 0px;padding:5px;border:1px solid #00f;').html(
                    sample_page.patch('sample_page_patch', data), # Correct View Name
                    sample_page.patch('sample_page_patch', data),
                    sample_page.patch('sample_page_error'), # Unkown View Name
                )
            ),
            NAV.TAB('trigger & signal').html(
                DIV(STYLE='margin:5px 0px;padding:5px;border:1px solid #00f;').html(
                    HEAD(2).html('Trigger & Signal Test'),
                    sample_page.patch('sample_page_trigger'),
                    BUTTON.GROUP().html(
                        sample_page.trigger(
                            BUTTON(CLASS='btn-primary').html('Count'),
                            'sample_page_trigger',
                        ),
                        sample_page.signal(
                            BUTTON(CLASS='btn-danger').html('Zero'),
                            'GET', 'sample_page_trigger', '0',
                        )
                    )
                )
            ),
            NAV.TAB('context').html(
                DIV(STYLE='margin:5px 0px;padding:5px;border:1px solid #00f;').html(
                    HEAD(2).html('Context Test'),
                    sample_page.patch('sample_page_context'),
                )
            ),
            NAV.TAB('table').html(
                DIV(STYLE='margin:5px 0px;padding:5px;border:1px solid #00f;').html(
                    HEAD(2).html('Table Test'),
                    sample_page.table(
                        TABLE.SYNC('Name', 'Group', 'Status'),
                        'sample_page_table'
                    )
                )
            )
        )
    )

@PAGE.VIEW(sample_page)
def sample_page_patch(req, data):
    return HEAD(2).html('This is Sample Patch ' + data)

click_val = [0]
@PAGE.VIEW(sample_page)
def sample_page_trigger(req, val=None):
    if val != None:
        click_val[0] = int(val)
    else:
        click_val[0] += 1
    return 'Count : ' + str(click_val[0])

context = {'title' : '', 'name' : '', 'group' : ''}
@PAGE.VIEW(sample_page)
def sample_page_context(req):
    if req.method == 'POST':
        context['title'] = req.data['title']
        context['name'] = req.data['name']
        context['group'] = req.data['group']
    
    i_title = INPUT.TEXT('title', context['title'])
    i_name = INPUT.TEXT('name', context['name'])
    i_group = INPUT.TEXT('group', context['group'])
    
    return DIV().html(
        DIV().html(
            INPUT.GROUP().html(
                INPUT.LABEL_TOP('Title'),
                i_title
            ),
            INPUT.GROUP().html(
                INPUT.LABEL_LEFT('Name'),
                i_name,
                INPUT.LABEL_LEFT('Group'),
                i_group
            )
        ),
        sample_page.context(
            BUTTON(CLASS='btn-success').html('Submit'),
            'sample_page_context',
            i_title,
            i_name,
            i_group
        )
    )

@PAGE.TABLE(sample_page)
def sample_page_table(dtable):
    dtable.record('david', 'test', 'good')
    dtable.record('faul', 'test', 'bad')
    dtable.record('david', 'test', 'good')
    dtable.record('faul', 'test', 'bad')
    dtable.record('david', 'test', 'good')
    dtable.record('faul', 'test', 'bad')
    dtable.record('david', 'test', 'good')
    dtable.record('faul', 'test', 'bad')
    dtable.record('david', 'test', 'good')
    dtable.record('faul', 'test', 'bad')
    
    dtable.record('david', 'test', 'good')
    dtable.record('faul', 'test', 'bad')
    dtable.record('david', 'test', 'good')
    dtable.record('faul', 'test', 'bad')
    dtable.record('david', 'test', 'good')
    dtable.record('faul', 'test', 'bad')
    dtable.record('david', 'test', 'good')
    dtable.record('faul', 'test', 'bad')
    dtable.record('david', 'test', 'good')
    dtable.record('faul', 'test', 'bad')
    
    dtable.record('david', 'test', 'good')
    dtable.record('faul', 'test', 'bad')
    dtable.record('david', 'test', 'good')
    dtable.record('faul', 'test', 'bad')
    dtable.record('david', 'test', 'good')
    dtable.record('faul', 'test', 'bad')
    dtable.record('david', 'test', 'good')
    dtable.record('faul', 'test', 'bad')
    dtable.record('david', 'test', 'good')
    dtable.record('faul', 'test', 'bad')

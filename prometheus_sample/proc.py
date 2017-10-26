# -*- coding: utf-8 -*-
'''
Created on 2017. 5. 24.
@author: HyechurnJang
'''

import pygics
import prometheus

@prometheus.register
class TickGenerator(pygics.Task, prometheus.Generator):
    
    VENDOR = 'Prometheus'
    PRODUCT = 'Sample'
    TITLE = 'TickGenerator'
    VERSION = '0.1'
    INFO = 'simple tick message'
    DESC = 'generate simple tick message to prometheus every 1 sec'
    
    def __init__(self, name='TickGenerator'):
        pygics.Task.__init__(self, tick=1)
        prometheus.Generator.__init__(self, name)
    
    def OutputScheme(self, message): pass
    
    def create(self, message='from TickGenerator'):
        self.message = {'message' : message }
        self.start()
    
    def delete(self):
        self.stop()
        
    def run(self):
        print 'Do Trigger'
        self.trigger(self.message)

@prometheus.register
class Logger(prometheus.Actor):
    
    VENDOR = 'Prometheus'
    PRODUCT = 'Sample'
    TITLE = 'Logger'
    VERSION = '0.1'
    INFO = 'logging data'
    DESC = 'logging data'
    
    def __init__(self, name='Logger'):
        prometheus.Actor.__init__(self, name)
    
    def InputScheme(self, data): pass
    def OutputScheme(self, data): pass
    
    def process(self, data):
        print 'Logger : %s' % str(data)
        return data
        

@prometheus.register
class Printer(prometheus.Terminator):
    
    VENDOR = 'Prometheus'
    PRODUCT = 'Sample'
    TITLE = 'Printer'
    VERSION = '0.1'
    INFO = 'print data'
    DESC = 'print data'
    
    def __init__(self, name='Printer'):
        prometheus.Terminator.__init__(self, name)
    
    def InputScheme(self, data): pass
    
    def process(self, data):
        print 'Printer : %s' % str(data)
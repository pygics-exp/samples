# -*- coding: utf-8 -*-
'''
Created on 2017. 6. 8.
@author: HyechurnJang
'''

from sql import *

db = Sql(Memory())
# db = Sql(File())
# db = Sql(Mysql('localhost', 'root', 'password'))

@model(db)
class TestUser(Model):
    
    name = String(16)
    fullname = String(32)
    password = String(16)
    
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password
          
    def __repr__(self):
        return "TestUser('%s', '%s', '%s')" % (self.name, self.fullname, self.password)

@model(db)
class TestGroup(Model):
    
    name = String(24)
    desc = Text()
    
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
          
    def __repr__(self):
        return "TestGroup('%s', '%s')" % (self.name, self.desc)

print 'Init Data'
print 'Users ---------'
results = TestUser.list()
for r in results: print r
print ''
print 'Groups --------'
results = TestGroup.list()
for r in results: print r
print ''

#===============================================================================
# Insert
#===============================================================================
t1 = TestUser('what', 'tf', '1234').create()
t2 = TestUser('oh', 'mg', 'abcd').create()
t3 = TestUser('what', 'hty', 'qwer').create()
g = TestGroup('good', 'relation').create()

print 'Inserted Data'
print 'Users ---------'
results = TestUser.list()
for r in results: print r
print ''
print 'Groups --------'
results = TestGroup.list()
for r in results: print r
print ''

#===============================================================================
# Retrieve
#===============================================================================
print 'Select Data'
print 'Filter ---------'
for r in TestUser.list(TestUser.name=='what', TestUser.fullname.like('%t%')):
    print r
print ''
print 'Get ---------'
print TestUser.get(1)
print TestUser.get(0)
print ''
print 'One ---------'
print TestUser.one(TestUser.name=='what', TestUser.fullname=='tf')
print TestUser.one(TestUser.name=='what', TestUser.fullname=='tff')
print ''

#===============================================================================
# Update
#===============================================================================
t1.name = 'What!'
t1.update()

print 'Updated Data'
print 'Users ---------'
results = TestUser.list()
for r in results: print r
print ''
print 'Groups --------'
results = TestGroup.list()
for r in results: print r
print ''

#===============================================================================
# Delete
#===============================================================================
t1.delete()
t2.delete()
t3.delete()
g.delete()
  
print 'Deleted Data'
print 'Users ---------'
results = TestUser.list()
for r in results: print r
print ''
print 'Groups --------'
results = TestGroup.list()
for r in results: print r
print ''

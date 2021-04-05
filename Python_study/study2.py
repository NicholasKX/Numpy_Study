#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2021/4/5 11:34
@Author: Wu Kaixuan
@File  : study2.py
@Desc  :
"""
def init(data):
    '初始化'
    data['first']={}
    data['middle']={}
    data['last']={}
def lookup(data,label,name):
    return data[label].get(name)
def store(data,full_name):
    names = full_name.split()
    if len(names) == 2:
        names.insert(1,'')
    labels = 'first','middle','last'
    for label,name in zip(labels,names):
        people = lookup(data,label,name)
        if people:
            people.append(full_name)
        else:
            data[label][name]=[full_name]


Myname={}
init(Myname)
print(Myname)
store(Myname,'Wu Kai Xuan')
store(Myname,'Robin Hood')
store(Myname,'Robin Locksley')
# print(Myname)
print(lookup(Myname,'first','Robin'))

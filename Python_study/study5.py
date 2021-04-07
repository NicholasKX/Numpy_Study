#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2021/4/6 20:49
@Author: Wu Kaixuan
@File  : study5.py
@Desc  :
"""
class Filter:
    def init(self):
        self.blocked = []
    def filter(self,sequence):
        return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter):
    def init(self):
        self.blocked = ['SPAM']

# print(issubclass(SPAMFilter,Filter))
# print(issubclass(Filter,SPAMFilter))
print(SPAMFilter.__bases__)

s = SPAMFilter()
print(isinstance(s,SPAMFilter))
print(isinstance(s,Filter))

print(s.__class__) #要获悉对象属于哪个类，可使用属性__class__

class Calculator:
    def calculate(self,expression):
        self.value = eval(expression)
class Talker:
    def talk(self):
        print("Hi,my value is",self.value)
class TalkingCalculator(Calculator,Talker):
    pass
tc = TalkingCalculator()
tc.calculate('1+2*3')
tc.talk()
from abc import ABC, abstractmethod
class Talker(ABC):
    @abstractmethod
    def talk(self):
        pass
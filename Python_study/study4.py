#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2021/4/5 19:53
@Author: Wu Kaixuan
@File  : study4.py
@Desc  :
"""
class Person:
    '新建Person类'
    def set_name(self,name):
        self.name=name
    def get_name(self):
        return self.name
    def greet(self):
        print("Hello,World! I am {}.".format(self.name))
class Bird:
    song = 'Squaak'
    def sing(self):
        print(self.song)
class Secretive:
    '让方法或属性成为私有的（不能从外部访问）'
    def __inaccessible(self):
        print("Bet you cannot see me...")
    def accessible(self):
        print("The secret message is:")
        self.__inaccessible()

foo = Person()
bar = Person()
bird = Bird()
s = Secretive()
# s.__inaccessible() #让方法或属性成为私有的（不能从外部访问），只需让其名称以两个下划线打头即可。
s.accessible()
s._Secretive__inaccessible()#在类定义中，对所有以两个下划线打头的名称都进行转换，即在开头
#加上一个下划线和类名。只要知道这种幕后处理手法，就能从类外访问私有方法，然而不应这样做。
bird.sing()
birdsong = bird.sing #虽然这方法调用看起来很像函数调用，但变量 birdsong指向的是
# 关联的方法bird.sing，这意味着它也能够访问参数self（即它也被关联到类的实例）
birdsong()
# foo.set_name("Jack")
# bar.set_name("Mask")
# print(foo.get_name())
# print(bar.get_name())
# foo.greet()
# bar.greet()
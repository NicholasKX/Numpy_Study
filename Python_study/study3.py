#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2021/4/5 14:38
@Author: Wu Kaixuan
@File  : study3.py
@Desc  : 关键字参数和默认值,收集参数
"""
def parameters(*para):
    '多参数输入\
    参数前面的星号将提供的所有值都放在一个元组中，\
    也就是将这些值收集起来。'
    return para
def print_params_1(**para):
    '要收集关键字参数，可使用两个星号'
    print(para)
def print_params_2(x,y,z=3,*pospara,**keypara):
    '结合使用这些技术'
    print(x,y,z)
    print(pospara)
    print(keypara)


def multiplier(factor):
    '闭包'
    def multiplyByFactor(number):
        return number*factor
    return multiplyByFactor
double = multiplier(2)
print(type(double))
print(double(5))
print(multiplier(4)(5))
# print(parameters(1,2,3))
# print_params_1(x=1,y=2,z=3)
# print_params_2(1,2,3,5,6,7,foo=1,bar=2)
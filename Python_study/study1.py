#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2021/3/29 22:00
@Author: Wu Kaixuan
@File  : study1.py
@Desc  :
"""
from decimal import Decimal
# print("520")
# print(chr(0b100111001011000))
# print(ord('乘'))
# name = 'maria'
# age = 20
# # print(name)
# # print(id(name))
# # print(type(name))
# # print(Decimal('1.1')+Decimal('2.2'))
# print(name+"今年"+str(age))
from typing import List


def pivotIndex(nums: List[int]) -> int:
    for i in range(len(nums)+1):
        if (sum(nums[:i]) == sum(nums[i + 1:])):
            return i
    return -1
# list1=[-1,-1,-1,1,1,1]
# nums = [1, 7, 3, 6, 5, 6]
# nums1 = [1, 2, 3]
# nums2 = [2, 1, -1]
# print(pivotIndex(list1))
# print(pivotIndex(nums))
# print(pivotIndex(nums1))
# print(pivotIndex(nums2))
def searchInsert(nums: List[int], target: int) -> int:
    if target in nums:
        return nums.index(target)
    else:
        nums.append(target)
        nums1=sorted(nums)
        return nums1.index(target)
# nums=[1,3,5,6]
# target=2
# print(searchInsert(nums,target))
# print('i','love','you',sep='_')
# # name=""
# # while not name:
# #     name = input('Please enter your name:')
# # print("Hello,{}".format(name))
# words=['this','is','an','ex','parrot']
# for word in words:
#     print(word)
def square(x):
    'Calulate the square of the number x.'
    return x*x
print(square.__doc__)
print(help(square))
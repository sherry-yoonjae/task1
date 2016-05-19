#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys   
sys.setrecursionlimit(1000000)
import time
def sub_sort(array,low,high):
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        while low < high and array[high] < key:
            array[low] = array[high]
            low += 1
            array[high] = array[low]
    array[low] = key
    return low

def quick_sort(array,low,high):
     if low < high:
        key_index = sub_sort(array,low,high)
        quick_sort(array,low,key_index)
        quick_sort(array,key_index+1,high)

if __name__ == '__main__':
    start = time.time()
    array = []
    for i in range(0,10000):
        array.append(10000-i)
    quick_sort(array,0,len(array)-1)
    end = time.time()
    print ("time:%f" %(end- start))
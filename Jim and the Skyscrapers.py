# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 00:23:16 2021

@author: ASUS
"""

#!Jim and the Skyscrapers



import sys

def solution(arr):
    res = 0
    st = []
    
    for ind in range(len(arr)):
        while st and st[-1][0] < arr[ind]:
            st.pop()
        if st and arr[ind] == st[-1][0]:
            res += st[-1][1]
            st[-1][1] += 1
        else:
            st.append([arr[ind], 1])
    
    return 2*res

if __name__ == "__main__":
    n = int(input().strip())
    arr = [int(x) for x in input().strip().split()]
    print(solution(arr))
    
© 2021 GitHub, Inc.
Terms
Privacy

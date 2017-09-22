#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 18:25:49 2017

@author: hasee
"""

import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-1,1,50)
y1=x*2+1
y2=x**2+1

plt.figure(num=3,figsize=(8,8))
plt.plot(x,y1)
plt.xlim((-1,2))
plt.xlim((-2,3))

plt.figure(num=5,figsize=(9,5))
l1,=plt.plot(x,y1)
l2,=plt.plot(x,y2,color='red',linewidth=3.0,linestyle='--')
plt.xticks(np.linspace(-1,2,5))
plt.yticks([-2,-1.8,-1,1.22,3],[r'$really\ GOOD$','B','C','D','E'])

plt.legend(handles=[l1,l2],labels=['aaa','bbb'],loc='right')

plt.show()
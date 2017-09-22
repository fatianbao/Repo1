#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 15:52:55 2017

@author: hasee
"""

import numpy as np
import pandas as pd

dates=pd.date_range('20130101',periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
df.A[df.A>4]=0
df['E']=pd.Series([1,2,3,4,5,6],index=dates)
print(df)
print(pd.Series([1,2,3,4,5,6]))
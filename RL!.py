#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 21:06:36 2017

@author: hasee
"""

import numpy as np
import pandas as pd
dates=pd.date_range('20160101',periods=6)
df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])
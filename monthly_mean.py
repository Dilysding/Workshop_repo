# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 16:31:52 2022

@author: admin
"""
import numpy as np
from datetime import datetime, timedelta

def monthly_average(x, t, t_sel):
    #print(list(x[np.where(np.round(t)==t_sel)]))
    x_sel = x[np.where(np.round(t)==t_sel)]
    y = np.mean(x_sel)    
    return y
    
mon_series = []
t0 = datetime(year=2022, month=1, day=1)
for i in range(365):
    t = t0 + timedelta(days=i)
    mon_series.append(t.month)
    
Array = np.random.randint(low=-10,high=10,size=len(mon_series))

select_mon = [3]

m = []
for mon_sel in select_mon:
    m.append(monthly_average(Array, mon_series, mon_sel))
    
print(m)
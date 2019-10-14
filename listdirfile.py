# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 11:08:08 2019

@author: LZM
"""
import os
def walk(dirname):
    for name in os.listdir(dirname):
        path=os.path.join(dirname,name)
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)
walk('C:\\CloudMusic\\script')
            
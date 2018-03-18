import os
import logging
import numpy as np
import pandas as pd



def dofilesystem(filename):
    os.remove(filename)


def dopandas():
    dates = pd.date_range('20130101', periods=6)
    df= pd.DataFrame(data=np.random.randn(6,4),index=dates, columns=['a','b','c','d'])
    b=df['a'].mean()
    logging.warn("test")
    return b


    
    
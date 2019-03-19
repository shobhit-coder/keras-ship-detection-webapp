import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

import os
import cv2
import tensorflow as tf
from keras import backend as K


def customloss(y_true,y_pred):
    mask1=[True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,False]           #box
    mask2=[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True]        #object
    y_true1=tf.boolean_mask(y_true,mask1)
    y_true2=tf.boolean_mask(y_true,mask2)
    y_pred1=tf.boolean_mask(y_pred,mask1)
    y_pred2=tf.boolean_mask(y_pred,mask2)
    x1=K.square(y_true1-y_pred1)
    x2=K.square(y_true2-y_pred2)
    x1 = y_true2*x1  
#     print(y_true.shape)
    return x1+x2
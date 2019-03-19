import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

import os
#print(os.listdir("../input"))


import keras
import tensorflow as tf
import numpy as np
import cv2 
import keras.backend as K

model=keras.models.load_model('21Febtrainedmodel.h5')


print(model.summary())

for filename in os.listdir('testimages/'):
        print(filename+'-------------')
        frame = cv2.imread('testimages/'+filename)
        frame = cv2.resize(frame, (300,300))
        #fr1 = frame
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #frame = cv2.medianBlur(frame, 3)#ksize[, dst])
        # #cv2.imshow('Original',frame)
        cv2.imshow('Original',frame)
        frame = frame.reshape(1, 300, 300, 1)
        frame=frame/255
        result = model.predict(frame)
   
        print(result)
        #image_saved = cv2.rectangle(fr1,(topleftx,toplefty) ,(bottomrightx,bottomrighty),100,3)

        #cv2.imwrite('testpics/'+'predicted'+filename,image_saved)

        #cv2.imshow('frame',fr1)



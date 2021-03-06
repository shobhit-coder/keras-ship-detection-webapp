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
import time
# import pyodbc
import datetime

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

# server = 'adroit.database.windows.net'
# database = 'codefundo-db'
# username = 'Adroitadmin1'
# password = 'Adroitpassword1'
# driver= '{ODBC Driver 17 for SQL Server}'
# cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
# cursor = cnxn.cursor()

# cursor.execute("select * from location;")
# row = cursor.fetchone()
# while row:
#     print (str(row[0]) + " " + str(row[1])+" "+str(row[2]))
#     row = cursor.fetchone()


# def loss_func(y_true,y_pred):
#     print(y_true)
#     print(y_pred)
#     mask = np.array([False, False, False,False,True])   # check column of the class of object
#     mask1 = np.array([True, True, True,True,False])     # get the columns of the coordinates of B box
#     check_class = K.mean(K.square(tf.subtract(tf.boolean_mask(y_true,mask),tf.boolean_mask(y_pred,mask))))
#     mean_square = K.mean(K.square(tf.subtract(tf.boolean_mask(y_true,mask1),tf.boolean_mask(y_pred,mask1))))
#     value=K.mean(tf.boolean_mask(y_true,mask))
    
#     return value*mean_square/1000 + check_class
print(os.getcwd())


#print(model.summary())

# for filename in os.listdir('testpics/'):
#     if filename.endswith(".jpg"):
#         frame = cv2.imread('testpics/'+filename)
#         frame = cv2.resize(frame, (400,400))
#         fr1 = frame
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         #frame = cv2.medianBlur(frame, 3)#ksize[, dst])
#         # #cv2.imshow('Original',frame)
#         cv2.imshow('Original',frame)
#         frame = frame.reshape(1, 400, 400, 1)
#         frame=frame/255
#         coord=model.predict(frame)
#         print(coord)
#         print(coord[0])
#         topleftx=int(coord[1][0][0])
#         toplefty=int(coord[1][0][1])
#         bottomrightx=int(coord[1][0][2])
#         bottomrighty=int(coord[1][0][3])
        
#         image_saved = cv2.rectangle(fr1,(topleftx,toplefty) ,(bottomrightx,bottomrighty),100,3)

#         cv2.imwrite('testpics/'+'predicted'+filename,image_saved)

#         cv2.imshow('frame',fr1)


def returnImagewithrectangle(image,name):
    K.clear_session()
    model=keras.models.load_model('8novtrainedmodel2.h5')

    graph = tf.get_default_graph()
    global cooord
    frame = cv2.imread(image)
    frame = cv2.resize(frame, (400,400))
    fr1 = frame
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #frame = cv2.medianBlur(frame, 3)#ksize[, dst])
    # #cv2.imshow('Original',frame)
    #cv2.imshow('Original',frame)
    frame = frame.reshape(1, 400, 400, 1)
    frame=frame/255
    with graph.as_default():
        global coord
        coord=model.predict(frame)
        print(coord)
        print(coord[0])
    topleftx=int(coord[1][0][0])
    toplefty=int(coord[1][0][1])
    bottomrightx=int(coord[1][0][2])
    bottomrighty=int(coord[1][0][3])

    if(coord[0]<0.5):
        returnvalue = 'Car was detected!!'
        classname = "CAR"
    else:
        returnvalue = 'Ship was detected!!'
        classname = "SHIP"
    
    image_saved = cv2.rectangle(fr1,(topleftx,toplefty) ,(bottomrightx,bottomrighty),100,3)

    cv2.imwrite('static/predicted/predictedourmodel_'+name + '.jpg',image_saved)
    K.clear_session()

    #inserting data into DB

    # cursor.execute("insert into objdetect values (\'"+st+"\' , \'"+classname+"\',\'"+str(topleftx)+"\',\'"+str(toplefty)+"\',\'"+str(bottomrightx)+"\',\'"+str(bottomrighty)+"\');")
    # cnxn.commit()

    

    return returnvalue

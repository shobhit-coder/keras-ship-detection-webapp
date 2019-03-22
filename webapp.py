import os
from Mask_RCNN.samples import codercnn
from flask import Flask,redirect,url_for,request,render_template
from werkzeug import secure_filename
from testmodel import returnImagewithrectangle
from resnet import app as a1
app = Flask(__name__)
import cv2
from yolo1 import yolo_video
import traceback

vfilepath='static/video1.mp4'
currentmodel='none'
UPLOAD_FOLDER = 'static/uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
filepath='static/camera.png'
filename='lala'
@app.route('/')
def welcome():
    print("inside")
    return render_template('home.html',filepath='static/camera.png',vfilepath=vfilepath)


@app.route('/', methods = ['GET', 'POST'])
def upload_file():
   global currentmodel
   if request.method == 'POST':
      f = request.files['file']
      print(request.form)
      print(request.form['radio1'])
      
      currentmodel=request.form['radio1']
      global filename
      filename = secure_filename(f.filename)
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      global filepath 
      filepath=str(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      print(filepath)
      print(filename+'form')
      if filepath.split('.')[-1]=='mp4':
            vfilepath=filepath
      else:
          vfilepath='static/video.mp4'
      #run CNN here and draw a rectangle on the image and also store class of object in a variable
      #i'll also add code here once u add stuff to save it onto my local sql database
      return render_template('home.html',filepath='static/uploads/'+filename,vfilepath=vfilepath)

@app.route('/modelrun',methods = ['POST','GET'])
def run_model():    
    print(currentmodel+'boooo')
    try:
        # print(filepath.split('.')[-1]+'lololol')
        # if filepath.split('.')[-1]=='mp4':
            # vfilepath=filepath
            # filepath='static/camera.png'
        if currentmodel=="ourmodel":
            print(filepath + "filepath -------------\n")
            value1 = returnImagewithrectangle(filepath,filename)
            return render_template('home.html',filepath='static/predicted/predictedourmodel_'+filename+'.jpg',value = value1,vfilepath=vfilepath)
        elif currentmodel=="resnet":
            a1.demo(mode='static',imgfile=filepath,imgfilename=filename)
            return render_template('home.html',filepath='static/predicted/predictedresnet_'+filename,vfilepath=vfilepath)
            #return 'hello123'
        elif currentmodel=="maskrcnn":  
            codercnn.func(filepath,filename)
            # return 'a'
            return render_template('home.html',filepath='static/predicted/predictedrcnn_'+filename,vfilepath=vfilepath)
        elif currentmodel == "videotime":
            #CALL YOLO VIDEO FUNCTION HERE
            #vfilepath = set it to the location of the predicted video. try to keep it in static/predicted
            print('hello')
            return render_template('home.html',filepath='static/camera.png',vfilepath=vfilepath)
            return 'yolovideo' ##comment this line later
        else:
            yolo_video.runmodel(filename,filepath)
            return render_template('home.html',filepath='static/predicted/predictedyolo_'+filename,vfilepath=vfilepath)

    except Exception as e :
        traceback.print_exc()
        print(e)

        print("Error occured -------")
    
        return("Error occured"+str(e))




if __name__ == '__main__': 
    # image = returnImagewithrectangle('static/car7.jpg')
    # print(image)
    # cv2.imwrite('static/predicted/',image)
    app.run(host='0.0.0.0',debug = True)
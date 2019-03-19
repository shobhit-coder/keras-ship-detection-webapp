import os
from flask import Flask,redirect,url_for,request,render_template
from werkzeug import secure_filename
from testmodel import returnImagewithrectangle
app = Flask(__name__)
import cv2
# import pyodbc
# import mysql.connector
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="battlefield4",
#   database="footballmanagement"
# )
# print(mydb)

currentmodel='none'
UPLOAD_FOLDER = 'static/uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
filepath='static/camera.png'
@app.route('/')
def welcome():
    print("inside")
    return render_template('home.html',filepath='static/camera.png')


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
      #run CNN here and draw a rectangle on the image and also store class of object in a variable
      #i'll also add code here once u add stuff to save it onto my local sql database
      return render_template('home.html',filepath='static/uploads/'+filename)

@app.route('/modelrun',methods = ['POST','GET'])
def run_model():
   print(currentmodel)
   if currentmodel=="ourmodel":
      print(filepath + "filepath -------------\n")
      value1 = returnImagewithrectangle(filepath,filename)
      return render_template('home.html',filepath='static/predicted/predicted_'+filename+'.jpg',value = value1)
   else:
      return 'hello'


if __name__ == '__main__': 
    # image = returnImagewithrectangle('static/car7.jpg')
    # print(image)
    # cv2.imwrite('static/predicted/',image)
    app.run(debug = True)
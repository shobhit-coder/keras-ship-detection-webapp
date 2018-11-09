import os
from flask import Flask,redirect,url_for,request,render_template
from werkzeug import secure_filename
from testmodel import returnImagewithrectangle
app = Flask(__name__)
import cv2
# import mysql.connector
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="battlefield4",
#   database="footballmanagement"
# )
# print(mydb)

UPLOAD_FOLDER = 'static/uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
filepath='camera.png'
@app.route('/')
def welcome():
    return render_template('home.html',filepath=filepath)


@app.route('/', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      global filename
      filename = secure_filename(f.filename)
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      global filepath
      filepath=str(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      print(filepath)
      #run CNN here and draw a rectangle on the image and also store class of object in a variable
      #i'll also add code here once u add stuff to save it onto my local sql database
      return render_template('home.html',filepath='uploads/'+filename)

@app.route('/modelrun',methods = ['POST'])
def run_model():
    print(filepath + "filepath -------------")
    returnImagewithrectangle(filepath)
    return render_template('home.html',filepath='predicted/predicted.jpg')


if __name__ == '__main__':
    # image = returnImagewithrectangle('static/car7.jpg')
    # print(image)
    # cv2.imwrite('static/predicted/',image)
    app.run(debug = True)
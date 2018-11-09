import os
from flask import Flask,redirect,url_for,request,render_template
from werkzeug import secure_filename
app = Flask(__name__)

UPLOAD_FOLDER = 'C:\\Users\\SHOBHIT KUMAR\\Desktop\\projects\\shipDetectWebapp\\webapp\\static\\uploads\\'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
filepath=''
@app.route('/')
def welcome():
    return render_template('home.html',filepath=filepath)


@app.route('/', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      filename = secure_filename(f.filename)
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      filepath=str(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      print(filename)
      #run CNN here and draw a rectangle on the image and also store class of object in a variable
      #i'll also add code here once u add stuff to save it onto my local sql database
      return render_template('home.html',filepath=filename)


if __name__ == '__main__':
   app.run(debug = True)
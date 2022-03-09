from flask import Flask, request, render_template, send_file, redirect
import re
from utils.utils import generateToken, matToStr
from utils.get_border import get_border

app = Flask(__name__)

UPLOAD_FOLDER = "./uploads/"


@app.route("/", methods=['GET'])
def home():
    return render_template('home.html')


@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == "GET":
        return render_template("upload.html")

    elif request.method == "POST":
        
        try:
            token = generateToken()

            f = request.files['file']
            image_location = UPLOAD_FOLDER + token + '.' + f.filename.split('.')[-1]
            f.save(image_location)
            
            contour = matToStr(get_border(image_location))
            print(contour)

            return redirect("http://localhost:5000/border?contour="+contour, code=302)

        except Exception as e:
            print(e)
            return render_template("error.html")


@app.route("/get_image", methods=['GET'])
def get_image():

    if request.args.get('token') is not None:
        regex = re.compile('^[0-9A-F]{32}$')
        token = request.args.get('token')

        if regex.fullmatch(token):
            try:       
                filename = './uploads/' + token + '.jpg'
                return send_file(filename, mimetype='image/gif')

            except Exception as e:
                print(e)
                return render_template("error.html")
        
        else:
            print('Wrong Token')
            return render_template("error.html")
       
    else:
       return render_template("error.html")
    



@app.route("/border", methods=['POST', 'GET'])
def border():
    if request.method == "GET":

        return render_template("border.html")

    elif request.method == "POST":
        try:

            f = request.files['file']
            image_location = UPLOAD_FOLDER + f.filename
            f.save(image_location)
            return render_template("border.html")

        except Exception as e:
            print(e)
            return render_template("error.html")


if __name__ == "__main__":
    app.run()


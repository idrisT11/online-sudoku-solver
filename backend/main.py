from flask import Flask, request, render_template, send_file, redirect
import re
from utils.utils import generateToken, matToStr, strToMat, getNewVal
from utils.get_border import get_border
from utils.get_result import get_result

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
            param = "contour="+contour+"&token="+token

            return redirect("http://localhost:5000/border?"+param, code=302)

        except Exception as e:
            print(e)
            return render_template("error.html")


@app.route("/get_image/<token>", methods=['GET'])
def get_image(token):

    if token is not None:
        regex = re.compile('^[0-9A-F]{32}$')

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



@app.route("/result", methods=['GET'])
def result():

    contourStr = request.args.get('contour')
    token = request.args.get('token')

    sudokuVal = request.args.get('values')

    if contourStr is not None and len(contourStr) < 100 :
        
        try:
            contour = strToMat(contourStr)
            image_location = UPLOAD_FOLDER + token + '.' + 'jpg'

            result, new_val = get_result(image_location, contour)
            resultStr = ''.join([str(int(e)) for row in result for e in row])
            new_valStr = getNewVal(new_val)

            param = 'values=' + resultStr + '&new_val='+new_valStr

            return redirect("http://localhost:5000/result?"+param, code=302)


        except Exception as e:
            print(e)
            return render_template("error.html")  

    elif sudokuVal is not None and len(sudokuVal) < 100:
        return render_template("result.html")

    else:
        return render_template("error.html")

if __name__ == "__main__":
    app.run()


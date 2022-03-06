from flask import Flask, request, render_template
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

            f = request.files['file']
            image_location = UPLOAD_FOLDER + f.filename
            f.save(image_location)
            return render_template("success.html")

        except Exception as e:
            print(e)
            return render_template("error.html")


if __name__ == "__main__":
    app.run()

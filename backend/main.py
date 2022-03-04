from flask import Flask, request, render_template

app = Flask(__name__)

UPLOAD_FOLDER = "./uploads/"

@app.route("/", methods=['GET'])
def home():
    return render_template('home.html')

@app.route("/upload", methods=['GET', 'POST'])
def upload():
    image = request.files.getlist("files")
    if image:
        if image.read() == b"":
            return render_template("error.html")

        image_location = UPLOAD_FOLDER + image.filename
        image.save(image_location)
    
    else:
        return render_template("error.html")
     
    return render_template('upload.html')

if __name__ == "__main__":
    
    app.run()

from flask import Flask, request, render_template

app = Flask(__name__)

UPLOAD_FOLDER = "./images/"

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('home.html')

if __name__ == "__main__":
    
    app.run()

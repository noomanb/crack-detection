from flask import Flask, render_template, request, redirect, url_for
import os
from main import predict_crack, model
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'JFIF'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/predict_crack", methods = ["GET", "POST"])
def imageCheck():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            filename = secure_filename(file.filename)
            print(filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            img = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            out = predict_crack(img, model)
            return render_template("result.html", crack = out, filename = filename)
    return render_template("crack.html")


if __name__=="__main__":
    app.run(debug = True)

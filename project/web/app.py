from flask import Flask, request, render_template
from unipath import Path
from use_cases import RecognizePublicFigures

BASEDIR = Path(__file__).parent

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    photo = request.files.get('photo')
    photo.save(BASEDIR.child('static', 'upload',photo.filename))
    image_path = 'static/upload/{}'.format(photo.filename)
    converted_path = 'static/upload/converted/{}'.format(photo.filename)
    path = 'web/{}'.format(image_path)
    uc = RecognizePublicFigures()
    uc.execute(path)
    return '<img src="{}">'.format(converted_path)


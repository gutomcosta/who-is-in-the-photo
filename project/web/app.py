from flask import Flask, request, render_template
from unipath import Path
from use_cases import RecognizePublicFigures
from services import FileSystem

BASEDIR = Path(__file__).parent

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    photo = request.files.get('photo')
    file_system = FileSystem(BASEDIR)
    file_system.save_file(photo)
    image_path = file_system.upload_path_of(photo)
    identified_path = file_system.identified_path_of(photo)
    error = ''
    try:
        uc = RecognizePublicFigures()
        uc.execute(image_path)
    except ValueError as e:
        error = e.message
    
    file_system.remove_upload_files()
    return render_template('index.html', identifieds=file_system.last_identified_paths(), message=error)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
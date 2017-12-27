import face_recognition
from domain import Photo
from PIL import Image

class PhotoRepository(object):
    
    def __init__(self, image_store_path=None):
        self.image_store_path = image_store_path or 'web/static/media/identified'

    def get_photo_from(self,path):
        try:
            image = face_recognition.load_image_file(path)
            return Photo(image, path)
        except IOError:
            raise ValueError("Invalid path to image {}".format(path))
    
    def save(self, image, filename):
        try:
            path = self.image_store_path+'/'+filename
            image = image.resize((300,300), Image.ANTIALIAS)
            image.save(path)
        except IOError as e:
            raise ValueError("Cannot save image in the disk {}".format(e.message))

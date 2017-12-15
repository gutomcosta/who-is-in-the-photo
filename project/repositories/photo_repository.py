import face_recognition
from domain import Photo


class PhotoRepository(object):
    
    def __init__(self, image_store_path=None):
        self.image_store_path = image_store_path or 'web/static/upload/converted'

    def get_photo_from(self,path):
        try:
            image = face_recognition.load_image_file(path)
            return Photo(image, path)
        except IOError:
            raise ValueError("Invalid path to image {}".format(path))
    
    def save(self, image, filename):
        try:
            path = self.image_store_path+'/'+filename
            image.save(path)
        except IOError as e:
            raise ValueError("Cannot save image in the disk {}".format(e.message))

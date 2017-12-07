import face_recognition
from domain import Photo


class PhotoRepository(object):

    def get_photo_from(self,path):
        try:
            image = face_recognition.load_image_file(path)
            return Photo(image, path)
        except IOError:
            raise ValueError("Invalid path to image {}".format(path))

# import face_recognition
from domain import Photo
from PIL import Image
import random
import cv2

class PhotoRepository(object):
    
    def __init__(self, image_store_path=None):
        self.image_store_path = image_store_path or 'web/static/media/identified'

    def get_photo_from(self,path):
        try:
            # image = face_recognition.load_image_file(path)
            image = self._load_image(path)
            return Photo(image, path)
        except IOError:
            raise ValueError("Invalid path to image {}".format(path))
    
    def save(self, image, filename):
        try:
            code = random.randint(1,1000)
            names = filename.split('.')
            name  = '{}{}.{}'.format(names[0],str(code),names[1])
            path = self.image_store_path+'/'+name
            image = image.resize((300,300), Image.ANTIALIAS)
            image.save(path)
        except IOError as e:
            raise ValueError("Cannot save image in the disk {}".format(e.message))
        
    
    def _load_image(self,path):
        # opencv uses bgr color scheme, we need to convert to rgb
        image = cv2.imread(path, 3)
        b,g,r = cv2.split(image)           
        return cv2.merge([r,g,b]) 



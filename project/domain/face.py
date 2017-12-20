from PIL import Image
import cv2

class Face(object):
    def __init__(self, image, top, right, bottom, left):
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left
        self.original_image = image

    
    def is_it_a_face(self):
        eye_haarcascade_path = 'haarcascades/haarcascade_eye.xml'
        face = self.image()
        detector= cv2.CascadeClassifier(eye_haarcascade_path)
        eyes = detector.detectMultiScale(face)
        if len(eyes) > 0:
            return True
        return False
        

    def image(self):        
        face = self.original_image[self.top:self.bottom, self.left:self.right]
        face_image = Image.fromarray(face)
        face_image.save('face_extracted.jpeg')
        return face
        
    
    def expanded_image(self):
        top, left, bottom, right = self.expand_face_image()
        face =self.original_image[top:bottom, left:right]
        face_image = Image.fromarray(face)
        face_image.save('face_expanded.jpeg')
        return face

    def expand_face_image(self):
        img = Image.fromarray(self.original_image)
        height_factor = int(img.height * 0.15)    
        width_factor  = int(img.width * 0.15)
        top     = self.top    if (self.top - height_factor) < 0    else self.top - height_factor
        left    = self.left   if (self.left - width_factor) < 0     else self.left - width_factor
        bottom  = self.bottom if (self.bottom + height_factor) > img.height else  self.bottom + height_factor
        right   = self.right  if (self.right + width_factor) > img.width    else self.right + width_factor 

        return top, left, bottom, right

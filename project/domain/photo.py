import face_recognition
from face import Face
import cv2

class Photo(object):
    def __init__(self,image, path):
        self.image = image
        self.path = path

    def get_faces(self):
        haar_cascade_path = '/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml'
        detector= cv2.CascadeClassifier(haar_cascade_path);
        detected = []
        faces = detector.detectMultiScale(self.image)
        for (x,y,w,h) in faces:
            face = Face(self.image, y,x+w, y+h,x)
            detected.append(face)
        return detected

                # locations =  face_recognition.face_locations(image)
        # for (top, right, bottom, left)  in locations:
        #     frame = cv2.imread('../obama.jpeg')
        #     cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        #     cv2.imwrite("ah.png",frame)

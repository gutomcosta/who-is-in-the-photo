import face_recognition
from face import Face
import cv2
from PIL import Image


class Photo(object):
    def __init__(self,image, path):
        self.image = image
        self.path = path

    def get_faces(self):
        face_haarcascade_path = 'haarcascades/haarcascade_frontalface_default.xml'
        detector= cv2.CascadeClassifier(face_haarcascade_path)
        detected = []
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray)
        for (x,y,w,h) in faces:
            face = Face(self.image, y,x+w, y+h,x)
            if face.is_it_a_face():
                detected.append(face)
        return detected

    def highlight(self, persons):
        img = self.image.copy()
        for person in persons:
            cv2.rectangle(img, (person.face.left, person.face.top), (person.face.right, person.face.bottom), (0,0,255),2)
            cv2.putText(img, person.get_name(), (person.face.left-10,person.face.bottom+20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        return Image.fromarray(img)


                # locations =  face_recognition.face_locations(image)
        # for (top, right, bottom, left)  in locations:
        #     frame = cv2.imread('../obama.jpeg')
        #     cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        #     cv2.imwrite("ah.png",frame)

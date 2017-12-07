import face_recognition
from face import Face

class Photo(object):
    def __init__(self,image, path):
        self.image = image
        self.path = path

    def get_faces(self):
        faces = []
        face_locations = face_recognition.face_locations(self.image)
        for (top, right,bottom, left) in face_locations:
            face = Face(top, right, bottom, left)
            faces.append(face)
        
        return faces

                # locations =  face_recognition.face_locations(image)
        # for (top, right, bottom, left)  in locations:
        #     frame = cv2.imread('../obama.jpeg')
        #     cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        #     cv2.imwrite("ah.png",frame)

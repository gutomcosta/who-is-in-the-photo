import face_recognition

class PhotoRepository(object):

    def get_photo_from(path):
        image = face_recognition.load_image_file(path)
        # locations =  face_recognition.face_locations(image)
        # for (top, right, bottom, left)  in locations:
        #     frame = cv2.imread('../obama.jpeg')
        #     cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        #     cv2.imwrite("ah.png",frame)

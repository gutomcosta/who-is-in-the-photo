from domain import Person

class PersonIdentifier(object):

    def __init__(self, neural_network):
        self.neural_network = neural_network
    
    def identify(self,faces):
        persons = []
        expanded_face = len(faces) == 1
        for face in faces:
            img = face.expanded_image() if expanded_face else face.image()
            prediction = self.neural_network.predict(img)
            person = Person(prediction, face)
            persons.append(person)
        return persons
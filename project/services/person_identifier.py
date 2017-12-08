from domain import Person

class PersonIdentifier(object):

    def __init__(self, neural_network):
        self.neural_network = neural_network
    
    def identify(self,faces):
        persons = []
        for face in faces:
            prediction = self.neural_network.predict(face)
            person = Person(prediction, face)
            persons.append(person)
        return persons
from services import NeuralNetwork
from domain import Person

class PersonIdentifier(object):

    def __init__(self, neural_network=None):
        self.neural_network = neural_network or NeuralNetwork(weights_path='weights/weights.custom.model_pc90-batch20-ada.hdf5')
    
    def identify(self,faces):
        persons = []
        for face in faces:
            img = face.image()
            prediction = self.neural_network.predict(img)
            person = Person(prediction, face)
            persons.append(person)
        return persons
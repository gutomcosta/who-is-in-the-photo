

class RecognizePublicFigures(object):

    def __init__(self, photo_repository, person_identifier):
        self.photo_repository = photo_repository
        self.person_identifier = person_identifier

    def execute(self, path):
        photo = self.photo_repository.get_photo_from(path)
        faces = photo.get_faces()
        persons = self.person_identifier.identify(faces)
        image = photo.highlight(persons)
        image.save('recognized.jpeg')
    

    # from repositories import PhotoRepository
    # from use_cases import RecognizePublicFigures
    # from services import PersonIdentifier, NeuralNetwork

    # cnn = NeuralNetwork(weights_path='weights/weights.custom.model_pc90-batch20-ada.hdf5')
    # identifier = PersonIdentifier(cnn)
    # repository = PhotoRepository()
    # uc = RecognizePublicFigures(repository,identifier)
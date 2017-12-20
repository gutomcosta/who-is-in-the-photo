from repositories import PhotoRepository
from services import PersonIdentifier

class RecognizePublicFigures(object):

    def __init__(self, photo_repository=None, person_identifier=None):
        self.photo_repository = photo_repository or PhotoRepository()
        self.person_identifier = person_identifier or PersonIdentifier()

    def execute(self, path):
        photo = self.photo_repository.get_photo_from(path)
        faces = photo.get_faces()
        if not faces:
            raise ValueError('There is no faces in the image. Are you sure the image contains human faces?')
        persons = self.person_identifier.identify(faces)
        image = photo.highlight(persons)
        names = path.split('/')
        filename = names.pop()
        self.photo_repository.save(image, filename)
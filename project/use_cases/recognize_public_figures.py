class RecognizePublicFigures(object):

    def __init__(self, photo_repository, person_identifier):
        self.photo_repository = photo_repository
        self.person_identifier = person_identifier

    def execute(self, path):
        photo = self.photo_repository.get_photo_from(path)
        faces = photo.get_faces()
        persons = self.person_identifier.identify(faces)
        photo.highlight(persons)
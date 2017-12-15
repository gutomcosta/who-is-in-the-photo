class Person(object):
    
    def __init__(self,prediction, face):
        self.name = prediction['predicted_class']
        self.confidence = prediction['confidence']
        self.face = face
    
    def get_name(self):
        if self.is_known():
            return self.name
        else:
            return 'Unknown person :('

    def is_known(self):
        return self.name != None

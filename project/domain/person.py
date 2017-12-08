class Person(object):
    
    def __init__(self,prediction, face):
        self.name = prediction['predicted_class']
        self.confidence = prediction['confidence']
        self.face = face

    def is_known(self):
        return self.name != None

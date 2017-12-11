from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.optimizers import SGD, RMSprop, adam
from keras.callbacks import TensorBoard
from glob import glob 
from PIL import Image
from keras.preprocessing import image

import numpy as np

class NeuralNetwork(object):

    def __init__(self, weights_path=None, dataset_train_path=None):
        self.model = self._build_network()
        self.train_path = dataset_train_path or '../faces/train'
        self.weights = weights_path or '../weights/weights.custom.model.hdf5'
        # extract person name from full path
        self.person_names = [item[12:-1] for item in sorted(glob(self.train_path+"/*/"))]
    
    def predict(self, img):
        self.model.load_weights(self.weights)
        img = self._image_to_tensor(img)
        return self._predict(img)

    def _build_network(self):
        model = Sequential()
        model.add(Conv2D(filters=32, kernel_size=3, padding='same', activation='relu',input_shape=(100,100,3)))
        model.add(MaxPooling2D(pool_size=(2,2)))

        model.add(Conv2D(filters=64, kernel_size=3, padding='same', activation='relu'))
        model.add(MaxPooling2D(pool_size=(2,2)))

        model.add(Conv2D(filters=128, kernel_size=3, padding='same', activation='relu'))
        model.add(MaxPooling2D(pool_size=(2,2)))

        model.add(Conv2D(filters=256, kernel_size=3, padding='same', activation='relu'))
        model.add(MaxPooling2D(pool_size=(2,2)))

        model.add(Dropout(0.5))
        
        model.add(Flatten())
        model.add(Dense(100, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(83, activation='softmax'))
        return model

    def _image_to_tensor(self, img):
        img = Image.fromarray(img)
        img = img.resize((100,100), Image.ANTIALIAS)
        img_array = image.img_to_array(img)
        return np.expand_dims(img_array, axis=0)

    def _predict(self, img):
        import ipdb; ipdb.set_trace()
        index = self.model.predict_classes(img)
        class_name = ''
        if index:
            index = index[0]
            class_name = self.person_names[index]
        return {'predicted_class':class_name, 'confidence': None } 


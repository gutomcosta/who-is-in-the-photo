from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.optimizers import SGD, RMSprop, adam
from keras.callbacks import TensorBoard
from glob import glob 
from PIL import Image
from keras.preprocessing import image
from repositories import PersonRepository

import numpy as np

class NeuralNetwork(object):

    def __init__(self, weights_path=None, dataset_train_path=None, person_repository=None):
        self.model = self._build_network()
        self.train_path = dataset_train_path or '../faces/train'
        self.weights = weights_path or '../weights/weights.custom.model_pc90-batch20-ada.hdf5a'
        self.person_repository = person_repository or PersonRepository()
    
    def predict(self, img):
        self.model.load_weights(self.weights)
        img = self._image_to_tensor(img).astype('float32')/255
        return self._predict(img)

    def _build_network(self):
        model = Sequential()
        model.add(Conv2D(filters=32, kernel_size=3, padding='same', activation='relu',input_shape=(100,100,1)))
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

    def vgg_face(self):
        from keras.models import Model
        from keras.layers import Input, Convolution2D, ZeroPadding2D, MaxPooling2D, Flatten, Dropout, Activation
        
        img = Input(shape=(100, 100, 1))
        
        pad1_1 = ZeroPadding2D(padding=(1, 1))(img)
        conv1_1 = Convolution2D(64, 3, 3, activation='relu', name='conv1_1')(pad1_1)
        pad1_2 = ZeroPadding2D(padding=(1, 1))(conv1_1)
        conv1_2 = Convolution2D(64, 3, 3, activation='relu', name='conv1_2')(pad1_2)
        pool1 = MaxPooling2D((2, 2), strides=(2, 2))(conv1_2)
    
        pad2_1 = ZeroPadding2D((1, 1))(pool1)
        conv2_1 = Convolution2D(128, 3, 3, activation='relu', name='conv2_1')(pad2_1)
        pad2_2 = ZeroPadding2D((1, 1))(conv2_1)
        conv2_2 = Convolution2D(128, 3, 3, activation='relu', name='conv2_2')(pad2_2)
        pool2 = MaxPooling2D((2, 2), strides=(2, 2))(conv2_2)
    
        pad3_1 = ZeroPadding2D((1, 1))(pool2)
        conv3_1 = Convolution2D(256, 3, 3, activation='relu', name='conv3_1')(pad3_1)
        pad3_2 = ZeroPadding2D((1, 1))(conv3_1)
        conv3_2 = Convolution2D(256, 3, 3, activation='relu', name='conv3_2')(pad3_2)
        pad3_3 = ZeroPadding2D((1, 1))(conv3_2)
        conv3_3 = Convolution2D(256, 3, 3, activation='relu', name='conv3_3')(pad3_3)
        pool3 = MaxPooling2D((2, 2), strides=(2, 2))(conv3_3)
    
        pad4_1 = ZeroPadding2D((1, 1))(pool3)
        conv4_1 = Convolution2D(512, 3, 3, activation='relu', name='conv4_1')(pad4_1)
        pad4_2 = ZeroPadding2D((1, 1))(conv4_1)
        conv4_2 = Convolution2D(512, 3, 3, activation='relu', name='conv4_2')(pad4_2)
        pad4_3 = ZeroPadding2D((1, 1))(conv4_2)
        conv4_3 = Convolution2D(512, 3, 3, activation='relu', name='conv4_3')(pad4_3)
        pool4 = MaxPooling2D((2, 2), strides=(2, 2))(conv4_3)
    
        pad5_1 = ZeroPadding2D((1, 1))(pool4)
        conv5_1 = Convolution2D(512, 3, 3, activation='relu', name='conv5_1')(pad5_1)
        pad5_2 = ZeroPadding2D((1, 1))(conv5_1)
        conv5_2 = Convolution2D(512, 3, 3, activation='relu', name='conv5_2')(pad5_2)
        pad5_3 = ZeroPadding2D((1, 1))(conv5_2)
        conv5_3 = Convolution2D(512, 3, 3, activation='relu', name='conv5_3')(pad5_3)
        pool5 = MaxPooling2D((2, 2), strides=(2, 2))(conv5_3)
    
    
        fc6 = Convolution2D(4096, 7, 7, activation='relu', name='fc6')(pool5)
        fc6_drop = Dropout(0.5)(fc6)
        fc7 = Convolution2D(4096, 1, 1, activation='relu', name='fc7')(fc6_drop)
        fc7_drop = Dropout(0.5)(fc7)
        fc8 = Convolution2D(2622, 1, 1, name='fc8')(fc7_drop)
        flat = Flatten()(fc8)
        out = Activation('softmax')(flat)

        return Model(input=img, output=out)

    def _image_to_tensor(self, img):
        img = Image.fromarray(img)
        img = img.resize((100,100), Image.ANTIALIAS)
        img = img.convert('L')
        img_array = image.img_to_array(img)
        return np.expand_dims(img_array, axis=0)

    def _predict(self, img):
        index = self.model.predict_classes(img, batch_size=20)
        class_name = ''
        if index:
            index = index[0]
            class_name = self.person_repository.get_person_name(index)
        return {'predicted_class':class_name, 'confidence': None } 


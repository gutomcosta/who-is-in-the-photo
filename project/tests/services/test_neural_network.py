# coding: utf-8
from datetime import date, datetime

from mock import patch, Mock
import os
import unittest

from services import NeuralNetwork
from repositories import PhotoRepository


class NeuralNetworkTest(unittest.TestCase):

    def setUp(self):
        self.path = os.getcwd()
        self.neural_network = NeuralNetwork(dataset_train_path='../../faces/train', weights_path='../weights/weights.custom.model_pc90-batch20-ada.hdf5')
        self.photo_repository = PhotoRepository()
        self.path = os.getcwd()
        self.path +='/support/obama.jpeg'
        self.photo = self.photo_repository.get_photo_from(self.path)


    def test_it_show_predict_classes(self):
        faces = self.photo.get_faces()
        for face in faces:
            prediction = self.neural_network.predict(face.image())
            print(prediction['predicted_class'])    
        self.assertIsNotNone(prediction)
        self.assertIn('Barack Obama', prediction['predicted_class'])
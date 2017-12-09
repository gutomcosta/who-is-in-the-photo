# coding: utf-8
from datetime import date, datetime

from mock import patch, Mock
import os
import unittest

from services import NeuralNetwork
from repositories import PhotoRepository


class NeuralNetworkTest(unittest.TestCase):

    def setUp(self):
        self.neural_network = NeuralNetwork(dataset_train_path='../../faces/train')
        self.photo_repository = PhotoRepository()
        self.path = os.getcwd()
        self.path +='/support/angelina.jpeg'
        self.photo = self.photo_repository.get_photo_from(self.path)


    def test_it_show_predict_classes_with_confidence(self):
        faces = self.photo.get_faces()
        prediction = self.neural_network.predict(faces[0])
        self.assertIsNotNone(prediction)
        self.assertIn('Barack Obama', prediction['predicted_class'])
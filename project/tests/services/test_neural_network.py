# coding: utf-8
from datetime import date, datetime

from mock import patch, Mock
import os
import unittest

from services import NeuralNetwork
from repositories import PhotoRepository


class NeuralNetworkTest(unittest.TestCase):

    def setUp(self):
        self.neural_network = NeuralNetwork()
        self.photo_repository = PhotoRepository()
        self.path = os.getcwd()
        self.path +='/support/obama.jpeg'
        self.face = self.photo_repository.get_photo_from(self.path)


    def test_it_show_predict_classes_with_confidence(self):
        persons = self.neural_network.predict(self.face)
        self.assertTrue(persons[0].is_known())
        self.assertEqual('Barack Obama', persons[0].name)
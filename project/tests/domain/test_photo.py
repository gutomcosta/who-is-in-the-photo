# coding: utf-8
from datetime import date, datetime

from mock import patch, Mock
import os

import unittest

from domain import Photo
from repositories import PhotoRepository

class PhotoTest(unittest.TestCase):

    def setUp(self):
        self.photo_repository = PhotoRepository()
        self.path = os.getcwd()
        self.path +='/support/obama.jpeg'
    
        self.photo = self.photo_repository.get_photo_from(self.path)

    def test_it_returns_all_faces_from_image(self):
        faces = self.photo.get_faces()
        self.assertIsNotNone(faces)
        self.assertEqual(1,len(faces))

  
# coding: utf-8
from datetime import date, datetime

from mock import patch, Mock
import os

import unittest

from repositories import PhotoRepository


class PhotoRepositoryTest(unittest.TestCase):

    def setUp(self):
        self.photo_repository = PhotoRepository()
        self.path = os.getcwd()
        self.path +='/support/obama.jpeg'
    
    def test_it_should_return_a_photo_object(self):
        photo = self.photo_repository.get_photo_from(self.path)
        self.assertIsNotNone(photo)
        self.assertEqual(self.path, photo.path)

    def test_it_raises_value_error_when_image_does_not_exists(self):
        with self.assertRaises(ValueError):
            photo = self.photo_repository.get_photo_from('invalid_path/image.jpeg')

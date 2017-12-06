# coding: utf-8
from datetime import date, datetime

from mock import patch, Mock

import unittest

from use_cases import RecognizePublicFigures


class RecognizePublicFiguresTest(unittest.TestCase):

    def setUp(self):
        self.photo_repository = Mock()
        self.person_identifier = Mock()
        self.photo = Mock()
        self.faces = [Mock(), Mock()]
        self.persons = [Mock(), Mock()]
        self.photo_repository.get_photo_from.return_value = self.photo
        self.photo.get_faces.return_value = self.faces
        self.person_identifier.identify.return_value = self.persons
        self.use_case = RecognizePublicFigures(self.photo_repository, self.person_identifier)

    def test_it_receives_an_image_path_and_load_an_image(self):
        self.use_case.execute('faces/obama.jpg')
        self.photo_repository.get_photo_from.assert_called_with('faces/obama.jpg')
    
    def test_it_asks_to_photo_about_the_faces(self):
        self.use_case.execute('faces/obama.jpg')
        self.photo.get_faces.assert_called_with()
    
    def test_it_asks_to_person_identifier_to_identify_persons_in_the_photo(self):
        self.use_case.execute('faces/obama.jpg')
        self.person_identifier.identify.assert_called_with(self.faces)
    
    def test_it_asks_photo_to_highlight_identified_person(self):
        self.use_case.execute('faces/obama.jpg')
        self.photo.highlight.assert_called_with(self.persons)

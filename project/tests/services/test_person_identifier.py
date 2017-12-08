# coding: utf-8
from datetime import date, datetime

from mock import patch, Mock

import unittest

from services import PersonIdentifier


class PersonIdentifierTest(unittest.TestCase):

    def setUp(self):
        self.neural_network = Mock()
        self.person_identifier = PersonIdentifier(self.neural_network)
        self.neural_network.predict.return_value = {'predicted_class': 'Barack Obama', 'confidence': 0.9}
        self.face = Mock()
    
    def test_it_asks_to_neural_net_for_identify_a_person(self):
        self.person_identifier.identify([self.face])
        self.neural_network.predict.assert_called_with(self.face)
    
    def test_it_creates_a_person_object_for_each_face(self):
        persons = self.person_identifier.identify([self.face])
        self.assertEqual(1, len(persons))
        self.assertEqual('Barack Obama', persons[0].name)
        self.assertEqual(0.9, persons[0].confidence)
    
    def test_it_creates_person_null_object_when_person_is_unknown(self):
        self.neural_network.predict.return_value = {'predicted_class': None, 'confidence': None}
        persons = self.person_identifier.identify([self.face])
        self.assertEqual(1, len(persons))
        self.assertFalse(persons[0].is_known())

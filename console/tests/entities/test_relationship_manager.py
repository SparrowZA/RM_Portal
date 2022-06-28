from unittest import TestCase

from console.entities.relationship_manager import RelationshipManager


class DocumentTests(TestCase):
    def test_document_entity_to_dictionary(self):
        rm = RelationshipManager(
            id=6,
            name='Test Data',
            email='test@data.com'
        )
        expected_dict = {
            'id': 6,
            'name': 'Test Data',
            'email': 'test@data.com'
        }

        assert rm.to_dict() == expected_dict
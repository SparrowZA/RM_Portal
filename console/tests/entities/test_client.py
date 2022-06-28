from unittest import TestCase

from console.entities.client import Client


class ClientTests(TestCase):
    def test_client_entity_to_dictionary(self):
        client = Client(
            id=1,
            name='Test Data',
            company='Private',
            email='test@private.com'
        )
        expected_dict = {
            'id':1,
            'name': 'Test Data',
            'company': 'Private',
            'email': 'test@private.com'
        }

        assert client.to_dict() == expected_dict
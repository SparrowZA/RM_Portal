from unittest import TestCase

from console.entities.document_request import DocumentRequest
from console.entities.relationship_manager import RelationshipManager
from console.entities.client import Client
from console.entities.document import Document


class ClientTests(TestCase):
    def test_doc_request_entity_to_dictionary(self):
        doc_request = DocumentRequest(
            id=1,
            request_date='21 August 2020',
            submitted=False,
            doc_name='Identification Document',
            relationship_manager=RelationshipManager(id=1,name='Test',email='test@test.com'),
            client=Client(id=4,name='Dave',company='Private',email='dave@private.com'),
            client_url='5zFodbjBkv8qRHaJSXjmCG',
            document=Document(id=9,document_path='media/document/test.txt',upload_datetime='1 September 2020')
        )

        expected_dict = {
            'id':1,
            'request_date': '21 August 2020',
            'submitted': False,
            'doc_name': 'Identification Document',
            'relationship_manager': {
                'id':1,
                'name': 'Test',
                'email': 'test@test.com'
            },
            'client': {
                'id':4,
                'name': 'Dave',
                'company': 'Private',
                'email': 'dave@private.com'
            },
            'client_url': '5zFodbjBkv8qRHaJSXjmCG',
            'document': {
                'id': 9,
                'document_path': 'media/document/test.txt',
                'upload_datetime': '1 September 2020'
            }
        }

        assert doc_request.to_dict() == expected_dict
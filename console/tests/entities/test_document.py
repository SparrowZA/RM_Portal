from unittest import TestCase

from console.entities.document import Document


class DocumentTests(TestCase):
    def test_document_entity_to_dictionary(self):
        document = Document(
            id=6,
            document_path='media/documents/test.txt',
            upload_datetime='28 June 2022'
        )
        expected_dict = {
            'id': 6,
            'document_path': 'media/documents/test.txt',
            'upload_datetime': '28 June 2022'
        }

        assert document.to_dict() == expected_dict
import unittest

from console.utils.email_utils import EmailBuilder
from console.entities.document_request import DocumentRequest
from console.entities.client import Client
from console.entities.relationship_manager import RelationshipManager
from console.entities.document import Document
from console.entities.email import EmailNotification

# Pre upload request object builder for the email builder.
def build_document_request_pre_upload() -> DocumentRequest:
    client = Client(
        id=1, 
        name='Dave Masters', 
        company='Tech-No-Logic',
        email='dave.master@tech.com'    
    )
    rm = RelationshipManager(
        id=1,
        name='Gillian November',
        email='gnovember@particles.com'
    )
    return DocumentRequest(
        id=1,
        request_date='21 March 2022',
        submitted=False,
        doc_name='Tax Return for 2022',
        relationship_manager=rm,
        client=client,
        client_url='7z8K4DuMemcAPvdPPK2dvt',
        document=None
    )

# Post upload request object builder for the email builder.
def build_document_request_post_upload() -> DocumentRequest:
    client = Client(
        id=1, 
        name='Dave Masters', 
        company='Tech-No-Logic',
        email='dave.master@tech.com'    
    )
    rm = RelationshipManager(
        id=1,
        name='Gillian November',
        email='gnovember@particles.com'
    )
    document = Document(
        id=1,
        document_path='media/documents/test.txt',
        upload_datetime='22 March 2022'
    )
    return DocumentRequest(
        id=1,
        request_date='21 March 2022',
        submitted=False,
        doc_name='Tax Return for 2022',
        relationship_manager=rm,
        client=client,
        client_url='7z8K4DuMemcAPvdPPK2dvt',
        document=document
    )

class EmailTests(unittest.TestCase):
    # Client Notification email tests.
    def test_build_client_notification_email(self):
        document_request = build_document_request_pre_upload()
        email_builder = EmailBuilder(document_request)

        notification_email = email_builder.build_client_request_email6()
        
        assert type(notification_email) == EmailNotification
        assert notification_email.sender == document_request.relationship_manager.email
        assert notification_email.recipient == [document_request.client.email]

    def test_build_client_notification_email_no_client(self):
        document_request = build_document_request_pre_upload()
        document_request.client = None

        with self.assertRaises(AttributeError):
            EmailBuilder(document_request)
    
    def test_build_client_notification_email_no_relationship_manager(self):
        document_request = build_document_request_pre_upload()
        document_request.relationship_manager = None

        with self.assertRaises(AttributeError):
            EmailBuilder(document_request)
    
    # Relationship Manager notification email.
    def test_build_rm_notification_email(self):
        document_request = build_document_request_post_upload()
        email_builder = EmailBuilder(document_request)

        notification_email = email_builder.build_rm_notification_email()
        
        assert type(notification_email) == EmailNotification
        assert notification_email.sender == document_request.relationship_manager.email
        assert notification_email.recipient == [document_request.client.email]

from console.entities.document_request import DocumentRequest
from console.entities.email import EmailNotification

REQUEST_SUBJECT = 'Document Request'
NOTIFICATION_SUBJECT = 'Document Upload Notification'

class EmailBuilder:
    def __init__(self, request: DocumentRequest):
        self.request = request
        if request.client is None or request.relationship_manager is None:
            raise AttributeError('The request is missing a Client or Relationship manager.')

    def build_rm_notification_email(self):
        if self.request.document is None:
            raise AttributeError('Missing document value from entity.')
        subject = NOTIFICATION_SUBJECT
        message = self._create_notification_message()
        sender = self.request.relationship_manager.email
        recipient = [self.request.client.email]

        return EmailNotification(
            subject=subject,
            message=message,
            sender=sender,
            recipient=recipient
        )

    def build_client_request_email6(self):
        subject = REQUEST_SUBJECT
        message = self._create_request_message()
        sender = self.request.relationship_manager.email
        recipient = [self.request.client.email]

        return EmailNotification(
            subject=subject,
            message=message,
            sender=sender,
            recipient=recipient
        )
    
    def _create_notification_message(self):
        return f'Dear {self.request.relationship_manager.name}\n\n \
        The following document was uploaded {self.request.doc_name} by {self.request.client.name}.'
    
    def _create_request_message(self):
        return f'Dear {self.request.client.name}\n\n \
        Please follow the link below and submit the following document {self.request.doc_name}.\
            \n{self._create_url()}'

    def _create_url(self):
        return 'http://127.0.0.1:8000/' + self.request.client_url

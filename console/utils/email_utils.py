from console.entities.client import Client
from console.entities.request import Request

REQUEST_SUBJECT = 'Document Request'

class EmailBuilder:
    def __init__(self, client: Client, request: Request):
        self.client = client
        self.request = request

    def build_request_email(self, form_data):
        subject = REQUEST_SUBJECT
        message = self.create_request_message(form_data.doc_name['client_email'])
        sender = '' # Need to get this from the DB
        recipients = 'swattingbats@gmail.com'
    
    def create_request_message(self, document):
        return f'Please follow the link below and submit {document}'

    def create_url(self):
        return 'http://127.0.0.1:8000/' + self.request.client_url

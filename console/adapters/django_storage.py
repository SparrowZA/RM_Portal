'''
Adapter to the Django ORM
'''
from datetime import datetime
from django.conf import PASSWORD_RESET_TIMEOUT_DAYS_DEPRECATED_MSG
from console.adapters.storage_interface import IStorage
from console.entities.document import Document
from console.entities.request import Request
from console.models import ClientModel, DocumentModel, RelationshipManagerModel, RequestModel
from console.utils.url_creator import create_unique_url

class DjangoStorage(IStorage):
    '''Adapter to use Django ORM as a storage backend.'''

    def create_request(self, request_date, submitted, doc_name, relationship_manager, client):
        ''' Create a request model and save it to the storage.
            Returns a request entity of the model.
        '''
        rm_model = RelationshipManagerModel.objects.get(
                id=relationship_manager.id
            )
        client_model = ClientModel.objects.get(id=client.id)
        #create client URL
        client_url = create_unique_url()

        #Create model
        request_model = RequestModel(
            request_date=request_date,
            submitted=submitted,
            doc_name=doc_name,
            relationship_manager=rm_model,
            client=client_model,
            client_url=client_url
            )

        #save model
        request_model.save()
        return request_model.to_entity()

    def create_client(self, name, company, email):
        client = ClientModel(name=name, company=company, email=email)
        client.save()
        return client.to_entity()

    def create_document(self, request, file) -> Document:
        doc = DocumentModel(
            request=RequestModel.objects.get(id=request.id),
            file=file,
            upload_datetime=datetime.now()
        )
        doc.save()
        return doc.to_entity()

    def get_request(self, request_id):
        try:
            request = RequestModel.objects.get(id=request_id)
        except RequestModel.DoesNotExist:
            request = None
        return request.to_entity()

    def get_request_by_url(self, client_url):
        try:
            request = RequestModel.objects.get(client_url=client_url)
        except RequestModel.DoesNotExist:
            request = None
        return request.to_entity()


    def get_client(self, client_id):
        try:
            client = ClientModel.objects.get(id=client_id)
        except ClientModel.DoesNotExist:
            client = None
        return client.to_entity()

    def get_rm(self, rm_id):
        try:
            rm = RelationshipManagerModel.objects.get(id=rm_id)
        except RelationshipManagerModel.DoesNotExist:
            rm = None
        return rm.to_entity()
    
    def get_rm_id(self, rm_email):
        try:
            rm_id = RelationshipManagerModel.objects.get(email=rm_email)
        except RelationshipManagerModel.DoesNotExist:
            rm_id = None
        return rm_id.to_entity()
    
    def update_request_submit(self, request_id, new_value):
        value = RequestModel.objects.filter(id=request_id).update(submitted=new_value)
        return value

    def update_request(self, request):
        result = RequestModel.objects.filter(id=request.id).update(
            doc_name=request.doc_name,
            submitted=request.submitted
        )
        return result

    def get_document(self, document_id):
        try:
            rm_id = Document.objects.get(pk=document_id)
        except Document.DoesNotExist:
            rm_id = None
        return rm_id.to_entity()

    def get_clients(self):
        client_list = ClientModel.objects.all()
        return [client.to_entity() for client in client_list]
    
    def get_requests(self):
        request_list = RequestModel.objects.all()
        return [request.to_entity() for request in request_list]

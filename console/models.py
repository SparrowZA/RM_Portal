from django.db import models

from console.entities.client import Client
from console.entities.relationship_manager import RelationshipManager
from console.entities.document_request import DocumentRequest
from console.entities.document import Document

class RelationshipManagerModel(models.Model):
    name = models.CharField(max_length=200, null=False)
    email = models.EmailField(null=False, unique=True)

    def to_entity(self):
        return RelationshipManager(
            id=self.id,
            name=self.name,
            email=self.email
            )

class ClientModel(models.Model):
    name = models.CharField(max_length=200, null=False)
    company = models.CharField(max_length=200, default='')
    email = models.EmailField(null=False, unique=True)

    def to_entity(self):
        return Client(
            id=self.id,
            name=self.name,
            email=self.email,
            company=self.company
        )

class RequestModel(models.Model):
    request_date = models.DateField(null=False)
    submitted = models.BooleanField(default='False')
    doc_name = models.CharField(max_length=200, null=False)
    relationship_manager = models.ForeignKey(RelationshipManagerModel, on_delete=models.CASCADE)
    client = models.ForeignKey(ClientModel, on_delete=models.CASCADE)
    client_url = models.CharField(max_length=200, unique=True)
    
    def to_entity(self):
        if hasattr(self, 'documentmodel'):
            return DocumentRequest(
                id=self.id,
                request_date=self.request_date,
                submitted=self.submitted,
                doc_name=self.doc_name,
                relationship_manager=self.relationship_manager.to_entity(),
                client=self.client.to_entity(),
                client_url=self.client_url,
                document=self.documentmodel.to_entity()
            )
        else:
            return DocumentRequest(
                id=self.id,
                request_date=self.request_date,
                submitted=self.submitted,
                doc_name=self.doc_name,
                relationship_manager=self.relationship_manager.to_entity(),
                client=self.client.to_entity(),
                client_url=self.client_url,
                document=None
            )

class DocumentModel(models.Model):
    request = models.OneToOneField(RequestModel, on_delete=models.CASCADE, primary_key=True)
    file = models.FileField(upload_to='documents/')
    upload_datetime = models.DateTimeField()
    
    def to_entity(self):
        return Document(
            id=self.pk,
            # request=self.request,
            document_path=self.file.path,
            upload_datetime=self.upload_datetime
        )

'''
>>> from console.models import RelationshipManagerModel
>>> rm = RelationshipManagerModel(name='Marc Geffroy', email='geffroymarc@gmail.com') 
>>> rm.save()

'''
from console.entities.document_request import DocumentRequest
from console.entities.document import Document


def build_console_table_list(request_list):
    if request_list is None:
        return None    
    
    result = []
    for entity in request_list:
        entity_json = entity.to_dict()
        if entity.submitted is True:
            submitted = 'Yes'
        else:
            submitted = 'No'
        
        if entity.document is None:
            upload_date = None
        else:
            upload_date = entity.document.upload_datetime

        table_row = {
            'client_name': entity.client.name,
            'client_email': entity.client.email,
            'doc_name': entity.doc_name,
            'request_date': entity.request_date,
            'submitted': submitted,
            'upload_date': upload_date,
            'client_url': entity.client_url
        }
        result.append(table_row)
        # result.append(entity.to_dict())

    return result

from dataclasses import dataclass, asdict

from console.entities.client import Client
from console.entities.relationship_manager import RelationshipManager
from console.entities.document import Document

# from console.models import ClientModel, RelationshipManagerModel

@dataclass
class DocumentRequest():
    id: int
    request_date: str
    submitted: bool
    doc_name: str
    relationship_manager: RelationshipManager
    client: Client
    client_url: str
    document: Document

    def to_dict(self):
        return asdict(self)

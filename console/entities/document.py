from dataclasses import dataclass, asdict

# from console.entities.request import Request

@dataclass
class Document():
    id: int
    # request: Request
    document_path: str
    upload_datetime: str

    def to_dict(self):
        return asdict(self)

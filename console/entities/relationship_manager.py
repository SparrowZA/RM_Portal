from dataclasses import dataclass, asdict

@dataclass
class RelationshipManager():
    id: int
    name: str
    email: str

    def to_dict(self):
        return asdict(self)

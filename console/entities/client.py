from dataclasses import dataclass, asdict

@dataclass
class Client():
    id: int
    name: str
    company: str
    email: str

    def to_dict(self):
        return asdict(self)

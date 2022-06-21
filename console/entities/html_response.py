from dataclasses import dataclass, asdict


@dataclass
class CustomResponse():
    result: str
    error_message: str
    data: dict

    def is_success(self):
        if self.result == 'success':
            return True
        else:
            return False

    def to_dict(self):
        return asdict(self)


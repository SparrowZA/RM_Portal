from dataclasses import dataclass


@dataclass
class EmailNotification:
    subject: str
    message: str
    sender: str
    recipient: list
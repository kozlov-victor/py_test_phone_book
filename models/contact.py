
class Contact:
    def __init__(self):
        self.phone = ''

    def to_dict(self) -> dict:
        return {"phone": self.phone}

    def from_dict(self, d: dict):
        self.phone = d.get('phone')

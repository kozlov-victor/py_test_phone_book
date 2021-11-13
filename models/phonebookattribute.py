

class PhoneBookAttribute:
    def __init__(self,type: str, value: str):
        self.type = type
        self.value = value

    def to_dict(self) -> dict:
        return {"type":self.type, "value": self.value}

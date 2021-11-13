class Contact:
    def __init__(self, name: str, attributes):
        self.name = name
        self.attributes = attributes

    def to_dict(self) -> dict:
        return {"name": self.name, "attributes": [a.to_dict() for a in self.attributes]}

    def get_val_by_attribute(self,attr_type:str,default_val):
        filtered = [a for a in self.attributes if a.type==attr_type]
        if not filtered:
            return default_val
        return filtered[0].value

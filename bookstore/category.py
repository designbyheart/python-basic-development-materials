class Category:
    def __init__(self, category_id, name):
        self.category_id = category_id
        self.name = name

    def to_dict(self):
        return {"category_id": self.category_id, "name": self.name}

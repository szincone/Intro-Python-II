# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item


class Room(Item):
    def __init__(self, name, description, items):
        super().__init__(items)
        self.name = name
        self.description = description

    def list_items(self):
        return (f"Loot: {', '.join([item for item in self.items])}.")

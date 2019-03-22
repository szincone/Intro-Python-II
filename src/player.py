# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item


class Player(Item):
    def __init__(self, name, current_room, items=['empty...']):
        super().__init__(items)
        self.player_name = name
        self.current_room = current_room

    def __str__(self):
        return (f"{self.player_name} is currently in {self.current_room.name}")

    def inventory(self):
        return (f"Inventory: {', '.join([item for item in self.items])}.")

    def take_item(self, item):
        if 'nothing' in self.inventory() or 'empty...' in self.inventory():
            self.items = [item]
        else:
            self.items.append(item)
        return (f"Picked up: {item}.")

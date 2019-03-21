# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item


class Room(Item):
    def __init__(self, name, description, items):
        super().__init__(items)
        self.name = name
        self.description = description

    def list_items(self):
        return (f"Loot: {', '.join([item.capitalize() for item in self.items])}.")

    def get_directions(self, curr_room):
        directions = {"n_to": 'north', "w_to": 'west',
                      "s_to": 'south', "e_to": 'east'}
        for key in curr_room.__dict__:
            # exits = [x for x in directions if x in curr_room.__dict__]
            exits = [directions[x]
                     for x in directions if x in curr_room.__dict__]
        # print([directions[x] for x in directions ])
        return ", ".join([exit.capitalize() for exit in exits])

import os
from textwrap import wrap
from room import Room
from player import Player

room = {
    'outside':
        Room(
            "Outside Cave Entrance", "North of you, the cave mount beckons",
            ["trinket", "cape", "pants"]
        ),

    'foyer':
        Room(
            "Foyer",
            """Dim light filters in from the south. Dusty passages run north
and east.""",
            ["coin", "dog"]
        ),

    'overlook':
        Room(
            "Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
            ["apple", "chapstick"]
        ),

    'narrow':
        Room(
            "Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
            ["sword", "materia"]
        ),

    'treasure':
        Room(
            "Treasure Chamber", """You've found the long-lost treasure chamber! Sadly,
it has already been completely emptied by earlier adventurers.
The only exit is to the south.""",
            ["glasses", "card"]
        ),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
# Make a new player object that is currently in the 'outside' room.
player = Player('Hero Steve', room['outside'])
lb = '\n'
print_desc_bool = False
# Write a loop that:
while True:
    # * Prints the current room name
    # * Prints the current description
    # (the textwrap module might be useful here).
    # works below
    if print_desc_bool is False:

        print(
            f"{lb}{wrap('=' * 50)[0]}{lb}"
            f"Current Room: {wrap(player.current_room.name, 30)[0]}"
            f"{lb}{wrap('=' * 50)[0]}{lb}"
            f"{lb}{player.current_room.description}{lb}"
            f"{lb}{wrap(player.current_room.list_items())[0]}{lb}"
            f"{lb}Current Exits: {player.current_room.get_directions(player.current_room)}{lb}"
            f"{lb}{wrap('=' * 50)[0]}{lb}"
        )
        action = input("What direction do you want to move in? n/s/e/w: ")
    # * Waits for user input and decides what to do.
    [action, action_mod] = [action.split(' ')[0], action.split(
        ' ')[1]] if ' ' in action else [action, 'nothing']
    print_desc_bool = False
    # If the user enters a cardinal direction,
    # attempt to move to the room there.
    try:
        if action == 'n':
            # move north
            # print('player', player.current_room.name)
            player.current_room = player.current_room.n_to
        elif action == 's':
            # move south
            player.current_room = player.current_room.s_to
        elif action == 'e':
            # move east
            player.current_room = player.current_room.e_to
        elif action == 'w':
            # move west
            player.current_room = player.current_room.w_to
        elif action == 'take':
            player.take_item(action_mod)
        elif action == 'check':
            # list inventory
            os.system('clr||clear')
            input(player.inventory())
            # continue
        elif action == 'q':
            # If the user enters "q", quit the game.
            print("exiting the program...")
            break
        os.system('clr||clear')
    except:
        # Print an error message if the movement isn't allowed.
        os.system('clr||clear')
        print(
            f"{lb}{wrap('=' * 50)[0]}{lb}"
            f"Your path is blocked, go another direction.{lb}"
            f"{lb}Current Room: {wrap(player.current_room.name, 30)[0]}"
            f"{lb}{wrap('=' * 50)[0]}{lb}"
            f"{lb}Current Exits: {player.current_room.get_directions(player.current_room)}{lb}"
        )
        action = input("What direction do you want to move in? n/s/e/w: ")
        print_desc_bool = True
        os.system('clr||clear')
        continue

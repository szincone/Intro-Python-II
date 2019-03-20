from room import Room
from player import Player
from textwrap import wrap

room = {
    'outside':
        Room("Outside Cave Entrance", "North of you, the cave mount beckons", [
             "red trinket", "orange cape", "mc hammer pants"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ["coin", "small dog"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                     ["apple", "chapstick"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                     ["buster sword", "materia"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                     ["broken glasses", "credit card"]),
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
linebreak = "\n"
# Write a loop that:
while True:
    # * Prints the current room name
    # * Prints the current description
    # (the textwrap module might be useful here).
    # works below
    print(
        f"{linebreak}{wrap('=' * 50)[0]}{linebreak}"
        f"{' ' * 10}Room: {wrap(player.current_room.name, 30)[0]}"
        f"{linebreak}{wrap('=' * 50)[0]}{linebreak}"
        f"{player.current_room.description}{linebreak}"
        f"{linebreak}{wrap(player.current_room.list_items())[0]}"
        f"{linebreak}{wrap('=' * 50)[0]}{linebreak}"
    )
# * Waits for user input and decides what to do.
    choice = input("What direction do you want to move in? n/s/e/w: ")
# If the user enters a cardinal direction, attempt to move to the room there.
    try:
        if choice == 'n':
            # move north
            # print('player', player.current_room.name)
            player.current_room = player.current_room.n_to
        elif choice == 's':
            # move south
            player.current_room = player.current_room.s_to
        elif choice == 'e':
            # move east
            player.current_room = player.current_room.e_to
        elif choice == 'w':
            # move west
            player.current_room = player.current_room.w_to
        elif choice == 'q':
            # If the user enters "q", quit the game.
            print("exiting the program...")
            break
    except:
        # Print an error message if the movement isn't allowed.
        print(f"{linebreak}YOU SHALL NOT PASS.")

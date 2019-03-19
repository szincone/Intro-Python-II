from room import Room
from player import Player
from textwrap import wrap

room = {
    'outside':
        Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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
    print(f"Current room: {player.current_room.name} {linebreak}"
          f"You see: {wrap(player.current_room.description, 50)[0]}"
          )
# * Waits for user input and decides what to do.
    choice = input("What direction do you want to move in? n/s/e/w: ")
# If the user enters a cardinal direction, attempt to move to the room there.
    try:
        if choice == 'n':
            # move north
            print("PLAYA Be", player.current_room.name)
            player.current_room = player.current_room.n_to
            print("PLAYA Af", player.current_room.name)
        elif choice == 's':
            # move south
            print("PLAYA Be", player.current_room.name)
            player.current_room = player.current_room.s_to
            print("PLAYA Af", player.current_room.name)
        elif choice == 'e':
            # move east
            print("PLAYA Be", player.current_room.name)
            player.current_room = player.current_room.e_to
            print("PLAYA Af", player.current_room.name)
        elif choice == 'w':
            # move west
            print("PLAYA Be", player.current_room.name)
            player.current_room = player.current_room.w_to
            print("PLAYA Af", player.current_room.name)
        elif choice == 'q':
            # If the user enters "q", quit the game.
            print("exiting the program...")
            break
    except:
        # Print an error message if the movement isn't allowed.
        print("You see a big brick wall, go the other way.")

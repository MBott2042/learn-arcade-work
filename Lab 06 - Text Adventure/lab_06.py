
"""Class def for room"""


class Room:

    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


"""Standard code"""


def main():
    room_list = []
    current_room = 0
    next_room = 0
    done = False

    # Rooms 0-7 (des,N,E,S,W)
    room = Room("\nYou are in the bathroom, there is a door to the East\n", None, 1, None, None)
    room_list.append(room)

    room = Room("\nYou are in the mud room, there is a door to the East, West, and North\n", 4, 2, None, 0)
    room_list.append(room)

    room = Room("\nYou are in the Study, there is a door to the West\n", None, None, None, 1)
    room_list.append(room)

    room = Room("\nYou are in the Master Bedroom, there is a door to the East\n", None, 4, None, None)
    room_list.append(room)

    room = Room("\nYou are in the main hallway, there is a door to the East, West, North and south\n", 6, 5, 1, 3)
    room_list.append(room)

    room = Room("\nYou are in the kitchen, there is a door to the West\n", None, None, None, 4)
    room_list.append(room)

    room = Room("""\nYou are standing on the Balcony,
there is a door to the South and a Long fall if you go North\n""", 7, None, 4, None)
    room_list.append(room)

    room = Room("""\nWow your not very smart 
I think you broke some bones anyway head south to get back inside \n""", None, None, 6, None)
    room_list.append(room)

# creating a way to move around and what happens when an incorrect input is put in

    while not done:
        print(room_list[current_room].description)
        direction = input("""Where to Boss? (n s e w) or press (q) to jump off the roof. """).lower()
        if direction[0] == 'n':
            next_room = room_list[current_room].north
            if next_room == None:
                print("\nThat's a WALL Genius!")
                continue
            current_room = next_room

        elif direction[0] == 's':
            next_room = room_list[current_room].south
            if next_room == None:
                print("\nThat's a WALL Genius!")
                continue
            current_room = next_room

        elif direction[0] == 'e':
            next_room = room_list[current_room].east
            if next_room == None:
                print("\nThat's a WALL Genius!")
                continue
            current_room = next_room

        elif direction[0] == 'w':
            next_room = room_list[current_room].west
            if next_room == None:
                print("\nThat's a WALL Genius!")
                continue
            current_room = next_room

        elif direction[0] == 'q':
            done = True
            print("\nyou took the easy way out")

        else:
            print("""what is wrong with you you have five options
             and what ever you just put down is not one of them are you stupid.""")
            continue


main()

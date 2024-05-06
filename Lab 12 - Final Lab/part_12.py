"""Class def for room"""
print('''your a researcher, you got caught up in a major disaster. the SCP you where containing broke
free and as you were running away you got knocked out'
when you woke up you heard a loud roar, head North to the exit and hope it has not been locked down 
P.S. it is really quite just try to get out before it finds you''')


class Room:

    def __init__(self, description, north, east, south, west, up, down, secretI, look, secretII, secretIII, secretIV,
                 secretV):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = up
        self.down = down
        self.secretI = secretI
        self.look = look
        self.secretII = secretII
        self.secretIII = secretIII
        self.secretIV = secretIV
        self.secretV = secretV


"""Standard code"""


def main():
    room_list = []
    current_room = 0
    next_room = 0
    done = False
    monster = 0
    if monster >= 21:
        monster = 0

    monsterpath = [4, 5, 7, 3, 1, 0, 1, 8, 10, 12, 14, 16, 14, 12, 10, 8, 1, 3, 5, 4]

    # Rooms 0-30 (des,N,E,S,W)
    room = Room("\nYou are in the Security checkroom there is a page on the wall to the"
                " west, and there is a door to the North and East\n", 2, 1, None, None, None, None, None, 21, None,
                None, None, None)
    room_list.append(room)

    room = Room("\nYou are in the Entrance to Floor 1, there is a door to the North, West, and stairs that go Up\n", 3,
                None, None, 0, 8, None, None, None, None, None, None, None)
    room_list.append(room)

    room = Room("\nYou are in the General Office space, there is a door to the South and the locked exit to the North "
                "and there is a passcode protected door to the North\n", 30, None, 0, None, None, None, None, 20, None,
                None, None, None)
    room_list.append(room)

    room = Room("\nYou are in the Grade 2 office space, there is a door to the North and East and South\n", 5, 7, 1,
                None, None, None, None, None, None,
                None, None, None)
    room_list.append(room)

    room = Room("\nYou are in the Containment room "
                "There appears to be a busted up containment tube in the middle of the room"", "
                "there is a door to the South and a box on the wall \n", None, None, 5, None, None, None, None, 20,
                None, None, None, None)
    room_list.append(room)

    room = Room("\nYou are in the guard room, there is a door to the "
                "South and North and a hole in the wall to the East and a page on the wall\n", 4, 7, 3, None, None,
                None, None, 19, None, None, None, None)
    room_list.append(room)

    room = Room("\nYou are in the bathroom, there is a door to the West\n", None, None, None, 7, None, None, None,
                None, None, None, None, None)
    room_list.append(room)

    room = Room("""\nYou are in the break room there is a box on the wall, there is a door to the 
    East and West, and a hole to the North
 \n""", 5, 6, None, 3,  None, None, None, 18, None, None, None, None)
    room_list.append(room)
    # ROOMS 8 thru 15
    room = Room("\nYou are in the Hall 1, there is a door to the South and East as well as a way Down\n", None, 9, 10,
                None, None, 1, None, None, None, None, None, None)
    room_list.append(room)

    room = Room("\nYou are in the Main Entrance, there is a door blocked door to the East and a door to the West\n",
                None, None, None,
                8, None,
                None, None, None, None, None, None, None)
    room_list.append(room)

    room = Room("\nYou are in the Hall 2, there is a door to the North and South and a locked Brass door"
                " that needs a code \n", 8, None, 12,
                None, None,
                None, None, 26, None, None, None, None)
    room_list.append(room)

    room = Room("\nYou are in the Brass 1 Office, there is a door to the East as well as a code on the wall\n",
                None, 10, None,
                None, None,
                None, None, 23, None, None, None, None)
    room_list.append(room)

    room = Room("\nYou are in the Hall 3, there is a door to the North and South and a locked Brass door it"
                " that needs a code \n", 10, None, 14,
                None, None,
                None, None, 27, None, None, None, None)
    room_list.append(room)

    room = Room("\nYou are in the Brass 2 Office, there is a door to the East as well as a code on the wall\n", None,
                12, None,
                None, None,
                None, None, 24, None, None, None, None)
    room_list.append(room)

    room = Room("\nYou are in the Hall 4, there is a door to the North and a way Up and a locked Brass door it"
                " that needs a code \n", 12, None, None,
                None, 16,
                None, None, 28, None, None, None, None)
    room_list.append(room)

    room = Room("\nYou are in the Brass 3 Office, there is a door to the East as well as a code on the wall\n", None,
                14, None,
                None, None,
                None, None, 25, None, None, None, None)
    room_list.append(room)

    room = Room("\nYou are in the Armoury entrance, there is a passcoded door to the "
                "South and a way Down and a page on the wall"
                "  \n", None, None, 29,
                None, None,
                14, None, 22, None, None, None, None)
    room_list.append(room)

    room = Room("\nYou are in the Armoury , there is  a Mounted mini gun in the room"
                "(type (g) to kill the monster) or go North"
                " \n", 16, None, None,
                None, None,
                None, None, None, None, None, None, None)
    room_list.append(room)

    room = Room("\nThis is the code for Brass door 1 (r), you can go West, East or North \n", 5, 6, None,
                3, None,
                None, None, None, None, None, None, None)
    room_list.append(room)

    room = Room("\nThis is the partial code for the Gun code : part 1 (The letter between),"
                " you can go South, North, or East \n", 4, 7, 3,
                None, None,
                None, None, None, None, None, None, None)
    room_list.append(room)

    room = Room("\nThis is the code for Brass door 2 (t), you can go South \n", None, None, 5,
                None, None,
                None, None, None, None, None, None, None)
    room_list.append(room)

    room = Room("\nThis is the partial code for the Gun code : part 2 (G and I), you can go North or East \n", 2,
                1, None,
                None, None,
                None, None, None, None, None, None, None)
    room_list.append(room)

    room = Room("\nThis is the code for Brass door 3 (y), you can Down the stairs or to the passcoded door to the south \n", None, None, 29,
                None, None,
                14, None, None, None, None, None, None)
    room_list.append(room)

    room = Room("\nThis is security code 1 (It is the...), you can go West \n", None, None, None,
                10, None,
                None, None, None, None, None, None, None)
    room_list.append(room)

    room = Room("\nThis is security code 2 (....last...), you can go West \n", None, None, None,
                12, None,
                None, None, None, None, None, None, None)
    room_list.append(room)

    room = Room("\nThis is security code 3 (letter of the alphabet), you can go West \n", None, None, None,
                14, None,
                None, None, None, None, None, None, None)
    room_list.append(room)

    room = Room("\nThis is Brass door 1 enter the correct code to enter or go North or South \n", 8, None, 12,
                None, None,
                None, 11, None, None, None, None, None)
    room_list.append(room)

    room = Room("\nThis is Brass door 2 enter the correct code to enter or go North or South \n", 10, None, 14,
                None, None,
                None, None, None, 13, None, None, None)
    room_list.append(room)

    room = Room("\nThis is Brass door 3 enter the correct code to enter or go North or Up \n", 10, None, None,
                None, 16,
                None, None, None, None, 15, None, None)
    room_list.append(room)

    room = Room("\nThis is gun door enter the correct code to enter or go Down \n", None, None, None,
                None, None,
                14, None, None, None, None, 17, None)
    room_list.append(room)

    room = Room("\nThis is The exit enter the correct code to leave or go South \n", None, None, None,
                None, None,
                14, None, None, None, None, None, 31)
    room_list.append(room)

    room = Room("\nYou have won Type (f) to leave and win or go South to go back in and try to kill the beast\n", None,
                None, 2,
                None, None,
                None, None, None, None, None, None, 31)
    room_list.append(room)

    # creating a way to move around and what happens when an incorrect input is put in

    while not done:
        print(room_list[current_room].description)
        direction = input("""Where to Boss? (n s e w u d) or press (l) to look around 
        or press (q) to sit there and wait for help. """).lower()

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

        elif direction[0] == 'u':
            next_room = room_list[current_room].up
            if next_room == None:
                print("\nThat's a WALL Genius!")
                continue
            current_room = next_room

        elif direction[0] == 'd':
            next_room = room_list[current_room].down
            if next_room == None:
                print("\nThat's a WALL Genius!")
                continue
            current_room = next_room

        elif direction[0] == 'l':
            next_room = room_list[current_room].look
            if next_room == None:
                print("\nThere is nothing here")
                continue
            current_room = next_room

        elif direction[0] == 'r':
            next_room = room_list[current_room].secretI
            if next_room == None:
                print("\nThere is nothing that takes that code here")
                continue
            current_room = next_room

        elif direction[0] == 't':
            next_room = room_list[current_room].secretII
            if next_room == None:
                print("\nThere is nothing that takes that code here")
                continue
            current_room = next_room

        elif direction[0] == 'y':
            next_room = room_list[current_room].secretIII
            if next_room == None:
                print("\nThere is nothing that takes that code here")
                continue
            current_room = next_room

        elif direction[0] == 'h':
            next_room = room_list[current_room].secretIV
            if next_room == None:
                print("\nThere is nothing that takes that code here")
                continue
            current_room = next_room

        elif direction[0] == 'z':
            next_room = room_list[current_room].secretV
            if next_room == None:
                print("\nThere is nothing that takes that code here")
                continue
            current_room = next_room

        elif direction[0] == 'q':
            done = True
            print("\nGood news someone found you, Bad news it was the Monster")

        elif direction[0] == 'g':
            done = True
            print("\nyou killed the monster now have fun waiting")

        elif direction[0] == 'f':
            done = True
            print("\nyou run into the hills never to return")

        else:
            print("""what is wrong with you you have eight options
             and what ever you just put down is not one of them are you stupid.""")
            continue

        if current_room == monsterpath[monster]:
            done = True
            print("\n the monster sent you to meat god\n")
        monster = monster + 1


main()
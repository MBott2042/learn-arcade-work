import re

# This function takes in a line of text and returns
# a list of words in the line.


def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


def main():
    """ Read in lines from a file """

    # Open the file for reading, and store a pointer to it in the new
    # variable "file"
    dictionary_list = open("dictionary.txt")

    # Create an empty list to store our names
    name_list = []

    # Loop through each line in the file like a list
    for line in dictionary_list:
        # Remove any line feed, carriage returns or spaces at the end of the line
        line = line.strip()

        # Add the name to the list
        name_list.append(line)

    dictionary_list.close()

    print("There were", len(name_list), "names in the file.")

    print("--- Linear Search ---")

    alice_file = open("AliceInWonderLand200.txt")
    i = 0
    for line in alice_file:
        i += 1
        line = line.strip()
        word_list = split_line(line)
        for word in word_list:
            # --- Linear search
            key = word.upper()

            # Start at the beginning of the list
            current_list_position = 0

            # Loop until you reach the end of the list, or the value at the
            # current position is equal to the key
            while current_list_position < len(name_list) and name_list[current_list_position] != key:
                # Advance to the next item in the list
                current_list_position += 1

                if current_list_position < len(name_list):
                    word = word
                else:
                    print("line", i, word)
    alice_file.close()

    print("--- Binary search ---")
    alice_file = open("AliceInWonderLand200.txt")
    i = 0
    for line in alice_file:
        i += 1
        line = line.strip()
        word_list = split_line(line)
        for word in word_list:

            key = word.upper()
            # --- Binary search
            lower_bound = 0
            upper_bound = len(name_list) - 1
            found = False

            # Loop until we find the item, or our upper/lower bounds meet
            while lower_bound <= upper_bound and not found:

                # Find the middle position
                middle_pos = (lower_bound + upper_bound) // 2

                # Figure out if we:
                # move up the lower bound, or
                # move down the upper bound, or
                # we found what we are looking for
                if name_list[middle_pos] < key:
                    lower_bound = middle_pos + 1
                elif name_list[middle_pos] > key:
                    upper_bound = middle_pos - 1
                else:
                    found = True

            if not found:
                print("line", i, word)


    alice_file.close()


main()

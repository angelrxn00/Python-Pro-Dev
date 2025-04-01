# File -> notes.py
# Here goes the core logic of the note app

def take_notes():
    """Prompt the user for a note and save it to a file"""
    with open("notes.txt", 'a') as notes:
        print("Write here: ")
        body = input(">>> ")
        notes.write(body)


def main():
    take_notes()


if __name__ == '__main__':
    main()

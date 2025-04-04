# File -> notes.py
# Here goes the core logic of the note app


import logging

logger = logging.getLogger(__name__)

def take_notes():
    """Prompt the user for a note and save it to a file"""
    with open("notes.txt", 'a') as notes:
        print("Write here: ")
        body = input(">>> ")
        notes.write(body + "\n")



def read_notes():
    """Reads the content of the current note"""
    with open("notes.txt", 'r') as notes:
        print(notes.readline())

def main():
    take_notes()
    logging.basicConfig(filename="notes.log", level=logging.INFO)
    logger.info("Reading the notes")
    read_notes()
    logger.info("Notes read!")
    
if __name__ == '__main__':
    main()


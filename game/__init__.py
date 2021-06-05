import sys

# Load ASCII art before running the game. 
try:
    with open("./art/asciiart/happyface.txt") as f:
        happyface = f.read()
    with open("./art/asciiart/sadface.txt") as f:
        sadface = f.read()
    with open("./art/asciiart/badbanana.txt") as f:
        banana = f.read()
except OSError as err:
        print("WARNING: Unable to load one or more ASCII art files. Using emojis instead.")
        happyface = '😁'        
        sadface = '😔'
        banana = '💩 🍌 💩'
        # Enable if you want more error details.
        # print("OSError: {0}".format(err))
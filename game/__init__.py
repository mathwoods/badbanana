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
        print("OSError: {0}".format(err))
        sys.exit(1)
        

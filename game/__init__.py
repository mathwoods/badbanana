# Load images before running the game. 
with open("./art/asciiart/happyface.txt") as f:
    happyface = f.read()
with open("./art/asciiart/sadface.txt") as f:
    sadface = f.read()
with open("./art/asciiart/badbanana.txt") as f:
    badbanana = f.read()

print(happyface)
print(sadface)
print(badbanana)
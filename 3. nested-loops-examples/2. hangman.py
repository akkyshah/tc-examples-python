movie = input("Enter movie: ").upper()                # Example: "AVENGERS"
guessed_characters = len(movie) * ["_"]            # Then: ["_", "_", E, "_", "_", E, "_", "_"]
chance = 3

while chance > 0 and "_" in guessed_characters:
    character = input("Enter a character:").upper()     # E

    if character not in movie:
        chance -= 1
        print(f"\n\tIncorrect Guess: {chance} chances left")
    else:
        for i in range(0, len(movie)):
            if movie[i] == character:
                guessed_characters[i] = character
        print("\n\tCorrect Guess")

    print("\t" + "".join(guessed_characters) + "\n")

if chance == 0:
    print("You Lost")
else:
    print("you Won")

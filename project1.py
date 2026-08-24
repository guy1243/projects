letter = input("Choose a letter: ").lower()
if len(letter) == 1 and letter in "abcdefghijklmnopqrstuvwxyz":
    print("The letter is in the alphabet")
else:
    print("The letter is not in the alphabet")
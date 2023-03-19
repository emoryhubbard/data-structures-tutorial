
answer = ["r", "o", "c", "k"]
letters = []
gameover = False

while gameover != True:
    letter = input("Guess the next letter: ")
    letters.append(letter)
    print(f"Current letters: {letters}")

    if letter != answer[len(letters) - 1]:
        letters.pop()
        print("Last letter not a match, try again.")
        print(f"Current letters: {letters}")

    if letters == answer:
        gameover = True

    
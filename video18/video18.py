secret_word = "Noris"
hint = "The name has appeared many times in this project"
guess_count = 1
guess_limit = 3
print(hint)
print(f"you have {guess_limit} times to guess")
guess_word = input("Enter the prediction word: ")


while guess_word != secret_word:
    guess_count += 1
    if guess_count > guess_limit:
        guess_word = "0"
        break
    guess_word = input("Wrong, please enter again / Press 0 to exit: ");
    if guess_word == "0":
        break

if guess_word == secret_word:
    print('Correct answer, congratulations')
else:
    print('Loser')
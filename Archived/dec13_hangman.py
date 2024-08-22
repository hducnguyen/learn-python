word_to_guess = 'study'
description = 'the act of texting, eating, watching Netflix with an textbook nearby'
lives = 3

answer = []
for i in range(len(word_to_guess)):
    answer.append("_")

print(description)
print(answer)

while lives > 0:
    guess = input("Enter your guess: ")

    found = False
    for i in range(len(word_to_guess)):
        if guess == word_to_guess[i]:
            answer[i] = guess
            found = True

    if not found:
        lives -= 1
        print(f'No letter {guess} found')

    final_answer = ''
    for character in answer:
        final_answer += character

    if final_answer == word_to_guess:
        print("Gud job")
        break

    print("\nAnswer:", answer)
    print("Lives:", lives)

if lives == 0:
    print("haha you suck")
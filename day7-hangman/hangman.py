#step 1
import random
import hangman_words
import hangman_art

#TODO1 - Randomly choose a word from the word_list and assign it to a variable called chosen word
selected_word = random.choice(hangman_words.word_list)

#debug
print(hangman_art.logo)
print(f"The solution is {selected_word}.")

#step 2 - 5
#TODO1 - Create an empty list called display. For each letter in the selected_word, add a "_" to display
display = []

for i in range(len(selected_word)):
  display += "_"
end_of_game = False
lives = 6

while not end_of_game:
  random_guess = input("Please select a letter!\n").lower()

  if (random_guess in display):
    print("You've already guessed this letter, try again")

  for position in range(len(selected_word)):
    letter = selected_word[position]
    if (letter == random_guess):
      display[position] = letter
      print(display)

  if (random_guess not in selected_word):
    lives -= 1
    print(hangman_art.stages[lives])
    print(f"You have {lives} lives remaining")
    if lives == 0:
      end_of_game = True
      print("You ran out of lives. You lose")

  if "_" not in display:
    end_of_game = True
    print("You win!")
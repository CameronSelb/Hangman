import random
import os
import time

def main():

    letters_guessed = []
    lives = 6
    answer = random_word()
    answer_list = list(answer.lower())
    guess = ""
    correct = ["-" for x in answer_list]

    

    while lives > 0 and guess != answer:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"---------\n{'HANGMAN':^9}\n---------")
        draw(lives, correct)
        guess = input("Guess a word/letter: ").lower()

        if guess in letters_guessed:
            print(f"\n{guess} has already been asked!")
            time.sleep(1)
            continue
        elif guess in answer_list or len(guess) == 1:
            for i in range(len(answer_list)):
                if answer_list[i] == guess:
                    if i == 0:
                        correct[i] = guess.upper()
                    else:
                       correct[i] = guess 
            if guess not in answer_list:
                lives -= 1       
            letters_guessed.append(guess)
        elif guess == answer.lower():
            break
        else:
            lives -= 1

        if answer.lower() == ("".join(correct)).lower():
            guess = ("".join(correct))
    
    os.system('cls' if os.name == 'nt' else 'clear')
    if lives == 0:
        draw(lives, correct)
        print(f"The word was {answer}.\nYou LOSE!!!")
    else:
        print("YOU WIN!!!")
    time.sleep(2)
   
    play_again()

def draw(i,c):
    HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
    print(HANGMANPICS[len(HANGMANPICS) - (i+1)])
    print("".join(c))

def random_word():
    words = ["Hello", "Builder", "Easy", "Program", "Dog", "Animal", "Hangman", "Car", "Water", "Food", "Laptop",
     "Mouse", "Keyboard","Terminal", "Code", "Number", "Element", "Atom", "Science", "Software", "Hardware"]

    word = random.choice(words)
    return word

def play_again():
    play = (input("Would you like to play again? y/n: ")).lower()
    if play in ["n", "y"]:
        if play == "n":
            exit
        else:
            main()
    else:
        print("Enter either y/n")
        play_again()

if __name__ == '__main__':
    main()

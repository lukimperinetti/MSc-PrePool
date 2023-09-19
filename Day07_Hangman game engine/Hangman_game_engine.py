# ----- Hangman game ----- #

def hangman():

    word_to_guess = input("Player 1, enter the word to guess : ").lower()
    word_to_guess = list(word_to_guess)
    result = "".join(word_to_guess)
    print("********************")
    print("*                  *")
    print("*  Welcome to the  *")
    print("*       game       *")
    print("*                  *")
    print("********************")
    print("|  |  |  |  |  |  |")
    print("|  |  |  |  |  |  |")
    print("V  V  V  V  V  V  V")

    life = 8
    currently_guessing = ["_"]*len(word_to_guess)

    while life > 0:
        letter = input('player 2, enter a letter : ').lower()

        if len(letter) != 1 or not letter.isalpha():
            print("Please enter a valid letter.")
            continue

        if letter in word_to_guess:
            for index, char in enumerate(word_to_guess):
                if letter == char:
                    currently_guessing[index] = letter
            print("".join(currently_guessing))
            winner = "".join(currently_guessing)
            if winner == result:
                print(f"Success, you win with {life} left !")
                break
                    
        else:
            life -= 1
            print(f"Nop, try again ! life : {life}")
            if life == 7:
                print('===========|')
            if life == 6:
                print('===========|')
                print('||/        |')
            if life == 5:
                print('===========|')
                print('||/        |')
                print('||         O')
            if life == 4:
                print('===========|')
                print('||/        |')
                print('||         O')
                print("||        /|\ ")
            if life == 3:
                print('===========|')
                print('||/        |')
                print('||         O')
                print("||        /|\ ")
                print('||        / \ ')
            if life == 2:
                print('===========|')
                print('||/        |')
                print('||         O')
                print("||        /|\ ")
                print('||        / \ ')
                print('||          ')
            if life == 1:
                print('===========|')
                print('||/        |')
                print('||         O')
                print("||        /|\ ")
                print('||        / \ ')
                print('||          ')
                print('||          ')

        if life <= 0:
            print('===========|')
            print('||/        |')
            print('||         O')
            print("||        /|\ ")
            print('||        / \ ')
            print('||          ')
            print('||          ')
            print('============')
            print(f"You'r so bad life : {life}")
            print(f"the word was : {result}")
            break

hangman()

while True:
    restart = input("Do you want to restart ? (y/n) : ")
    if restart == "y":
        hangman()
    else:
        break
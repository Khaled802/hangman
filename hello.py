import random
import os
# main variables
word_list = []

shape = '''
    +------|
    |       
    |        
    |       
    |        
    |
 ===!==============
'''
man_index = [[25, 'O'], [37, '/'], [38, '|'], [39, '\\'], [52, '^'], [64, '/'], [66, '\\']]


def load_words():
    words = open('words.txt', 'r')
    line = words.readline()
    word_list = line.split(' ')
    print("words loaded successfully")
    return word_list

def choose_random_word():
    """
        choosing the a random word from world_list

        return 
            str(random word)
    """
    words_num = len(word_list)
    rand_num = random.randrange(0, words_num-1)
    return word_list[rand_num]


def check_letter(available_letters, secert_word, letter):
    '''
        check_letter(available_letters->list, letter->str)
        ----------------------------------------------------
        see if the guessed letter in alphapetic and not used before and if it at the available_letters
        then remove it from the list

        return bool(True if it is alphabitic and not used before otherwise return False)
    '''
    if len(letter) != 1 or not letter.isalpha():
        return False

    if letter in available_letters:
        available_letters.remove(letter)
        if letter in secert_word:
            return True
    return False


def right_guess(letter, secret_word, user_word):
    '''
        right_guess(letter->str, secret_word->list, user_word->list)
        -----------------------------------------------------
        if user guess a right letter, update the secret_word and remove this letter 
        from it by convert its position to '*' and also update the user_word and show 
        the letter at its position

        return int(number of changes after adding this letter)
    '''
    changes_index = []
    for i in range(len(secret_word)):
        if secret_word[i] == letter:
            secret_word[i] = '*'
            changes_index.append(i)

    for c in changes_index:
        user_word[c] = letter

    return len(changes_index)

def wrong_letter(tries_number, Shape):
    '''
        wrong_letter(tries_number->int, shape->str)
        ----------------------------------------------
        when letter is wrong, the function while update the shape
        and if the is no more tries function to return False
        return bool(no more tries function to return False otherwise True)
    '''
    index_in_shape = len(man_index) - tries_number
    Shape[man_index[index_in_shape][0]] = man_index[index_in_shape][1]
    return tries_number != 1


def print_list(l):
    '''
    print_list(l->list)
    -----------------------------------
    print the list as str format
    
    return null
    '''
    for i in l:
        print(i, end='')
    print()

def state(tries_number, user_word, available_letters, Shape):
    print('='*40)
    print_list(Shape)
    print('='*40)
    print(f"Number of tries left: {tries_number}")
    print(f"Word: ", end='')
    print_list(user_word)
    print(f"Available: ", end='')
    print_list(available_letters)
    letter = input("Enter your guess letter: ").strip().lower()
    return letter




#draft
s = '4rk'
l = []

def game():
    # first shape without the man
    Shape = list(shape)
    # get a rondom word from list
    secret_word = list(choose_random_word())
    # make the word the shown to the user
    user_word = list('_'*len(secret_word))
    # all letters available to the user
    availble_letters = list("abcdefghijklmnopqrstuvwxyz")
    # number of changes that used to dedict if user guess all letters or not
    number_of_changes = 0
    # number of tries its initial value is number of grediantes the man shape
    tries = len(man_index)
    t = 26
    while t:
        os.system('cls')
        # printing the current state and ask user for guess letter
        letter = state(tries, user_word, availble_letters, Shape)
        # check if the letter is correct or not
        if check_letter(availble_letters, secret_word,letter):
            # update the scert_word and user_word and get the number of changes that made
            number_of_changes += right_guess(letter, secret_word, user_word)
            print("Right Answer")
            # if number of changes equals the secret_word that means that user guess all letters
            if number_of_changes == len(secret_word):
                print_list(user_word)
                print("CONGRATULATIONS")
                print("╰(*°▽°*)╯")
                break
        else:
            # update the shape and tries number and check if there is more tries or not
            if not wrong_letter(tries, Shape):
                print_list(Shape)
                print("GAME OVER")
                break
            else:
                print("Wrong answer")
            tries -= 1
        t -= 1

word_list = load_words()
game()


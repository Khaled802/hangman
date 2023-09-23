from game.word import Word
from game.dashboard import Dashboard

word = Word()
dashboard = Dashboard()

while dashboard.get_rest_tries() and not word.is_finished():
    print(dashboard.get_draw())
    print(f' -- rest number of tries [{dashboard.get_rest_tries()}] -- ')
    print(f'word: {word.get_user_word()}')

    char = input('Guess charcter: ')
    if not word.guess(char):
        print('wrong expectations')
        dashboard.update_shape()
        continue

    print(' == greate work == ')

if word.is_finished():
    print(" ============ WOW YOU DID IT ============= ")
    print(f" WORD: {word.get_user_word()}")
else:
    print(" =====  GAME OVER ====== ")
    print(dashboard.get_draw())



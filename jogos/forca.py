import random


def print_welcome_game_message():
    print('********************************')
    print('Bem vindo ao Jogo da Forca')
    print('********************************')

def draws_forca(attempts):
    print('  _______     ')
    print(' |/      |    ')

    if attempts == 1:
        print(' |      (_)    ')
        print(' |             ')
        print(' |             ')
        print(' |             ')

    if attempts == 2:
        print(' |      (_)    ')
        print(' |      \      ')
        print(' |             ')
        print(' |             ')

    if attempts == 3:
        print(' |      (_)    ')
        print(' |      \|     ')
        print(' |             ')
        print(' |             ')

    if attempts == 4:
        print(' |      (_)    ')
        print(' |      \|/    ')
        print(' |             ')
        print(' |             ')

    if attempts == 5:
        print(' |      (_)    ')
        print(' |      \|/    ')
        print(' |       |     ')
        print(' |             ')

    if attempts == 6:
        print(' |      (_)    ')
        print(' |      \|/    ')
        print(' |       |     ')
        print(' |      /      ')

    if attempts == 7:
        print(' |      (_)    ')
        print(' |      \|/    ')
        print(' |       |     ')
        print(' |      / \    ')

    print(' |          ')
    print('_|___       ')
    print()
def load_secret_word():
    words_list = []
    with open('../arquivo.txt', 'r', encoding='utf-8') as file:
        for row in file:
            row = row.strip()
            words_list.append(row)

    file.close()

    index = random.randrange(0, len(words_list))

    return words_list[index].lower()


def initializes_forca(secret_word: str) -> str:
    return ['_' for letra in secret_word]


def input_user_guess():
    return input('Informe uma letra: ').strip().lower()


def check_right_guesses(secret_word, guess, right_guesses):
    index = 0
    for letter in secret_word:
        if guess == letter:
            right_guesses[index] = letter
        index += 1


def show_winner_message():
    print('Você venceu')


def show_looser_message(secret_word):
    print('Você perdeu!!')
    print(f'A palavra secreta era {secret_word}')

def play_forca():

    print_welcome_game_message()
    secret_word = load_secret_word()

    right_guesses = initializes_forca(secret_word)
    print(right_guesses)
    
    hanged = False
    right_answer = False
    attempts = 0

    while not hanged and not right_answer:
        guess = input_user_guess()

        if guess in secret_word:
            check_right_guesses(secret_word, guess, right_guesses)
        else:
            print(f'Letra incorreta! Tentativa {attempts} de {len(secret_word)}')
            attempts += 1
            draws_forca(attempts)


        hanged = attempts == 7
        right_answer = '_' not in right_guesses
        print(right_guesses)

    if right_answer:
        show_winner_message()
    else:
        show_looser_message(secret_word)


    print('Fim de jogo')
if __name__ == "__main__":
    play_forca()
import random;

def play_guess_game():
    print('********************************')
    print('Bem vindo ao jogo de Adivinhação')
    print('********************************')

    secret_number = random.randrange(1, 101)
    score = 1000

    print('Escolha um nível de dificuldade: ')
    print('(1) Fácil (2) Médio (3) Difícil')

    level = int(input('Nível: '))

    if(level == 1):
        guess_tries = 20
    elif level == 2:
        guess_tries = 10
    else:
        guess_tries = 5

    for attempt in range(1,guess_tries + 1):

        print('Tentativa {} de {}'.format(attempt, guess_tries));
        guess = int(input('Digite um número entre 1 e 100: '))

        if guess < 1 or guess > 100:
            print('Você deve informar um valor entre 1 e 100')
            continue

        right_guess = guess == secret_number
        greater_then_guess = guess > secret_number
        less_then_guess = guess < secret_number

        if right_guess:
            print('Você acertou!!!')
            print(f'Pontuação: {score}')
            break
        else:
            if less_then_guess:
                print('Você errou.Tente um número maior!')
            elif greater_then_guess:
                print('Você errou.Tente um número menor!')
                if attempt == guess_tries:
                    print(f'O número secreto era {secret_number}. Você fez {score} pontos.')
            lost_score = abs(secret_number - guess)
            score = score - lost_score
if __name__ == "__main__":
    play_guess_game()
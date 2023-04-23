print('********************************')
print('Bem vindo ao jogo de Adivinhação')
print('********************************')

secret_number = 42
guess_tries = 3
attempt = 1

guess = int(input('Digite um número: '))


while attempt <= guess_tries:

    right_guess = guess == secret_number
    greater_then_guess = guess > secret_number
    less_then_guess = guess < secret_number

    print('Tentativa {} de {}'.format(attempt, guess_tries));
    if right_guess:
        print('Você acertou!!!')
    elif less_then_guess:
        print('Você errou.Tente um número maior!')
    elif greater_then_guess:
        print('Você errou.Tente um número menor!')
    attempt = attempt + 1
    guess = int(input('Digite um número: '))

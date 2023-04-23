print('********************************')
print('Bem vindo ao jogo de Adivinhação')
print('********************************')

secret_number = 42
guess = int(input('Digite um número: '))

right_guess = guess == secret_number
greater_then_guess = guess > secret_number
less_then_guess = guess < secret_number

if right_guess:
    print('Você acertou o número')
elif less_then_guess:
    print('Você errou.Tente um número maior!')
elif greater_then_guess:
    print('Você errou.Tente um número menor!')

print('Fim do jogo')
import forca
import adivinhacao_for

def game_select():
    print('************************************')
    print('********Escolha seu jogo************')
    print('************************************')

    print('(1) Jogo da Forca (2) Adivinhação')
    selected_game = int(input('Jogo selecionado: '))

    if selected_game == 1:
        print('Jogo da Forca inicializando...')
        forca.play_forca()
    elif selected_game == 2:
        print('Jogo da Adivinhação inicializando...')
        adivinhacao_for.play_guess_game()
    else:
        print('Opção inválida! Tente novamente!')

if __name__ == "__main__":
    game_select()
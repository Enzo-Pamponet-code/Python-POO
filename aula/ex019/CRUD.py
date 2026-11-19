from functions import *



def main():
    while True:
        public_interface()
        sistema = input_('Escolha uma opção: ')
        sair = system(sistema)
        if sair:
            print('[blue]Volte sempre[/]')
            break
        print('\n'*30)
if __name__ == '__main__':
    main()
from secret_key import get_secret_key
from Interface import menu, store, find, find_accounts, generate

def main():
    secret = get_secret_key()

    passw = input('Please provide the master password: ')

    if passw == secret:
        print('You\'re in')

    else:
        print('no luck')
        exit() 

    flag = True

    while flag:
        choice = menu()
        if choice == 'q':
            flag = False
        if choice == '1':
            store()
        if choice == '2':
            find_accounts()
        if choice == '3':
            find()
        if choice == '4':
            generate()
        else:
            choice = menu()
    exit()


if __name__ == '__main__':
    main() 
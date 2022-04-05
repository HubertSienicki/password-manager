from secret_key import get_secret_key
from Interface import menu, store, find, find_accounts, generate, remove

def main():
    secret = get_secret_key()

    passw = input('Please provide the master password: ')

    if passw == secret:
        print('You\'re in')

    else:
        print('no luck')
        exit() 

    choice = menu() 
    
    while choice != 'q': 

        if choice == '1':
            store()
        if choice == '2':
            find_accounts()
        if choice == '3':
            find()
        if choice == '4':
            remove()
        if choice == '5':
            generate()
            choice = menu() #idk why this works????????????????
        else:
            choice = menu()

    exit()


if __name__ == '__main__':
    main() 
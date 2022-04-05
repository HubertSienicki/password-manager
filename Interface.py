import random
from DBDriver import find_password, store_password, find_users, remove_password

ALPHABET = ('abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTYVWXYZ', '0123456789', '(,._-*~"<>/|!@#$%^&)+=')

#Defining the main menu
def menu():
    print('-'*30)
    print(('-'*13) + 'Menu' + ('-' *13))
    print('1. Store new password')
    print('2. Find all sites and apps connected to an email')
    print('3. Find a password for a site or app')
    print('4. Remove a password')
    print('5. Generate a password for a site or app')
    print('q. Exit')
    print('-'*30)
    return input(': ')

def remove():
    print('Please select an id to remove')
    remove_password()

def store():
    print("Please provide the name of the site you want to store password for")
    app_name = input(': ')

    print('Please provide a password for this site')
    passwd = input(': ')

    print('Please provide an email for this site')
    user_email = input(': ')

    print('Please provide a username for this site')
    username = input(': ')

    if username == None:
        username = ''

    print('Please provide a url for this site')
    url = input(': ')

    store_password(passwd, username, user_email, app_name, url)


def find():
    print("Please, provide the name of an app you want to find the password for")
    app_name = input(': ')
    find_password(app_name)

def find_accounts():
    print("Please provide the email that you want to find accounts for")
    user_email = input(': ')
    find_users(user_email)

def generate():
    print("Please provide the length of password you want to generate")
    length = input(': ')
    tempPwd = passwd_generator(length)
    
    print('-'*30)
    print('Your new password: ')
    print(tempPwd)
    print('')


def passwd_generator(length):
    chars = []
    num = int(length)

    while len(chars) < num:
        m = random.randint(0, len(ALPHABET) - 1)
        alpha =  ALPHABET[m]
        n = random.randint(0, len(alpha) - 1)
        chars.append(ALPHABET[m][n])


    return ''.join(chars)
        
from DBDriver import find_password, store_password, find_users

#Defining the main menu
def menu():
    print('-'*30)
    print(('-'*13) + 'Menu'+ ('-' *13))
    print('1. Store new password')
    print('2. Find all sites and apps connected to an email')
    print('3. Find a password for a site or app')
    print('4. Generate a password for a site or app')
    print('q. Exit')
    print('-'*30)
    return input(': ')

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
    print("Please provide the emial that you want to find accounts for")
    user_email = input(': ')
    find_users(user_email)

def generate():
    pass
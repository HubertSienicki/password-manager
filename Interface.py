from DBDriver import find_password

#Defining the main menu
def menu():
    print('-'*30)
    print(('-'*13) + 'Menu'+ ('-' *13))
    print('1. Create new password')
    print('2. Find all sites and apps connected to an email')
    print('3. Find a password for a site or app')
    print('q. Exit')
    print('-'*30)
    return input(': ')

def create():
    print("Create")

def find():
    print("Please, provide the name of an app you want to find the password for")
    app_name = input(': ')
    find_password(app_name)

def find_accounts():
    print("Find_accounts")
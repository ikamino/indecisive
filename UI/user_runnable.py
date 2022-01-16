def init():
    print("Welcome to indecisive, a program designed to help you places to eat near you, depending on how you feel!")
    running = 1
    

    while running: 
        menu()
        running = 0 


def menu(): 
    print('Please input what you would like to do. Type \t help \t to get a list of commands')

    user_input = input() 
    user_input.lower
    commands(user_input)
    


def commands(user_input): 
    if user_input == help: 
        help()

def help():
    print('Here are the available functions to you \n exit: exit the program \nhelp')
    

init()
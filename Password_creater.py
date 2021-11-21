from random import*
import string

print("\tHello, it's a password creater. It creates a random password, of three types: easy, medium, and complex.\n\n") #Beginning


#Explanations of each type of password, called when the user wants to know what one of the types consists of:
def info(type):
    if type == 'easy':
        inf = '\nThe password will contain at least 6 characters: small Latin letters and numbers.'
        return inf
    elif type == 'medium':
        inf = '\nThe password will contain at least 8 characters: large and small Latin letters and numbers.'
        return inf
    elif type == 'complex':
        inf = '\nThe password will contain at least 10 characters: large and small Latin letters, numbers and symbols.'
        return inf

#The loop is designed so that when entering incorrect words, the program asks again. If everything is entered correctly, the program will exit the loop and start explaining or creating passwords: 
cycle = True
while cycle:
    type_info = input('\nIf you want to get acquainted with one of the types of our passwords, write the name of the type (easy/medium/complex). If you want to create a password immediately, write "start" ->').lower().strip()
    if type_info in {'easy', 'medium', 'complex'}:
        print(info(type_info))
        cycle1 = True
        while cycle1:
            more_info = input('\nWant to know about another type or want to start? (another/start)').lower().strip()
            if more_info == 'another':
                    what_type = input('\nWhat type you want to know more about? (easy/medium/complex) ->').lower().strip()
                    if what_type in {'easy', 'medium', 'complex'}:
                        print(info(what_type))
                    else:
                        print('\nYou have written smth different...')
            elif more_info == 'start':
                cycle = False
                break
            else:
                print('\nYou have written smth different...')
    elif type_info == 'start':
        cycle = False
        break
    else:
        print('\nYou have written smth different...')
        


#Warehouse for creation (various items are stored here)
lowercase_letters = list(string.ascii_lowercase)
uppercase_letters = list(string.ascii_uppercase)
digits = list(string.digits)
symbols = list(string.punctuation)


chars_easy = lowercase_letters + digits
chars_medium = lowercase_letters + uppercase_letters + digits
chars_complex = lowercase_letters + uppercase_letters + digits + symbols


#My program creates a password such that it contains at least 1 element from each type of elements for each type of password:
def generate_password(what_type):
    if what_type == 'easy':
        result = [choice(i) for i in (lowercase_letters, digits)] + [choice(chars_easy) for _ in range(4)]
        shuffle(result)
        return ''.join(result)
    elif what_type == 'medium':
        result = [choice(i) for i in (lowercase_letters, uppercase_letters, digits)] + [choice(chars_medium) for _ in range(5)]
        shuffle(result)
        return ''.join(result)
    elif what_type == 'complex':
        result = [choice(i) for i in (lowercase_letters, uppercase_letters, digits, symbols)] + [choice(chars_complex) for _ in range(6)]
        shuffle(result)
        return ''.join(result)



#The user choose a password type:
cycle = True
while cycle:
    what_type = input('\nWhat password do you want? (easy/medium/complex) ->').lower().strip()
    if what_type in {'easy', 'medium', 'complex'}:
        cycle = False
        break
    else:
        print('\nYou have written smth different...')

cycle = True
while cycle:
    print()
    print(generate_password(what_type))
    cycle1 = True
    while cycle1:
        another = input('\nWant a different one? (Y/N) ->').upper().strip()
        if another == 'Y':
            what_type = input('\nWhat password you want? (easy/medium/complex) ->').lower().strip()
            if what_type in {'easy', 'medium', 'complex'}:
                cycle1 = False
            else:
                print('\nYou have written smth different...')
        elif another == 'N':
            print('\nThank you for using this program, bye!!!')
            cycle = False
            break
        else:
            print('\nYou have written smth different...')
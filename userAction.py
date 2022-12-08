import dictModule
import numTens
import numHundreds
import numThousands



def main():

    userData = int(input('Enter numbers: '))

    #Exception handling, if it's true...
    while userData < 0:
        try:
            userData = int(userData)* -1

        except KeyboardInterrupt:
            print('Please enter a positive number')
            exit()

    if userData > 9999:
        print("Sorry, we dont have that")

    while 0 < userData < 100:
        numTens.zero2hundred(userData)
        return False

    while 99 < userData <= 1000:
        numHundreds.hundred2thousand(userData)
        return False

    while 9999 >= userData > 1000 :
        numThousands.thousand2func(userData)
        return False



main()
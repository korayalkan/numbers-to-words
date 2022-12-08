import dictModule

def zero2hundred(usersNumber):

    if usersNumber in dictModule.numbers:
        print(dictModule.numbers[usersNumber])

    if usersNumber not in dictModule.numbers:
        i = str(usersNumber)
        inputSplitter = i.split(' ')

        for x in inputSplitter:
            forTen = (int(x[1]) * 10)
            print(dictModule.numbers[forTen], dictModule.numbers[int(x[1])])



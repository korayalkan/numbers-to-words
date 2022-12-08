import dictModule

def hundred2thousand(usersNumber):

    if usersNumber in dictModule.numbers:
        print(dictModule.numbers[usersNumber])

    if usersNumber not in dictModule.numbers:
        i = str(usersNumber)
        inputSplitter = i.split(' ')

        for x in inputSplitter:
            forHundred = (int(x[0]) * 100)
            forTen = (int(x[1]) * 10)
            forOne = (int(x[2]) * 1)

            forElevens = (int(forTen) + int(forOne))

            #While Loops
            while (forElevens > 9) and (forElevens < 20):

                #For numbers between 10-20
                print(dictModule.numbers[forHundred], dictModule.numbers[forElevens])
                return False

            while (int(x[2]) == 0):

                #For ten numbers
                print(dictModule.numbers[forHundred], dictModule.numbers[forTen])
                return False

            while (int(x[1]) == 0):

                #Numbers like 109, 205, 304 (to print them like 'Two Hundred Nine)
                print(dictModule.numbers[forHundred], dictModule.numbers[forOne])
                return False

            while (int(x[1:]) == 0):

                #Numbers like 100, 200, 300
                print(dictModule.numbers[forHundred])
                return False

            while (forElevens > 20):

                #Numbers higher than (for example 120), here i'm teaching my program how to print 'One Hundred "Twenty One" '
                print(dictModule.numbers[forHundred], dictModule.numbers[forTen], dictModule.numbers[forOne])
                return False



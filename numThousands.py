import dictModule

def thousand2func(usersNumber):

    if usersNumber in dictModule.numbers:
        print(dictModule.numbers[usersNumber])

    if usersNumber not in dictModule.numbers:
        i = str(usersNumber)
        inputSplitter = i.split(' ')

        for x in inputSplitter:
            forThousand = (int(x[0]) * 1000)
            forHundred = (int(x[1]) * 100)
            forTen = (int(x[2]) * 10)
            forOne = (int(x[3]) * 1)

            forElevens = (int(forTen) + int(forOne))

            #While Loops
                #Starting with 9900 - 9800 ... 9000
            while int(x[2:]) == 0:
                print(dictModule.numbers[forThousand],
                      dictModule.numbers[forHundred])
                return False

                #9910 - 9920 - 9930 .... 9990
            while int(x[3]) == 0:
                print(dictModule.numbers[forThousand],
                      dictModule.numbers[forHundred],
                      dictModule.numbers[forTen])
                return False

                #9901 - 9902 - 9903 - 9904 .... 9909
            while int(x[2]) == 0:
                print(dictModule.numbers[forThousand],
                      dictModule.numbers[forHundred],
                      dictModule.numbers[forOne])
                return False

                #9911 - 9912 - 9913 - 9914 .... 9919
            while int(x[2]) == 1:
                print(dictModule.numbers[forThousand],
                      dictModule.numbers[forHundred],
                      dictModule.numbers[forElevens])
                return False

                #9921 - 9922 - 9923 - 9924 ..... 9929
            while int(x[2]) > 1:
                print(dictModule.numbers[forThousand],
                      dictModule.numbers[forHundred],
                      dictModule.numbers[forTen],
                      dictModule.numbers[forOne])
                return False
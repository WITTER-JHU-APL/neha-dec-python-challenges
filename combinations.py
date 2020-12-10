class numCombinations: 
    numInput = 0
    number = 1
    while numInput >= 0:
        numInput = int(input("Type in a number: "))
        if numInput >= 0:
            number = number * numInput
        else:
             print(number)

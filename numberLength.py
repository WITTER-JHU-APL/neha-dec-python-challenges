class lengthOfNumber:
    numInput = int(input("Enter a number: "));
    convertedNum = str(numInput)
    #print(type(convertedNum))
    def findLength(convertedNum):
            counter = 0
            for i in convertedNum:
                counter+=1
            return counter
        
    print(findLength(convertedNum),"is the length of the number you entered.")

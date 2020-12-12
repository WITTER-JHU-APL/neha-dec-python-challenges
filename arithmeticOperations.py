class stringOperations: 
    inputOne = input("Enter a number: ")
    inputTwo = input("Enter a number: ")
    print("The numbers you inputted are",inputOne,"and",inputTwo)
    print("1. Addition 2. Subtraction 3. Multiplication 4. Division")
    menu = int(input("Enter the operation you would like to use: "))
    if menu == 1:
        print(inputOne,"+",inputTwo,"=",int(inputOne)+int(inputTwo))
    if menu == 2:
        print(inputOne,"+",inputTwo,"=",int(inputOne)-int(inputTwo))
    if menu == 3:
        print(inputOne,"+",inputTwo,"=",int(inputOne)*int(inputTwo))
    if menu == 4:
        print(inputOne,"+",inputTwo,"=",int(inputOne)/int(inputTwo))
    
   

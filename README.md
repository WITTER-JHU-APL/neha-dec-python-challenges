# neha-dec-python-challenges
## Challenge One: Change String to Number
First, get a string from the user and then use a statement to change it to an integer.
```python
stringInput = input("Enter a string: ")
print(int(stringInput))
```
## Challenge Two: Combinations -- basically multiplies all the numbers
First, get the user input and then multiply/print it all by using a loop.
```python
while numInput >= 0:
        numInput = int(input("Type in a number: "))
        if numInput >= 0:
            number = number * numInput
        else:
             print(number)
```
## Challenge Three: Arithmetic Operations
Add, substract, multiply, or divide two numbers inputted by the user. The user chooses the operation.
```python
    if menu == 1:
        print(inputOne,"+",inputTwo,"=",int(inputOne)+int(inputTwo))
    if menu == 2:
        print(inputOne,"-",inputTwo,"=",int(inputOne)-int(inputTwo))
    if menu == 3:
        print(inputOne,"*",inputTwo,"=",int(inputOne)*int(inputTwo))
    if menu == 4:
        print(inputOne,"/",inputTwo,"=",int(inputOne)/int(inputTwo))
```
## Challenge Four: Length of Number converted to String
First, prompt user for number, then convert it to a string, then return the length of the string.
```python
 numInput = int(input("Enter a number: "));
 convertedNum = str(numInput)
 def findLength(convertedNum):
         counter = 0
         for i in convertedNum:
             counter+=1
         return counter
```
## Challenge Five: sort the number of dates from either descending or ascendin order based on what the user chooses.
First, choose descending or ascending order.
```python
mode = input("Enter a mode (ASC/DEC): ")  
```
Next, get user to input in 3 dates.
```python
    one = input("Type in a date (DD-MM-YYYY_HH:MM): ")
    two = input("Type in a date (DD-MM-YYYY_HH:MM): ")
    three = input("Type in a date (DD-MM-YYYY_HH:MM): ")
```
Then, compare the month, day, and years of the dates. 
Code below compares the years and places in ascending order.
```python
   if mode == "ASC":
            if int(one[6:10]) < int(two[6:10]) and int(one[6:10]) < int(three[6:10]):
                print(one, ", ")
                if int(two[6:10]) < int(three[6:10]):
                    print(two, ", ", three)
                else:
                    print(three, ", ", two)
            elif int(two[6:10]) < int(one[6:10]) and int(two[6:10]) < int(three[6:10]):
                    print(two, ", ")
                    if int(one[6:10]) < int(three[6:10]):
                        print(one, ", ", three)
                    else:
                        print(three, ", ",one)
            elif int(three[6:10]) < int(one[6:10]) and int(three[6:10]) < int(two[6:10]):
                    print(three, ", ")
                    if int(one[6:10]) < int(two[6:10]):
                        print(one, ", ", two)
                    else:
                        print(two, ", ", one)
```
   

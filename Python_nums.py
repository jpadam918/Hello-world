def testThisNumber():
    num = int(input("Enter a number to test: "))
   
    #Conditional Variables
    a = 0
    b = 10
    c = 100

    #Conditional for if number is in between 0 and 10
    if num <b and num > a :
        print("Number", num, "is in between 0 and 10")
    else:
        print("Number", num, "is NOT in between 0 and 10")

    #Conditional for if number is a prime less than 100
    if num < c and num in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97 ]: 
        print("Number", num, "is a prime less than 100")
    else:
        print("Number", num, "is NOT a prime less than 100")

    #Conditional for if number divided by 100 is less than 1
    if (num / c ) < 1 :
        print("Number", num, "divided by 100 is less than 1")
    else:
        print("Number", num, "divided by 100 is NOT less than 1")



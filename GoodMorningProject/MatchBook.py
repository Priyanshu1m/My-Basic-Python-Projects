x = int(input("Enter any number: "))

match x: 
    case 0: 
        print("it is zero")
    case 30: 
        print("it is 30")
    case _:
        print(x)

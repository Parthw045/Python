print("Welcome to Calculator !!")

def Addition(a,b):
    print(f"{a} + {b} = {a+b}")

def Sub(a,b):
    print(f"{a} - {b} = {a-b}")

def Mul(a,b):
    print(f"{a} * {b} = {a*b}")

def Div(a,b):
    print(f"{a} / {b} = {a/b}")

def Expo(a,b):
    print(f"{a} ^ {b} = {a**b}")

while True:
    choice = input("Do you want to perform any calculation ?(Yes/No) : ").upper()

    if choice == "YES" :
        print("Enter choice for calculation: ")
        print("1. Addition")
        print("2. Substraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponent(Power)")
        print("6. Stop Calculation")
        calc = int(input("Choice :"))

        if calc == 6:
            break
        elif calc not in (1, 2, 3, 4, 5):
            print("Entered invalid choice!!")
            print("Please Enter Valid Choice...")
            continue

        x = int(input("Enter 1st Number :"))
        y = int(input("Enter 2nd Number :"))
        
        if calc == 1:
            Addition(x,y)
        elif calc == 2:
            Sub(x,y)
        elif calc ==3:
            Mul(x,y)
        elif calc == 4:
            Div(x,y)
        elif calc ==5:
            Expo(x,y)
    elif choice =="NO":
        break
    else :
        print("Entered something wrong!!!")
        break
print("Thanks for visiting !!")



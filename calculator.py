n1 = float(input("Enter 1st number: "))
n2 = float(input("Enter 2nd number: "))
n = int(input("Enter operation (1=Sum, 2=Sub, 3=Mul, 4=Div): "))

if n == 1:
    total = n1 + n2
    print("Sum:", total)

elif n == 2:
    diff = n1 - n2
    print("Sub:", diff)

elif n == 3:
    prod = n1 * n2
    print("Mul:", prod)

elif n == 4:
    if n2 != 0:
        div = n1 / n2
        print("Div:", div)
    else:
        print("Error: Cannot divide by zero")

else:
    print("Invalid")

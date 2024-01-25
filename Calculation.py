from random import randint

print("Valid for only Three Digits Calculation\nMaximum time write your first number is bigger than other numbers ")
Number_for_Calaculation = int(input("Enter how many number do you want\nfor Calculation(2 <= Number_for_Calculation >=4) :"))

if(Number_for_Calaculation >= 5):
    print("You can only give 2, 3 or 4 for variable")
elif(Number_for_Calaculation <= 1):
    print("You can only give 2, 3 or 4 for variable")
elif(Number_for_Calaculation == 2):
    num1 = float(input("Enter first Number calculation : "))
    Choose_Operator = input("Choose Opertor for calculation : ")
    num2 = float(input("Enter second number for calculation : "))
    if(Choose_Operator == '*'):
        print(num1 * num2)
    elif(Choose_Operator == '-'):
        print(num1 - num2)
    elif(Choose_Operator == '+'):
        print(num1 + num2)
    elif(Choose_Operator == '/'):
        print(num1 / num2)
    elif(Choose_Operator == "//"):
        print(num1 // num2)
    elif(Choose_Operator == "**"):
        print(num1 ** num2)
    elif(Choose_Operator == '%'):
        print(num1 % num2)
elif(Number_for_Calaculation == 3):
    print("First two number Calculation will be run fast than third number")
    num1 = float(input("Enter first Number for calculation : "))
    Choose_Operator1 = input("Choose your first Operator for Operating : ")
    num2 = float(input("Enter second number for calculation : "))
    Choose_Operator2 = input("Choose your second Operator for Operating : ")
    num3 = float(input("Enter third number for calculation : "))
    if(Choose_Operator1 == '+'):
        if(Choose_Operator2 == '-'):
            print(num1+num2-num3)
        elif(Choose_Operator2 == '*'):
            print(num1+num2*num3)
        elif(Choose_Operator2 == '/'):
            print(num1+num2/num3)
        elif(Choose_Operator2 == "**"):
            print(num1+num2**num3)
        elif(Choose_Operator2 == "//"):
            print(num1+num2//num3)
        elif(Choose_Operator2 == '%'):
            print(num1+num2%num3)
        elif(Choose_Operator2 == '+'):
            print(num1+num2+num3)
    elif(Choose_Operator1 == '-'):
        if(Choose_Operator2 == '+'):
            print(num1-num2+num3)
        elif(Choose_Operator2 == '*'):
            print(num1-num2*num3)
        elif(Choose_Operator2 == '/'):
            print(num1-num2/num3)
        elif(Choose_Operator2 == "**"):
            print(num1-num2**num3)
        elif(Choose_Operator2 == "//"):
            print(num1-num2//num3)
        elif(Choose_Operator2 == '%'):
            print(num1-num2%num3)
        elif(Choose_Operator2 == '-'):
            print(num1-num2-num3)
    elif(Choose_Operator1 == '*'):
        if(Choose_Operator2 == '+'):
            print(num1*num2+num3)
        elif(Choose_Operator2 == '-'):
            print(num1*num2-num3)
        elif(Choose_Operator2 == '/'):
            print(num1*num2/num3)
        elif(Choose_Operator2 == "**"):
            print(num1*num2**num3)
        elif(Choose_Operator2 == "//"):
            print(num1*num2//num3)
        elif(Choose_Operator2 == '%'):
            print(num1*num2%num3)
        elif(Choose_Operator2 == '*'):
            print(num1*num2*num3)
    elif(Choose_Operator1 == '/'):
        if(Choose_Operator2 == '+'):
            print(num1/num2+num3)
        elif(Choose_Operator2 == '*'):
            print(num1/num2*num3)
        elif(Choose_Operator2 == '-'):
            print(num1/num2-num3)
        elif(Choose_Operator2 == "**"):
            print(num1/num2**num3)
        elif(Choose_Operator2 == "//"):
            print(num1/num2//num3)
        elif(Choose_Operator2 == '%'):
            print(num1/num2%num3)
        elif(Choose_Operator2 == '/'):
            print(num1/num2/num3)
    elif(Choose_Operator1 == "**"):
        if(Choose_Operator2 == '+'):
            print(num1**num2+num3)
        elif(Choose_Operator2 == '*'):
            print(num1**num2*num3)
        elif(Choose_Operator2 == '/'):
            print(num1**num2/num3)
        elif(Choose_Operator2 == '-'):
            print(num1**num2-num3)
        elif(Choose_Operator2 == "//"):
            print(num1**num2//num3)
        elif(Choose_Operator2 == '%'):
            print(num1**num2%num3)
        elif(Choose_Operator2 == '**'):
            print(num1**num2**num3)
    elif(Choose_Operator1 == "//"):
        if(Choose_Operator2 == '+'):
            print(num1//num2+num3)
        elif(Choose_Operator2 == '*'):
            print(num1//num2*num3)
        elif(Choose_Operator2 == '/'):
            print(num1//num2/num3)
        elif(Choose_Operator2 == "**"):
            print(num1//num2**num3)
        elif(Choose_Operator2 == '-'):
            print(num1//num2-num3)
        elif(Choose_Operator2 == '%'):
            print(num1//num2%num3)
        elif(Choose_Operator2 == "//"):
            print(num1//num2//num3)
    elif(Choose_Operator1 == '%'):
        if(Choose_Operator2 == '+'):
            print(num1%num2+num3)
        elif(Choose_Operator2 == '*'):
            print(num1%num2*num3)
        elif(Choose_Operator2 == '/'):
            print(num1%num2/num3)
        elif(Choose_Operator2 == "**"):
            print(num1%num2**num3)
        elif(Choose_Operator2 == "//"):
            print(num1%num2//num3)
        elif(Choose_Operator2 == '-'):
            print(num1%num2-num3)
        elif(Choose_Operator2 == '%'):
            print(num1%num2%num3)
elif(Number_for_Calaculation == 4):
        num_1 = float(input("Enter first number for calculation : "))
        choose_Operator1 = input("Enter 1st operator : ")
        num_2 = float(input("Enter second number for calculation : "))
        choose_Operator2 = input("Enter 2nd operator : ")
        num_3 = float(input("Enter third number for calculation : "))
        choose_Operator3 = input("Enter 3rd operator : ")
        num_4 = float(input("Enter fourth number for calculation : "))
        if(choose_Operator1 == '+'):
            if(choose_Operator2 == '+'):
                if(choose_Operator3 == '+'):
                    print(num_1 + num_2 + num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 + num_2 + num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 + num_2 + num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 + num_2 + num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 + num_2 + num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 + num_2 + num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 + num_2 + num_3 // num_4)
            elif(choose_Operator2 == '-'):
                if(choose_Operator3 == '+'):
                    print(num_1 + num_2 - num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 + num_2 - num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 + num_2 - num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 + num_2 - num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 + num_2 - num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 + num_2 - num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 + num_2 - num_3 // num_4)
            elif(choose_Operator2 == '*'):
                if(choose_Operator3 == '+'):
                    print(num_1 + num_2 * (num_3 + num_4))
                elif(choose_Operator3 == '-'):
                    print(num_1 + num_2 * num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 + num_2 * num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 + num_2 * num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 + num_2 * num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 + num_2 * num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 + num_2 * num_3 // num_4)
            elif(choose_Operator2 == '/'):
                if(choose_Operator3 == '+'):
                    print(num_1 + num_2 / num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 + num_2 / num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 + num_2 / num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 + num_2 / num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 + num_2 / num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 + num_2 / num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 + num_2 / num_3 // num_4)
            elif(choose_Operator2 == '%'):
                if(choose_Operator3 == '+'):
                    print(num_1 + num_2 % num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 + num_2 % num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 + num_2 % num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 + num_2 % num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 + num_2 % num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 + num_2 % num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 + num_2 % num_3 // num_4)
            elif(choose_Operator2 == '//'):
                if(choose_Operator3 == '+'):
                    print(num_1 + num_2 // num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 + num_2 // num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 + num_2 // num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 + num_2 // num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 + num_2 // num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 + num_2 // num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 + num_2 // num_3 // num_4)
            elif(choose_Operator2 == '**'):
                if(choose_Operator3 == '+'):
                    print(num_1 + num_2 ** num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 + num_2 ** num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 + num_2 ** num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 + num_2 ** num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 + num_2 ** num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 + num_2 ** num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 + num_2 ** num_3 // num_4)
        elif(choose_Operator1 == '-'):
            if(choose_Operator2 == '+'):
                if(choose_Operator3 == '+'):
                    print(num_1 - num_2 + num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 - num_2 + num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 - num_2 + num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 - num_2 + num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 - num_2 + num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 - num_2 + num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 - num_2 + num_3 // num_4)
            elif(choose_Operator2 == '-'):
                if(choose_Operator3 == '+'):
                    print(num_1 - num_2 - num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 - num_2 - num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 - num_2 - num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 - num_2 - num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 - num_2 - num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 - num_2 - num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 - num_2 - num_3 // num_4)
            elif(choose_Operator2 == '*'):
                if(choose_Operator3 == '+'):
                    print(num_1 - num_2 * num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 - num_2 * num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 - num_2 * num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 - num_2 * num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 - num_2 * num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 + num_2 * num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 - num_2 * num_3 // num_4)
            elif(choose_Operator2 == '/'):
                if(choose_Operator3 == '+'):
                    print(num_1 - num_2 / num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 - num_2 / num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 - num_2 / num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 - num_2 / num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 - num_2 / num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 - num_2 / num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 - num_2 / num_3 // num_4)
            elif(choose_Operator2 == '%'):
                if(choose_Operator3 == '+'):
                    print(num_1 - num_2 % num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 - num_2 % num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 - num_2 % num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 - num_2 % num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 - num_2 % num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 - num_2 % num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 - num_2 % num_3 // num_4)
            elif(choose_Operator2 == '//'):
                if(choose_Operator3 == '+'):
                    print(num_1 - num_2 // num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 - num_2 // num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 - num_2 // num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 - num_2 // num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 - num_2 // num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 - num_2 // num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 - num_2 // num_3 // num_4)
            elif(choose_Operator2 == '**'):
                if(choose_Operator3 == '+'):
                    print(num_1 - num_2 ** num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 - num_2 ** num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 - num_2 ** num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 - num_2 ** num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 - num_2 ** num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 - num_2 ** num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 - num_2 ** num_3 // num_4)
        elif(choose_Operator1 == '*'):
            if(choose_Operator2 == '+'):
                if(choose_Operator3 == '+'):
                    print(num_1 * num_2 + num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 * num_2 + num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 * num_2 + num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 * num_2 + num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 * num_2 + num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 * num_2 + num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 * num_2 + num_3 // num_4)
            elif(choose_Operator2 == '-'):
                if(choose_Operator3 == '+'):
                    print(num_1 * num_2 - num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 * num_2 - num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 * num_2 - num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 * num_2 - num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 * num_2 - num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 * num_2 - num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 * num_2 - num_3 // num_4)
            elif(choose_Operator2 == '*'):
                if(choose_Operator3 == '+'):
                    print(num_1 * num_2 * num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 * num_2 * num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 * num_2 * num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 * num_2 * num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 * num_2 * num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 * num_2 * num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 * num_2 * num_3 // num_4)
            elif(choose_Operator2 == '/'):
                if(choose_Operator3 == '+'):
                    print(num_1 * num_2 / num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 * num_2 / num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 * num_2 / num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 * num_2 / num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 * num_2 / num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 * num_2 / num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 * num_2 / num_3 // num_4)
            elif(choose_Operator2 == '%'):
                if(choose_Operator3 == '+'):
                    print(num_1 * num_2 % num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 * num_2 % num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 * num_2 % num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 * num_2 % num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 * num_2 % num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 * num_2 % num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 * num_2 % num_3 // num_4)
            elif(choose_Operator2 == '//'):
                if(choose_Operator3 == '+'):
                    print(num_1 * num_2 // num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 * num_2 // num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 * num_2 // num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 * num_2 // num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 * num_2 // num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 * num_2 // num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 * num_2 // num_3 // num_4)
            elif(choose_Operator2 == '**'):
                if(choose_Operator3 == '+'):
                    print(num_1 * num_2 ** num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 * num_2 ** num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 * num_2 ** num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 * num_2 ** num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 * num_2 ** num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 * num_2 ** num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 * num_2 ** num_3 // num_4)
        elif(choose_Operator1 == '/'):
            if(choose_Operator2 == '+'):
                if(choose_Operator3 == '+'):
                    print(num_1 / num_2 + num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 / num_2 + num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 / num_2 + num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 / num_2 + num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 / num_2 + num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 / num_2 + num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 / num_2 + num_3 // num_4)
            elif(choose_Operator2 == '-'):
                if(choose_Operator3 == '+'):
                    print(num_1 / num_2 - num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 / num_2 - num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 / num_2 - num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 / num_2 - num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 / num_2 - num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 / num_2 - num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 / num_2 - num_3 // num_4)
            elif(choose_Operator2 == '*'):
                if(choose_Operator3 == '+'):
                    print(num_1 / num_2 * num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 / num_2 * num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 / num_2 * num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 / num_2 * num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 / num_2 * num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 / num_2 * num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 / num_2 * num_3 // num_4)
            elif(choose_Operator2 == '/'):
                if(choose_Operator3 == '+'):
                    print(num_1 / num_2 / num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 / num_2 / num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 / num_2 / num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 / num_2 / num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 / num_2 / num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 / num_2 / num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 / num_2 / num_3 // num_4)
            elif(choose_Operator2 == '%'):
                if(choose_Operator3 == '+'):
                    print(num_1 / num_2 % num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 / num_2 % num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 / num_2 % num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 / num_2 % num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 / num_2 % num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 / num_2 % num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 / num_2 % num_3 // num_4)
            elif(choose_Operator2 == '//'):
                if(choose_Operator3 == '+'):
                    print(num_1 / num_2 // num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 / num_2 // num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 / num_2 // num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 / num_2 // num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 / num_2 // num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 / num_2 // num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 / num_2 // num_3 // num_4)
            elif(choose_Operator2 == '**'):
                if(choose_Operator3 == '+'):
                    print(num_1 / num_2 ** num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 / num_2 ** num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 / num_2 ** num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 / num_2 ** num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 / num_2 ** num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 / num_2 ** num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 / num_2 ** num_3 // num_4)
        elif(choose_Operator1 == '%'):
            if(choose_Operator2 == '+'):
                if(choose_Operator3 == '+'):
                    print(num_1 % num_2 + num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 % num_2 + num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 % num_2 + num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 % num_2 + num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 % num_2 + num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 % num_2 + num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 % num_2 + num_3 // num_4)
            elif(choose_Operator2 == '-'):
                if(choose_Operator3 == '+'):
                    print(num_1 % num_2 - num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 % num_2 - num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 % num_2 - num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 % num_2 - num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 % num_2 - num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 % num_2 - num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 % num_2 - num_3 // num_4)
            elif(choose_Operator2 == '*'):
                if(choose_Operator3 == '+'):
                    print(num_1 % num_2 * num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 % num_2 * num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 % num_2 * num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 % num_2 * num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 % num_2 * num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 % num_2 * num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 % num_2 * num_3 // num_4)
            elif(choose_Operator2 == '/'):
                if(choose_Operator3 == '+'):
                    print(num_1 % num_2 / num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 % num_2 / num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 % num_2 / num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 % num_2 / num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 % num_2 / num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 % num_2 / num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 % num_2 / num_3 // num_4)
            elif(choose_Operator2 == '%'):
                if(choose_Operator3 == '+'):
                    print(num_1 % num_2 % num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 % num_2 % num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 % num_2 % num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 % num_2 % num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 % num_2 % num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 % num_2 % num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 % num_2 % num_3 // num_4)
            elif(choose_Operator2 == '//'):
                if(choose_Operator3 == '+'):
                    print(num_1 % num_2 // num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 % num_2 // num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 % num_2 // num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 % num_2 // num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 % num_2 // num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 % num_2 // num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 % num_2 // num_3 // num_4)
            elif(choose_Operator2 == '**'):
                if(choose_Operator3 == '+'):
                    print(num_1 % num_2 ** num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 % num_2 ** num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 % num_2 ** num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 % num_2 ** num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 % num_2 ** num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 % num_2 ** num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 % num_2 ** num_3 // num_4)
        elif(choose_Operator1 == '//'):
            if(choose_Operator2 == '+'):
                if(choose_Operator3 == '+'):
                    print(num_1 // num_2 + num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 // num_2 + num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 // num_2 + num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 // num_2 + num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 // num_2 + num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 // num_2 + num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 // num_2 + num_3 // num_4)
            elif(choose_Operator2 == '-'):
                if(choose_Operator3 == '+'):
                    print(num_1 // num_2 - num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 // num_2 - num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 // num_2 - num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 // num_2 - num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 // num_2 - num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 // num_2 - num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 // num_2 - num_3 // num_4)
            elif(choose_Operator2 == '*'):
                if(choose_Operator3 == '+'):
                    print(num_1 // num_2 * num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 // num_2 * num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 // num_2 * num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 // num_2 * num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 // num_2 * num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 // num_2 * num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 // num_2 * num_3 // num_4)
            elif(choose_Operator2 == '/'):
                if(choose_Operator3 == '+'):
                    print(num_1 // num_2 / num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 // num_2 / num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 // num_2 / num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 // num_2 / num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 // num_2 / num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 // num_2 / num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 // num_2 / num_3 // num_4)
            elif(choose_Operator2 == '%'):
                if(choose_Operator3 == '+'):
                    print(num_1 // num_2 % num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 // num_2 % num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 // num_2 % num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 // num_2 % num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 // num_2 % num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 // num_2 % num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 // num_2 % num_3 // num_4)
            elif(choose_Operator2 == '//'):
                if(choose_Operator3 == '+'):
                    print(num_1 // num_2 // num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 // num_2 // num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 // num_2 // num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 // num_2 // num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 // num_2 // num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 // num_2 // num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 // num_2 // num_3 // num_4)
            elif(choose_Operator2 == '**'):
                if(choose_Operator3 == '+'):
                    print(num_1 // num_2 ** num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 // num_2 ** num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 // num_2 ** num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 // num_2 ** num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 // num_2 ** num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 // num_2 ** num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 // num_2 ** num_3 // num_4)
        elif(choose_Operator1 == '**'):
            if(choose_Operator2 == '+'):
                if(choose_Operator3 == '+'):
                    print(num_1 ** num_2 + num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 ** num_2 + num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 ** num_2 + num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 ** num_2 + num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 ** num_2 + num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 ** num_2 + num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 ** num_2 + num_3 // num_4)
            elif(choose_Operator2 == '-'):
                if(choose_Operator3 == '+'):
                    print(num_1 ** num_2 - num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 ** num_2 - num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 ** num_2 - num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 ** num_2 - num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 ** num_2 - num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 ** num_2 - num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 ** num_2 - num_3 // num_4)
            elif(choose_Operator2 == '*'):
                if(choose_Operator3 == '+'):
                    print(num_1 ** num_2 * num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 ** num_2 * num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 ** num_2 * num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 ** num_2 * num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 ** num_2 * num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 ** num_2 * num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 ** num_2 * num_3 // num_4)
            elif(choose_Operator2 == '/'):
                if(choose_Operator3 == '+'):
                    print(num_1 ** num_2 / num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 ** num_2 / num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 ** num_2 / num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 ** num_2 / num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 ** num_2 / num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 ** num_2 / num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 ** num_2 / num_3 // num_4)
            elif(choose_Operator2 == '%'):
                if(choose_Operator3 == '+'):
                    print(num_1 ** num_2 % num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 ** num_2 % num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 ** num_2 % num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 ** num_2 % num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 ** num_2 % num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 ** num_2 % num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 ** num_2 % num_3 // num_4)
            elif(choose_Operator2 == '//'):
                if(choose_Operator3 == '+'):
                    print(num_1 ** num_2 // num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 ** num_2 // num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 ** num_2 // num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 ** num_2 // num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 ** num_2 // num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 ** num_2 // num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 ** num_2 // num_3 // num_4)
            elif(choose_Operator2 == '**'):
                if(choose_Operator3 == '+'):
                    print(num_1 ** num_2 ** num_3 + num_4)
                elif(choose_Operator3 == '-'):
                    print(num_1 ** num_2 ** num_3 - num_4)
                elif(choose_Operator3 == '*'):
                    print(num_1 ** num_2 ** num_3 * num_4)
                elif(choose_Operator3 == '/'):
                    print(num_1 ** num_2 ** num_3 / num_4)
                elif(choose_Operator3 == '%'):
                    print(num_1 ** num_2 ** num_3 % num_4)
                elif(choose_Operator3 == '**'):
                    print(num_1 ** num_2 ** num_3 ** num_4)
                elif(choose_Operator3 == '//'):
                    print(num_1 ** num_2 ** num_3 // num_4)
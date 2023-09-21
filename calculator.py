
number1 = int(input("1.Sayıyı giriniz: "))
number2 = int(input("2.Sayıyı giriniz: "))

operation = input("Yapmak istediğiniz işlemi giriniz: ")

if(operation == "+" ):
    print(number1, "+", number2, "= ", number1 + number2)

elif(operation == "-" ):
    print(number1, "-", number2, "= ", number1 - number2)

elif(operation == "*"):
    print(number1, "*", number2, "= ", number1 * number2)

elif(operation == "/"):
    print(number1, "/", number2, "= ", number1 / number2)

else:
    print("Hatalı giriş yaptınız..")



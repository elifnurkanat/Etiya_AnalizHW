midterm = int(input("Vize notunuzu giriniz: "))
final = int(input("Final notunuzu giriniz: "))


if(final < 40 or (midterm == final*2)):
    print("Kaldınız.. ")

else:
    average = midterm*0.4 + final*0.6

    if(average <= 49):
        print("Ortalamanız: ", average, "Harf notunuz: FF, Kaldınız.. ")

    elif(average >= 50 and average <= 59):
        print("Ortalamanız: ", average, "Harf notunuz: DD, Geçtiniz..")

    elif(average >= 60 and average <= 69):
        print("Ortalamanız: ", average, "Harf notunuz: CC, Geçtiniz..")

    elif(average >= 70 and average <= 79):
        print("Ortalamanız: ", average, "Harf notunuz: BB, Geçtiniz..")

    elif(average >= 80 and average <= 100):
        print("Ortalamanız: ", average, "Harf notunuz: AA, Geçtiniz..")

    else:
        print("Hatalı giriş yaptınız.. ")

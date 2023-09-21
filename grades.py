
midterm = int(input("Vize notunuzu giriniz: "))
final = int(input("Final notunuzu giriniz: "))

average = midterm*0.4 + final*0.6

if(average <= 49):
    print("Ortalamanız: ", average, "Harf notunuz: FF")

elif(average >= 50 and average <= 59):
    print("Ortalamanız: ", average, "Harf notunuz: DD")

elif(average >= 60 and average <= 69):
    print("Ortalamanız: ", average, "Harf notunuz: CC")

elif(average >= 70 and average <= 79):
    print("Ortalamanız: ", average, "Harf notunuz: BB")

elif(average >= 80 and average <= 100):
    print("Ortalamanız: ", average, "Harf notunuz: AA")

else:
    print("Hatalı giriş yaptınız.. ")
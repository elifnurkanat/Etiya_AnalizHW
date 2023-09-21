number = int(input("Sayi Giriniz:"))
sum =0
 
for i in range(1,number):

    if(number%i == 0):

        sum +=i
        
if(number == sum):
    print("Mükemmel Sayidir.")
else:
    print("Mükemmel Sayi Degildir")
from random import randint


print("===== Loop Lab: Interaktiv Topshiriqlar =====")
print("1. 🎯 Maxfiy sonni toping (Random son o‘yini)")
print("2. 🔄 So‘zni teskari yozish")
print("3. 🔢 Sonlar orasidagi eng kichigini topish")
print("4. 🧮 FizzBuzz o‘yini (1 dan N gacha)")
print("0. ❌ Dasturdan chiqish")
print("=============================================")

num = int(input("Tanlang: "))
if 0 <= num <= 4 :
    if num == 1:
        print("1. 🎯 Maxfiy sonni toping")
        numR = randint(1,21)
        a = 0
        while a < 5 :
            num1 = int(input("son kiriting: "))
            if 1<= num1 <=20 :
                if num1 == numR :
                    print("topdingiz")
                    break
                elif num1 > numR :
                    print("siz o'ylagan son katta")
                    a +=1
                else:
                    print("siz oylagan juda kichik")
                    a+=1
            else:
                print("1-20 oraliqda son kiriting")    
        else:
            print("urinishlar soni tugadi")
    
    elif num == 2:
        text = input("matnni kiriting: ")
        a = ""
        for i in text:
            a = i + a
        print(a)
    elif num == 3 :
        for i in range(1,6):
            min = int(input(f"{i} sonni kiriting: "))
            if i == 1:
                a = min
            if a > min:
                a = min
        print(a)
    elif num == 4:
        son1 = int(input("sonni kiriitng: "))
        
        for i in range(1,son1+1):
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            elif i % 3 == 0 :
                print("Fizz")
            elif i % 5 == 0 :
                print("Buzz")
            else:
                print(i)
    elif num == 0 :
        print("Dastur yakkunlandi. Xayr")
    
    
    else:
        print("butun son kitiring.") 
    
 
else:
    print("1-4 oraligida raqam kiriting")   
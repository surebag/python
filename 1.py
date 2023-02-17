op_count = float(input("Введите количество операций: ")) 
num1 = float(input("Введите число: ")) 
count = num1 
num2 = 0 
i=1
print("Выберите операцию:") 
print("1.Сложение") 
print("2.Вычитание") 
print("3.Умножение") 
print("4.Деление") 
print("5.Возведение в степень") 
print("6.Остаток от деления")

choice = input("Выбор (1/2/3/4/5/6): ")

num1 = int(input("Введите первоe число: ")) 
num2 = int(input("Ввeдитe второe число: "))
while i!= op_count: 
    if choice == '1': 
        print(num1,"+",num2,"=", print(count=num1+num2))

    elif choice == '2':      print ( num1 , "-" , num2 , "=" , print(count=num1 - num2 ) )
    elif choice == '3':   print(num1,"*",num2,"=", (count=num1*num2))
    elif choice == '4':   
            if num2==0:
      
                    print("делить на 0 нельзя")
            if num2>0:print(num1,"/",num2,"=", (num1/num2))

    elif choice == '5':   print ( num1 , "^" , num2 , "=" ,  ( num1 ** num2 ) )

    elif choice == '6':  

        print ( num1 , "%" , num2 , "=" , ( num1 % num2 ) )
i+=1
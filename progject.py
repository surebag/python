op_count = float(input("Введите количество операций: ")) 
num1 = float(input("Введите число: ")) 
count = num1 
num2 = 0 
i=1



while i == op_count:
    print("Выберите операцию:") 
print("1.Сложение") 
print("2.Вычитание") 
print("3.Умножение") 
print("4.Деление") 
print("5.Возведение в степень") 
print("6.Остаток от деления")

choice = input("Выбор (1/2/3/4/5/6): ")
num2 = float(input("Ввeдитe второe число: "))
if choice == '1': 
        count=count+num2
        print(count)
else:
        if choice == '2':   
            count=count- num2  
            print(count)
        else:
            if choice == '3':   
                count=count*num2
                print(count)
            else:
                if choice == '4':   
                    if num2==0:
      
                        print("делить на 0 нельзя")
                    else:
                        if num2>0:
                            count=count/num2
                            print(count)
                        else:
                            if choice == '5':   count=count* num2  
                    print(count)
                elif choice == '6':  

                    count=count % num2
                    print(count)
i+=1
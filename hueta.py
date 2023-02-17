op_count = float(input("Введите количество операций: ")) 
 
num1 = float(input("Введите число: ")) 
count = num1 
num2 = 0 
i = 1 
 
while i != op_count: 
    symbol = input("Введите символ: ") 
    num2 = float(input("Введите второе число: ")) 
    if (symbol == "+"): 
        count = count + num2 
        print(count) 
    else: 
        if (symbol == "-"): 
            count = count - num2 
            print(count) 
        else: 
            if (symbol == "*"): 
                count = count * num2 
                print(count) 
            else: 
                if (symbol == "/"): 
                    if (num2 == 0 or num1 == 0 and symbol == "/"): 
                                print("На ноль делить нельзя!!!") 
                    else: 
                        count = count / num2 
                        print(count) 
                else: 
                    if (symbol == "^"): 
                        count = count ** num2 
                        print(count) 
                    else: 
                        if (symbol == "%"): 
                            count = count % num2 
                            print(count) 
i+=1 
return             
 
# if (symbol=="+"): 
#     count = num1 
#     while i < op_count: 
#         num2 = int(input("Введите второе число: ")) 
#         count = count + num2 
#         print(count) 
#         i += 1 
# else: 
#     if(symbol=="-"): 
#         count = num1 
#         while i < op_count: 
#             num2 = int(input("Введите второе число: ")) 
#             count = count - num2 
#             print(count) 
#             i += 1 
#     else: 
#         if(symbol=="*"): 
#             count = num1 
#             while i < op_count: 
#                 num2 = int(input("Введите второе число: ")) 
#                 count = count * num2 
#                 print(count) 
#                 i += 1 
#         else: 
#             if(symbol=="/"): 
#                 count = num1 
#                 while i < op_count: 
#                     num2 = int(input("Введите второе число: ")) 
#                     count = count / num2 
#                     print(count) 
#                     i += 1 
#             else: 
#                 if(symbol=="^"): 
#                     count = num1 
#                     while i < op_count: 
#                         num2 = int(input("Введите второе число: ")) 
#                         count = count ** num2 
#                         print(count) 
#                         i += 1 
#                 else: 
#                     if(symbol=="%"): 
#                         count = num1 
#                         while i < op_count: 
#                             num2 = int(input("Введите второе число: ")) 
#                             count = count % num2 
#                             print(count) 
#                             i += 1
year = int(input("Введите год: "))


if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    leap_year = True
else:
    leap_year = False
 

month_days = {1:172, 2:154, 3:172, 4:168, 5:172, 6:168, 7:172, 8:172, 9:168, 10:172, 11:168, 12:172}
 

if leap_year == True and month_days[2] == 154 : month_days[2] += 11   # month_days[2] = 29 if leap_year else 28   

    
total_days = sum(month_days.values())     


print("В {}-м году {}-дат".format(year , total_days))
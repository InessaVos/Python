# -*- coding: utf-8 -*-
#eason=list(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
month = int(input ("Введите месяц от 1 до 12 цифрой: "))
if month == 1 or month == 2 or month == 12:
    print ("зима")
elif month == 3 or month == 4 or month == 5:
    print ("весна")
elif month == 6 or month == 7 or month == 8:
    print ("лето")
else:
    print ("осень")


#season=dict("winter": 12, 1, 2; "spring": 3, 4, 5; "summer": 6, 7, 8; "autumn": 9, 10, 11)
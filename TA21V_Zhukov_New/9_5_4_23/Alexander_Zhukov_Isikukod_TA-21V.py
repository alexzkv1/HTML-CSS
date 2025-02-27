#Alexander Zhukov TA-21V

import datetime 
isik = input("Введите свой исикукод: ")
n = 0
inp = [(i) for i in isik]

shet = 0
pp = ''
if inp[0] == '5':
    pp += '20'
elif inp[0] == '6':
    pp += '20'
elif inp[0] == "4":
    pp += '19'
elif inp[0] == "3":
    pp += '19'
elif inp[0] == "2":
    pp += '18'
elif inp[0] == "1":
    pp += '18'
     
pp += inp[1]
pp += inp[2]

mon = str(inp[5]) + str(inp[6])
#проверка на длину
if len(inp) > 11:
    print("Чисел больше чем 11!")
    shet += 1
if len(inp) < 11:
    print('Чисел меньше чем 11!')
    shet += 1
#проверка первых чисел
if len(inp) == 11 and inp[1]== '1' or '2' or '3' or '4' or '5' or '6':
    if int(inp[0]) > 6 or int(inp[0]) < 1:
        print("Ошибка в написании первых чисел!")
        shet += 1
#определение века
if len(inp) == 11:
    if inp[0] == '5':
        n = 20
    if inp[0] == '6':
        n = 20
    if inp[0] == "4":
        n = 19
    if inp[0] == "3":
        n = 19
    if inp[0] == "2":
        n = 18
    if inp[0] == "1":
        n = 18
#проверка года
nt = datetime.datetime.now()
ntt = nt.year
nd = str(n) + str(inp[1]) + str(inp[2])
if str(nd) > str(ntt):
    print("Ошибка в написании года!")
    shet += 1


if len(inp) == 11:
#проверка на дату
    if  int(mon) > 31 or int(mon) < 1:
        print("Неккоректная дата!")
        shet += 1

#вычисление месяца
if len(inp) == 11:
    ng = str(inp[3]) + str(inp[4])
    if ng > str(12):
        print("Ошибка в написании месяца!")
        shet += 1

#проверка на високосный год
    if ng == "02":
        if pp != 1700 and 1800 and 1900 and 2100 and 2200 and 2300:
            if int(pp) % 4 == 0 and int(pp) % 100 != 0 or int(pp) % 400 == 0:
                if int(mon) != 29:
                    print('В феврале не может быть 30 дней!')
                    shet += 1
        else:
            True
            
#метод вычиселния 11 числа
#сверение последнего числа с суммой
if len(inp) == 11:
    met = int(inp[0]) * 1 + int(inp[1]) * 2 + int(inp[2]) *3 + int(inp[3]) * 4 + int(inp[4]) * 5 + int(inp[5]) * 6 + int(inp[6]) * 7 + int(inp[7]) * 8 + int(inp[8]) * 9 + int(inp[9]) * 1
    met1 = met / 11
    met2 = met - int(met1) * 11
    if int(inp[-1]) > met2 or int(inp[-1]) < met2:
        print("Послднее число не совпадает с методом!")
        shet += 1

if shet == 0:
    print('Ваш иссикукод подлинный!')
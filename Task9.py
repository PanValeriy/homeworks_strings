nomer_kvytka = input('Введіть номер квитка (6зн)= ')
x = int(nomer_kvytka[0]) + int(nomer_kvytka[1]) + int(nomer_kvytka[2])
y = int(nomer_kvytka[3]) + int(nomer_kvytka[4]) + int(nomer_kvytka[5])
if x==y:
    print('Вітаю у Вас Щасливий квиток')
else:
    print('Вам не пощастило')

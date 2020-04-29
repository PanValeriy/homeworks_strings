nomerKvytka = input('Введіть номер квитка (6зн)= ')
x = int(nomerKvytka[0]) + int(nomerKvytka[1]) + int(nomerKvytka[2])
y = int(nomerKvytka[3]) + int(nomerKvytka[4]) + int(nomerKvytka[5])
if x==y:
    print('Вітаю у Вас Щасливий квиток')
else:
    print('Вам не пощастило')

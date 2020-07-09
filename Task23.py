"""В строке найдите все серии подряд идущих пробелов и замените каждую на один пробел."""


def spaces():
    str = input('Введіть текст: ')

    list_str = str.split()
    newstr = ''
    for el in list_str:
        newstr += (el+" ")
        newstr.rstrip()
    print(newstr)

if __name__ == '__main__':
    spaces()

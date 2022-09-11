print("Ноль в качестве знака завершит работу")
while True:
    s = input("выбери знак +,-,*,/: ")
    if s == '0':
        break
    if s in ('+', '-', '*', '/'):
        x = float(input("x="))
        y = float(input("y="))
        if s == '+':
            print(x+y)
        elif s == '-':
            print(x-y)
        elif s == '*':
            print(x*y)
        elif s == '/':
                print(x/y)
    else:
        print("неверный знак")
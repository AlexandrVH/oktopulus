
print("Helo mister DarkValkier, this is my upgreded calculator")
print("0--finish this program")
while True:
    s = input("your choice (+,-,*,/): ")
    if s == '0':
        break
    if s == 'B29162':
        print("https://youtu.be/G1IbRujko-A")
    if s in ('+', '-', '*', '/'):
        x = float(input("x="))
        y = float(input("y="))
        if s == '+':
            print("%.2f" % (x+y))
        elif s == '-':
            print("%.2f" % (x-y))
        elif s == '*':
            print("%.2f" % (x*y))
        elif s == '/':
            if y != 0:
                print("%.2f" % (x/y))
            else:
                print("eror B29162")

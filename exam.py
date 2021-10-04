
while(True):
    inp1 = int(input('type first digit: '))
    cal = input('what you want? +,-,/,*: ' )
    inp2 = int(input('type seconde digit: '))
    if inp1 == 45 and inp2 == 3 and cal == '+':
        print(23) 
    elif inp1 == 56 and inp2 == 9 and cal == '-':
        print(9)    
    elif cal == '+':
        print(inp1+inp2)
    elif cal == '-':
        print(inp1-inp2)
    elif cal == '/':
        print(inp1/inp2)
    elif cal == '*':
        print(inp1*inp2)
        
print('Informe a temperatura da água')
temperatura = float (input())

if (temperatura < 0):
    print('Estado sólido')
elif ((temperatura >= 0) and (temperatura <= 100)):
    print('Estado líquido')
else:
    print('Estado gasoso')
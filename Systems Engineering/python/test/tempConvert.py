# tempConvert.py
tempStr = input('Enter signed temperature value:')
if tempStr[-1] in ['F', 'f']:
    C = (eval(tempStr[0:-1]) - 32) / 1.8
    print('Temperature value is {:.2f}C'.format(C))
elif tempStr[-1] in ['C', 'c']:
    F = 1.8 * eval(tempStr[0:-1]) + 32
    print('Temperature value is {:.2f}F'.format(F))
else:
    print('Temperature input format error')
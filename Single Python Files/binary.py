i = int(input('From which decimal number do you want to start?\n'))
c = int(input('Which decimal number do you want to end with?\n'))
q = ''
print('\n')

while i < c+1:
    j=format(i, '1b')
    j= str(j)
    if j.count('') ==2:
        q = ''

    if j.count('') ==3:
        q = ''

    if j.count('') ==4:
        q = ''

    if j.count('') ==5:
        q = ''

    if j.count('') ==6:
        q = ''

    if j.count('') ==7:
        q = ''

    if j.count('') ==8:
        q = ''

    if j.count('') ==9:
        q = ''
    
    w = str(i)

    if w.count('') ==2:
        a = '               '

    if w.count('') ==3:
        a = '             '

    if w.count('') ==4:
        a = '           '

    if w.count('') ==5:
        a = '         '

    if w.count('') ==6:
        a = '       '

    if w.count('') ==7:
        a = '     '

    if w.count('') ==8:
        a = '   '

    if w.count('') ==9:
        a = ' '
        

    print(i,a, ' =', q, j)
    i=i+1


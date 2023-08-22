#A simple Repeat Loop for copy-pasting into other code

loop = 'Y'
while loop == 'Y' or loop == 'y':
    loop = input('Run Again?(Y/N)\n')

else:
    print('Thank you and Goodbye\n\tCreated by Wrath Lord')
    break

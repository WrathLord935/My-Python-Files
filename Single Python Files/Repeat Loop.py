#A simple Repeat Loop for copy-pasting into other code

h = 'Y'
while h == 'Y' or h == 'y':
    h = input('Run Again?(Y/N)\n')

while h == 'N' or h == 'n':
    print('Thank you and Goodbye\n\tCreated by Wrath Lord')
    break

loop = True

def one_root(root):
    a = 1
    b = -2*root
    c = root*root

    if root >=0:
        print(f'A Quadratic Equation with the root of {root} is {a}x²+{b}x+{c}')
    else:
        print(f'A Quadratic Equation with the root of {root} is {a}x²{b}x+{c}')


def two_root(root1,root2):
    a = 1
    average = (root1*2 + root2*2)/2
    b = -average

    if root1 > root2:
        discriminant = root1*2 - average
    else:
        discriminant = root2*2 - average

    c = ((discriminant**2)-(b**2))/-4

    b = int(b)
    c = int(c)

    if b >= 0:
            print(f'A Quadratic Equation with the roots of {root1} and {root2} is {a}x²+{b}x+{c}')
    else:
        print(f'A Quadratic Equation with the roots of {root1} and {root2} is {a}x²{b}x+{c}')

while loop:
    root_amount = int(input('Does the Quadratic Equation have\n\t1.One root\n\t2.Two roots\n'))

    if root_amount == 1:
        root = int(input('Enter your root: '))
        one_root(root)

    elif root_amount == 2:
        root1 = int(input('Enter your first root: '))
        root2 = int(input('Enter your second root: '))

        if root1 == root2:
            one_root(root1)
        else:
            two_root(root1,root2)
        
    loop = (input(f'Run Again?(Y/N)\n').lower() == "y")

print(f'Thank you and Goodbye\n\tCreated by Wrath Lord')

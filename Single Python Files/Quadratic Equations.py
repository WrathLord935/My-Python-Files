import math

loop = True
final_equation = ''
dash = '-'
underscore = '_'
space = ' '
line_separator = '\n'

def instructions():
  return [line_separator*3,
          '--> Use space before and after + or -',
          '--> Use the standard form of Quadratic Equations (ax2+bx+c)',
          '-->For x square use x2',
          '-->Use 2 negative signs for negative numbers',
          '-->Always put the co-efficient even if its 1',
          '-->Example: 1x2 - -11x + 28',
          line_separator * 2]

def formula():
    return ['The Quadratic Equation is the following:',
             (underscore * 15).rjust(23, space),
             f'-b ± √b² - 4*a*c',
             dash * 23,
             f'2*a'.rjust(12, space),
             line_separator]

def step1(a, b, c):
    return ['1. First we are going to substitute the value of everthing',
             (underscore * 15).rjust(23, space),
             f'-({b}) ± √{b}² - 4 * {a} * {c}',
             dash * 23,
             f'2*{a}'.rjust(12, space),
             line_separator]

def step2(a, b, c, four_ac, b_square):
    return [f'2. Secondly we are going to solve for {b}^2 and 4*{a} * {c}',
             (underscore * 15).rjust(23, space),
             f'-({b}) ± √{b_square} - {four_ac}',
             dash * 23,
             f'2*{a}'.rjust(12, space),
             line_separator]

def step3(a, b, four_ac, b_square, discriminant):
    return [f'3. Now we are going to solve for √{b_square} - {four_ac}',
             (underscore * 15).rjust(23, space),
             f'-({b}) ± √{discriminant}',
             dash * 23,
             f'2*{a}'.rjust(12, space),
             line_separator]

def step4(a, b, discriminant, two_a):
    return [f'4. Now we are going to solve for 2*{a}',
             (underscore * 15).rjust(23, space),
             f'-({b}) ± √{discriminant}',
             dash * 23,
             f'{two_a}'.rjust(12, space),
             line_separator]

def step5(a, b, discriminant_sqrt,discriminant, two_a):
    return [f'5. Then getting the square root of {discriminant}',
             f'-({b}) ± {discriminant_sqrt}',
             dash * 23,
             f'{two_a}'.rjust(12, space),
             line_separator]

def solution1(b, discriminant, two_a, quadratic_eq):
    return [f'The Solution for {quadratic_eq} is the following:',
             (underscore * 5).rjust(13, space),
             f'-({b}) ± √{discriminant}',
             dash * 11,
             f'{two_a}'.rjust(7, space),
             line_separator]

def solution2(b, discriminant_sqrt, two_a, quadratic_eq):
    return [f'The Solution for {quadratic_eq} is the following:',
             f'-({b}) ± {discriminant_sqrt}',
             dash * 11,
             f'{two_a}'.rjust(7, space),
             line_separator]


def print_all(lines):
    for line in lines:
        print(line)

while loop:
  ## Instructions & Input ##
  print_all(instructions())
  raw_equation = input('Input your Quadratic Equation: ')

  ## Extract Variables ##
  equation_subtraction = []
  element_list = raw_equation.split(' + ')
  for element in element_list:
      if dash in element:
          equation_subtraction = element.split(' - ')
          element_list.remove(element)
      final_equation = element_list + equation_subtraction

  for i in final_equation:
    if 'x2' in i:
      a = int(i.replace('x2',''))
    elif 'x' in i:
      b = int(i.replace('x',''))
    else:
      c = int(i.replace('x2',''))

  ## Calculations ##
  four_ac = a*c*4
  b_squared = b**2
  discriminant = b_squared - four_ac
  two_a = 2*a
  if discriminant >= 0:
    discriminant_sqrt = math.sqrt(discriminant)
    is_int = (discriminant_sqrt).is_integer()
    discriminant_sqrt = int(discriminant_sqrt)

  ## Print Steps ##
  print_all(formula())
  print_all(step1(a,b,c))
  print_all(step2(a,b,c,four_ac,b_squared))
  print_all(step3(a,b,four_ac,b_squared,discriminant))
  print_all(step4(a,b,discriminant,two_a))
  if is_int:
      print_all(step5(a,b,discriminant_sqrt,discriminant,two_a))
      print_all(solution2(b,discriminant_sqrt,two_a,raw_equation))
  else:
      print_all(solution1(b,discriminant,two_a,raw_equation))
  
  loop = (input(f'Run Again?(Y/N){line_separator}').lower() == "y")

print(f'Thank you and Goodbye{line_separator}\tCreated by Wrath Lord')

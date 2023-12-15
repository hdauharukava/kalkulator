from kalkulator import integerDivision, multiplication, division
from odejmowanie_pierwiastkowanie import subtraction, root
from Dodawanie import addnumbers, exponentiation

print(f"What do you want to do?\n1.Subtract\n2.Add"
      f"\n3.Multiply\n4.Divide\n5.Integer division\n6.Exponentiation\n7. Square root")

added_number = int(input('Choose one option: '))

print(f"Add your x and y: ")

if added_number == 7:
    x = int(input('Write x: '))
else:
    x = float(input('Write x: '))
    y = float(input('Write y: '))


if added_number == 1:
    print(subtraction(x, y))
elif added_number == 2:
    print(addnumbers(x, y))
elif added_number == 3:
    print(multiplication(x, y))
elif added_number == 4:
    print(division(x, y))
elif added_number == 5:
    print(integerDivision(x, y))
elif added_number == 6:
    print(exponentiation(x,y))
elif added_number == 7:
    print(root(x))

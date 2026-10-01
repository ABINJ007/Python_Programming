
from 2_calculation.addition import add
from 2_calculation.multipliation import multiply
def square_area(side):
    print(multiply(side,side))

def square_perimeter(side):
    print(2*(add(side,side)))

square_area(10)
square_perimeter(20)
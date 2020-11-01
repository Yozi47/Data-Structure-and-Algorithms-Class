# Question no 1 R-2.4

class Flower:
    def __init__(self, petal_name, petal_no, petal_price):
        if not isinstance(petal_name, str):
            raise TypeError("Given name should be string.")
        if not isinstance(petal_no, int):
            raise TypeError("Petal number should be integer.")
        if not isinstance(petal_price, float):
            raise TypeError("Petal price should be float.")

        self.name = petal_name
        self.petals = petal_no
        self.price = petal_price

    def set_name(self, petal_name):
        self.name = petal_name

    def get_name(self):
        return self.name

    def set_no(self, petal_no):
        self.petals = petal_no

    def get_no(self):
        return self.petals

    def set_price(self, petal_price):
        self.price = petal_price

    def get_price(self):
        return self.price

output = Flower("Rose", 12, 4.5)
print("Name: ", output.get_name())
print("Petal no: ", output.get_no())
print("Price: ", output.get_price())


# Question no 2 R-2.13
print()
class Vector(object):  # Used Class code
    def __init__(self, d):
        self._coords = [0] * d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, j):
        try:
            return self._coords[j]
        except IndexError:
            print('The index value {0} exceeds the vector dimension {1}'.format(j, len(self)))

    def __setitem__(self, j, value):
        try:
            self._coords[j] = value
        except IndexError:
            print('The index value {0} exceeds the vector dimension {1}'.format(j, len(self)))

    def __repr__(self):
        return '<' + str(self._coords)[1:-1] + '>'

    def __add__(self, v):
        if len(self) != len(v):
            raise ValueError('Dimension must be equal. Currently {0}!={1}'.format(len(self), len(v)))
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = float('{0:.1}'.format(self[i] + v[i]))
        return result

    def __mul__(self, other):
        if isinstance(other, int):  # Checking for question no 2
            vector = Vector(len(self))
            for i in range(len(self)):
                vector[i] = float("{0:.1f}".format(self[i] * other))
            return vector
        else:  # checking for question no 3
            sum = 0
            for i in range(len(self)):
                sum += float("{0:.1f}".format(self[i] * other[i]))
            return sum

    def __rmul__(self, other):  #
        vector = Vector(len(self))
        for i in range(len(self)):
            vector[i] = float("{0:.1f}".format(other * self[i]))
        return vector

if __name__ == '__main__':
    from random import random
    n = 4
    vector1 = Vector(n)  # Defining a new vector
    for i in range(n):  # Making a random vector
        vector1[i] = float("{0:.1f}".format(random()))
    print("A random vector")
    print(vector1)
    vector2 = (vector1 * 3)
    print("Using the __mul__ for multiplying vector by 3")
    print(vector2)
    print("Using the __rmul__ for multiplying 3 by vector")
    print(3 * vector1)



# Question no 3 R-2.14

# Rest codes are in question no 2
print()
print("The scalar value of dot product is ")
print(vector1 * vector2)  # gives the scalar value of dot product

# Question no 4 R-2.16
print()
print("We compute the number of elements in the range as ")
print("max(0,(stop - start + step -1) // step)")
print("It is worth testing this formula for both positive and negative step sizes.")


# Question no 5 R-2.19
print()
class Progression:
    def __init__(self, start=0):
        self._current = start

    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
        return answer

    def __iter__(self):
        return self

    def print_progression(self, n):
        print(' '.join(str(next(self)) for j in range(n)))

class ArithmeticProgression(Progression):
    def __init__(self, increment=1, start=0):
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        self._current += self._increment

if __name__ == '__main__':
    print('Arithmetic progression with increment 128:')
    ArithmeticProgression(128).print_progression(5)
    print("From above result we found that we can make 3 calls before we reach an integer 263 or larger")
print()

# Question no 6 C-2.28
print()
class CreditCard:
    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._account

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def charge(self, price):
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        self._balance -= amount

class PredatoryCreditCard(CreditCard):
    def __init__(self, customer, bank, acnt, limit,apr):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr
        self.count = 0

    def charge(self, price):
        self.count += 1
        if self.count > 10:
            self._balance += 1
        success = super().charge(price)
        if not success:
            self._balance += 5
        return success

    def process_month(self):
        self.count = 0
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1 / 12)
            self._balance *= monthly_factor

if __name__ == '__main__':
    wallet = []
    wallet.append(PredatoryCreditCard('John Bowman', 'California Savings',
                             '5391 0375 9387 5309', 2500,0.0825))
    wallet.append(PredatoryCreditCard('John Bowman', 'California Federal',
                             '3485 0399 3395 1954', 3500,0.0825))
    wallet.append(PredatoryCreditCard('John Bowman', 'California Finance',
                             '5391 0375 9387 5309', 5000,0.0825))

    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2 * val)
        wallet[2].charge(3 * val)

    for c in range(3):
        print('Customer =', wallet[c].get_customer())
        print('Bank =', wallet[c].get_bank())
        print('Account =', wallet[c].get_account())
        print('Limit =', wallet[c].get_limit())
        print('Balance =', wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print('New balance =', wallet[c].get_balance())
        print()


# Question no 7 C-2.31
print()
class AbsProg(Progression):
    def __init__(self, first=2, last=200):
        super().__init__(first)
        self.diff = first - last

    def _advance(self):
        other = abs(self._current-self.diff)
        self.diff = self._current
        self._current = other

if __name__ == '__main__':
    print('Absolute progression:')
    AbsProg().print_progression(10)

# Question no 8 C-2.32
print()
import math
class sqrProg(Progression):
    def __init__(self, val=65536):
        super().__init__(val)
        self.val = val

    def _advance(self):
        self.val = math.sqrt(self.val)
        self._current = self.val
if __name__ == '__main__':
    print("Square root Progression: ")
    sqrProg().print_progression(10)

# Question no 9 P-2.33
print()
from sympy import *
standard = "3*x**2-12*x+2"  # example for standard algebraic
equation = simplify(standard)
print("The standard algebraic equation: ", standard)
print("The 1st derivative of given equation: ", diff(equation))


# Question no 10 P-2.39
print()
class Polygon():
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def area(self):
        return self.base*self.height

    def perimeter(self):
        return 2(self.base*self.height)

class Triangle(Polygon):
    def __init__(self,base,height):
        super().__init__(base,height)

    def area(self):
        return (1/2)*self.base*self.height


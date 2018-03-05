import sys

class NoIntegerError(ValueError): pass

def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n
    
        m = oldn
        n = oldm % oldn
    return n

class Fraction:
    def __init__(self, top, bottom):
        # Excercise 5 {..
        try:                     
            if type(top) != int or type(bottom) != int: 
                raise NoIntegerError("Top and bottom have to be integers!")
            if bottom < 0:           # Excercise 6
                top = top * (-1)     # Excercise 6
                bottom = bottom * (-1)  # Excercise 6
        except ValueError as err:
            print(err)
            sys.exit(2)
        else:
            self.common = gcd(top, bottom) # Excercise 2
            self.num = top // self.common   # Excercise 2
            self.den = bottom // self.common  # Excercise 2
        # ..} Excercise 5
    
    def __str__(self):
        common = gcd(self.num, self.den)
        return str(self.num // common) + "/" + str(self.den // common)
    
    # Excercise 9 {..
    def __repr__(self):
        class_name = self.__class__.__name__
        common = gcd(self.num, self.den)
        self.num, self.den = (self.num // common), (self.den // common)
        return "{0}({self.num}, {self.den})".format(class_name, **locals())
    # ..} Excercise 9 
    
    def __show__(self):
        print(self.num, "/", self.den)
    
    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + \
                    self.den * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum, newden)  # Excercise 2, ("common" not needed here anymore)
    
    # Excercise 7 {..
    def __radd__(self, otherfraction):
        newnum = otherfraction.num * self.den + \
                    otherfraction.den * self.num
        newden = otherfraction.den * self.den
        return Fraction(newnum, newden)
    # ..} Excercise 7
    
    # Excercise 8 {..
    def __iadd__(self, otherfraction):
        self.num = self.num * otherfraction.den + \
                    self.den * otherfraction.num
        self.den = self.den * otherfraction.den
        return Fraction(self.num, self.den)
    # ..} Excercise 8
    
    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num
        return firstnum == secondnum
        
    def __floordiv__(self, otherfraction):
        newnum = self.num * otherfraction.den
        newden = self.den * otherfraction.num
        return Fraction(newnum, newden)  # Excercise 2, ("common" not needed here anymore)
    
    # Excercise 3 {..
    def __mul__(self, otherfraction):
        newnum = self.num * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum, newden)  # Excercise 2, ("common" not needed here anymore)
    
    def __truediv__(self, otherfraction):
        return self.__floordiv__(otherfraction)
    
    def __sub__(self, otherfraction):
        newnum = self.num * otherfraction.den - \
                    self.den * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum, newden)  # Excercise 2, ("common" not needed here anymore)
    # ..} Excercise 3
        
    # Excercise 4 {..
    def __gt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.num
        return firstnum > secondnum
    
    def __ge__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.num
        return firstnum >= secondnum
    
    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.num
        return firstnum < secondnum
    
    def __le__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.num
        return firstnum <= secondnum
    
    def __ne__(self, other):
        return False if self.__eq__(other) else True
    # ..} Excercise 4
    
    # {.. Excercise 1
    def getNum(self):
        return self.num
    
    def getDen(self):
        return self.den
    # ..} Excercise 1


test = Fraction(2, 3)
print(str(test))
test2 = Fraction(1, 3)
print(str(test2))
print(test.__iadd__(test2))
print(repr(test))
print(str(test))

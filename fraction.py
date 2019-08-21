def gcd(n, d):
    while n != d:
        if n > d:
            n = n - d
        else:
            d = d - n
    return n

class Fraction(object):
    def __init__(self, num, denom):
        
        if isinstance(num, int) == False:
            raise Exception("numerator is not an integer")
            
        if isinstance(denom, int) == False:
            raise Exception("denomerator is not an integer")
            
        self.num = num
        self.denom = denom
        
        self.num = int(num / gcd(abs(num), abs(denom)))
        self.denom = int(denom / gcd(abs(num), abs(denom)))

    def Addition(self, other):
        if self.denom == other.denom:
            return Fraction(self.num + other.num, self.denom)
        else:
            return Fraction(self.num * other.denom + other.num * self.denom, self.denom * other.denom)

    def Subtraction(self, other):
        if self.denom == other.denom:
            return Fraction(self.num - other.num, self.denom)
        else:
            return Fraction(self.num * other.denom - other.num * self.denom, self.denom * other.denom)

    def Multiplication(self, other):
        return Fraction(self.num * other.num, self.denom * other.denom)

    def Division(self, other):
        return self.Multiplication(other.Inverse())

    def Inverse(self):
        return Fraction(self.denom, self.num)

    def Simplify(self):
        num = self.num
        den = self.denom

        self.num = int(num / gcd(abs(num), abs(den)))
        self.denom = int(den / gcd(abs(num), abs(den)))

    def __float__(self):
        return self.num / self.denom

fA = Fraction(1, 4)
fB = Fraction(1, 2)

fC = fA.Division(fB)

fD = fC.Inverse()

print(fC.num,"/",fC.denom)
print(float(fC))

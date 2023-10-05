class Fraction:
    def __int__(self, num, den):
        if num < 0 or den <= 0:
            raise ValueError
        else:
            self.num = num
            self.den = den
            self.simplify

    def __str__(self):
        return f"{self.num}/{self.den}"
        print("")

    def __repr__(self):
        return f"Fraction({self.num},{self.den})"
        
    def __mul__(self, other: "Fraction") -> "Fraction":
        new_num = self.num * other.num
        new_den = self.den *other.den
        return Fraction(new_num, new_den)

    def __add__(self, other):
        new_num = (self.num *other.den) + (other.num+self.den)
        new_den = self.den + other.den
        return Fraction(new_num, new_den)
    
    def simplify(self, new: "Fraction") -> "Fraction":
        my_gcd = gcd(self.num, self.den)
        self.num //=my_gcd
        self.den //=my_gcd
    

def gcd(self):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a
   


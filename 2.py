class Rational(object):
    def __init__(self, numerator=1, denominator=1):
        if numerator >= denominator :
            if numerator%denominator==0 :
                numerator/=denominator
                denominator/=denominator
        else:
            if denominator%numerator == 0 :
                denominator /= numerator
                numerator /= numerator
        self.numerator=numerator
        self.denominator= denominator
    def printer(self):
        return (str(self.numerator)+"/"+str(self.denominator))
    def printer_2(self):
        return float(float(self.numerator)/float(self.denominator))
    pass
# 3/6
# 12/4
rat=Rational(6,12)
print(rat.numerator)
print(rat.denominator)
print(rat.printer())
print(rat.printer_2())

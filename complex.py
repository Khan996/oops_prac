class Complex:

    def __init__(self, real=0.0, imag=0.0):

        self.real = real 
        self.imag = imag 

    def __str__(self):
        if self.real == 0:
            s = f"{self.imag}i"
        elif self.imag < 0:
            s = f"({self.real} {self.imag}i)"
        else:
            s = f"({self.real} + {self.imag}i)"
        return s

    # def conjugate(self):
    #     print(f"{self.real} + {self.imag}")
    

cn = Complex(9, - 5)
# cn.conjuagte()
print(cn)
# print(cn.conjugate())
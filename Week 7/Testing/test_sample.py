import pytest

class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __str__(self):
        if self.imag >= 0:
            return str(self.real) + " + " + str(self.imag) + "i";
        return str(self.real) + " " + str(self.imag) + "i";

def add(x, y):
    return x + y

def test_add():
    assert add(3, 4) == 7

@pytest.mark.skip
def test_add_complex():
    a = Complex(1,1)
    b = Complex(2,3)
    assert a + b == Complex(3, 4)

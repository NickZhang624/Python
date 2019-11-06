#Module Package

# This is a temperature conversion
def c2f(cel):
    fah = cel * 2 + 32
    return fah


def f2c(fah):
    cel = (fah - 32) / 2
    return cel


def test():
    print("test, 0 Celsius = %.2f Fahrenheit" % c2f(0))
    print("test, 0 Fahrenheit = %.2f Celsius" % f2c(0))


# If this is main programme then proceduce function test
# otherwise call others function
if __name__ == "__main__":
    test()

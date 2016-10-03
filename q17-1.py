# First solution attempt
def add(x, y):
    i = 0
    z = 0
    carry = 0
    while x or y or carry:
        # Get ith bits of x and y
        x1 = x % 2
        y1 = y % 2
        # Compute ith bit of z
        z1 = x1 ^ y1 ^ carry | x1 & y1 & carry
        # Compute the carry
        carry = x1 & y1 | x1 & carry | y1 & carry
        # Set ith bit in z
        z |= z1 << i
        # Shift x and y 1 bit
        x >>= 1
        y >>= 1
        # Increment bit counter
        i += 1
    return z

# Better solution
def add2(x, y):
    while y != 0:
        # Add, but don't carry
        sum = x ^ y
        carry = (x & y) << 1
        x = sum
        y = carry
    return x

def test1():
    return add2(153, 182)

def main():
    print test1()

if __name__ == "__main__":
    main()

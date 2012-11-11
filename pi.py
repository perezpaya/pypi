# Using Machin formula
# http://en.literateprograms.org/images/math/7/9/e/79e33327955cad64ea3613b02e7c8e2d.png

def arccot(x, unity):
    sum = xpower = unity // x
    n = 3
    sign = -1
    while 1:
        xpower = xpower // (x*x)
        term = xpower // n
        if not term:
            break
        sum += sign * term
        sign = -sign
        n += 2
    return sum
def pi(digits):
    unity = 10**(digits + 10)
    pi = 4 * (4*arccot(5, unity) - arccot(239, unity))
    return pi // 10**10

digits = raw_input("Number of digits: ")
print pi(int(digits))

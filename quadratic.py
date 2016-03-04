# File: quadratic.py
# A program that uses the quadratic formula to find real roots of a quadratic equation.

def main():
        print "This program finds real roots of a quadratic equation ax^2+bx+c=0."
        a = input("Type in a value for 'a' and press Enter: ")
        b = input("Type in a value for 'b' and press Enter: ")
        c = input("Type in a value for 'c' and press Enter: ")
        d = (b**2.0 - (4.0 * a * c))
        if d < 0:
          print "No real roots"
        else:
          root_1 = (-b + d**0.5) / (2.0 * a)
          root_2 = (-b - d**0.5) / (2.0 * a)
          print "The answers are:", root_1, "and", root_2

        raw_input("Press Enter to exit.")
main()



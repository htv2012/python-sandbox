#!/usr/bin/env python3
import toolz


@toolz.curry
def mul(a, b):
    return a * b


print("\n\nCURRY DEMO")

print("\n# Print a product")
print(f"3 x 7 = {mul(3, 7)}")

print("\n# Curry: like partial function")
forty = mul(40)  # Possible, thanks to curry
print(forty("="))

print("\n# Double a number")
double = mul(2)
print(f"2 x 9 = {double(9)}")

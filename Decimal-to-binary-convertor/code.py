# program that converts Deciamal into binary

divisor = int(input("Enter Decimal: "))
reminder = 0
binary = []
while divisor >= 2: 
    reminder = divisor % 2
    binary.append(reminder)
    divisor = (divisor - reminder)/2
    if divisor < 2:
        binary.append(divisor)

# To reverse the string
binary = binary[::-1]
print(f"Binary Equivalent: ", end='')
for num in binary:
    print(int(num), end='')

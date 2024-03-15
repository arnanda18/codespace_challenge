def square_digits(num):
    # Your code here
    return int(''.join(str(int(d)**2) for d in str(num)))

print(square_digits(9199))
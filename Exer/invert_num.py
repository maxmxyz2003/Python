num1 = int(input())
num_inv = 0
while num1 > 0:
    num_inv = num_inv * 10 + num1 % 10
    num1 //= 10
print(num_inv)

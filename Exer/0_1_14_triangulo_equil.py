num1=int(input())
num2=int(input())
num3=int(input())
num4=int(input())
if num1 == num2 == num3 or num4 == num2 == num3 or num4 == num1 == num3 or num2 == num1 == num4:
    print(1)
else:
    print(0)

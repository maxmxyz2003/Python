num1, num2, num3 = map(int, input().split())
elMayormenoraCien = 0

if elMayormenoraCien < num1 < 100:
    elMayormenoraCien = num1
if elMayormenoraCien < num2 < 100:
    elMayormenoraCien = num2
if elMayormenoraCien < num3 < 100:
    elMayormenoraCien = num3

print(elMayormenoraCien)

"""
    APCS 106/10
    Logic Operator
    20220127
    by Kevin Hsu
"""
iTmp = input("input three number:\n").split()
x = int(iTmp[0])
y = int(iTmp[1])
z = int(iTmp[2])

answer = [0] * 3

if x > 0:
    x = 1
if y > 0:
    y = 1

if ((x & y) == z):
    answer[0] = 1
else:
    answer[0] = 0
    
if ((x | y) == z):
    answer[1] = 1
else:
    answer[1] = 0
    
if ((x ^ y) == z):
    answer[2] = 1
else:
    answer[2] = 0
    
if answer[0] == 1:
    print("AND")
if answer[1] == 1:
    print("OR")
if answer[2] == 1:
    print("XOR")
if answer[0] == 0 and answer[1] == 0 and answer[2] == 0:
    print("IMPOSSIBLE")
a = int(input("Enter the binary number:"))
decimal = a
remainder = 0
binary = []
while (True):
    decimal = decimal//2
    remainder = decimal%2
    binary.append(remainder)
    if decimal==0:
        break

if (a % 2) == 0:
        binary.insert(0, 0)
else:
        binary.insert(0, 1)

print(binary[::-1])





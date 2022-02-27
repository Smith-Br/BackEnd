n = int(input("Type your number:"))
counter_1 = 0

for a in range(n):
    for b in range(n):
        if a > b > 0:
            if a + b == n:
                counter_1 = counter_1 + 1
print(counter_1)

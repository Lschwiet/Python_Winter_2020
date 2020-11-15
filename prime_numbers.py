from random import randint

print("How many prime numbers do you want to know?")
n = int(input())
count = 0
i = 1
print("Okay, here are the first " + str(n) + " prime numbers:")

while count < n:
    i += 1
    for j in range(2, i):
            if i%j == 0:
                break
    else:
        print(i)
        count += 1
        if count == n:
            break

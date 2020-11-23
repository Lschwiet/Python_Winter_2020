"""Exercise - Calculate number of bowls in n rows - RECURSION"""
print("Tell me the largest number of bowls in a row.")
n = int(input())
print("In total, there are this many bowls: ")

"#1"
def sum_bowls(n):   #addrc(n) function was renamed to sum_bowls(n)
    if n == 1:
        return n
    else:
        return n + sum_bowls(n - 1)

print(sum_bowls(n))

"#2 - look in lecture"
n = int(input("enter the number: "))
sum = 0
for num in range(0, n+1. 1)
    sum = sum + num
print ("N", n )
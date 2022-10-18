#This program finds the sum of numbers from 1 to 1000 using a for loop.

def sum():
    num = 1000
    sum = 0
    for i in range(1, num + 1):
        sum = sum + i
    print("The sum is ", sum)

sum()

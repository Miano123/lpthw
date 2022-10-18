#Program to find the sum and average of 5 random numbers from users input.

import random
def main():
    sum = 0
    for count in range(5):
        num = int(input("Please enter the number: "))
        sum = sum + num
    print("Sum of the five numbers is ", sum)
    print("Average of the five numbers is ", sum/5)

main()

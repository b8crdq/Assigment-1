'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

# Task 1
n = int(input())
print(n >= 100)

#Task 2
year = int(input("Please input the year number:"))
print("Common year:", year % 4 != 0)
print("Leap year:", year % 4 == 0)

# Task 3
secret_number = 42  # Replace with the magician's secret number
while True:
    user_guess = int(input("Enter an integer number: "))
    if user_guess == secret_number:
        print("Well done, muggle! You are free now.")
        break
    else:
        print("Ha ha! You're stuck in my loop!")


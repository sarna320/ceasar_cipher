# Write your code below this line 👇
import math
def paint_calc(height,width,cover):
    print(f"You'll need {math.ceil(height*width/cover)} cans of paint.")



# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.   

# 🚨 Don't change the code below 👇
# test_h = int(input()) # Height of wall (m)
# test_w = int(input()) # Width of wall (m)
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)
#-------------------------------------------------------------------------------------------#

# Write your code below this line 👇
def prime_checker(number):
    check=True
    for i in range(2,math.floor(math.sqrt(number))):
        if(number%i==0):
            print("It's not a prime number.")
            check=False
            break
    if check==True:
        print("It's a prime number.")


# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)
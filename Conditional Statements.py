num = int(input("Enter a number = "))
if num > 0:
    print("Your number is positive")
else:
    print("Your number is nagenive")

ac = float(input("please enter the actual product price  = "))
sm = float(input("Enter your sales amount = "))
if ac < sm:
    amount = sm - ac
    print("You profit ",amount ,"taka")
else:
    print("You got no profit !!!")

num15 = int(input("Enter a number = "))
if num15 > 15:
    print("Your number", num15," is greater than 15")
else:
    print("Your number", num15 ," is leas than 15")

number = int(input("Enter a number = "))
if number%2==0:
    print("your number is even")
else:
    print("Your number is odd")

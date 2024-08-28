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

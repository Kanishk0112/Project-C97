import random
Number=random.randint(1,10)
chances=0
print("Guess A Number Between 1 and 100")
while chances<5:
    Guess=int(input("Enter Your Guess"))
    if(Guess==Number):
        print("Congratulations You have Won!!!")
        break
    elif(Guess<Number):
        print("Wrong Guess,Guess a number higher than",Guess)
    else:
        print("Wrong Guess, Guess a number lower than",Guess)
    chances=chances+1
if(not chances<5):
    print("You Lose!!, The Number is",Number)


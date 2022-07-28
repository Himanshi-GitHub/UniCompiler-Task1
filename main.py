import random

print("Enter the range: ")
lower, upper = map(int,input().split('-'))

x = random.randint(lower, upper)

print(f"Guess the no. between {lower} to {upper} - ")
count = 0
points = 100


while (points!=0):
    
    guess = int(input("Guess any No. : "))

    if x == guess:
        print(f"You the correct no. in {count} guesses.")
        print(f"you got {points} points.")
    else:
        points = points - 10
        count = count + 1
        print("Hints:-")
        if x > guess:
            print("Guess a larger number.") 
        else:
            print("Guess a smaller number.")
        
        if(x%2==0):
            print("Number is even.")
        else:
            print("Number is odd.")
        


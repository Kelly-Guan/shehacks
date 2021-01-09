import random

range_min = None #makes more sense to call range_(blank)
range_max = None
user_guess = None 
randNum = None

while type(range_min) is not int:
    range_min = input("What do you want the minimum value to be?: ")  #ask user for min value stores in input_min
    if range_min.isdigit(): #makes sure input is a digit
        range_min = int(range_min) #forces input to be a string
    else:
        print("Error. Only integers are allowed") #if imput not an integer displays...
    
while type(range_max) is not int:
    range_max = input("What do you want the maximum value to be?: ") #ask user for max value stores in input_max
    if range_max.isdigit() and int(range_max)>int(range_min):
        range_max = int(range_max) #forces input to be a string
        break
    elif range_max.isdigit() and int(range_max)<=int(range_min):
        print("Uh Oh! Please enter a max value that is greater than your minimum.") 
    else:
        print("Error. Only integers are allowed") 

print("Your range is:",range_min,"to",range_max) #outputs range for user 

randNum = random.randint(range_min, range_max) #has the program random guess a number!

while type(user_guess) is not int:
    user_guess = input("Guess a number in between your given range: ")  #ask user to guess a number, stores in user_guess
    if user_guess.isdigit(): #makes sure input is a digit
        user_guess = int(user_guess) #forces input to be a string
    else:
        print("Error. Only integers are allowed") #if input is not an integer displays...
    if (int(user_guess) >= int(range_min) and int(user_guess) <= int(range_max)):
        break
        
while int(user_guess) != int(randNum):#makes while loop repeat if user_guess is not randNum
    if int(user_guess) > int(range_max) or int(user_guess) < int(range_min): #makes sure user_guess is inbetween range
        print("This number is out of the set range")
        user_guess = input("Choose a number: ")
        user_guess = int(user_guess)
    elif int(user_guess) > int(randNum): #if user_guess is greater than randNum
        print("Incorrect. The number is lower")
        user_guess = input("Choose a number: ")
        user_guess = int(user_guess)
    elif int(user_guess) < int(randNum): #if user_guess is less than randNum
        print("Incorrect. The number is higher")
        user_guess = input("Choose a number: ")
        user_guess = int(user_guess)
    if user_guess == randNum:#if uses_guess is the randNum
        break #breaks from loop

print("Congratulations! You guessed the number") #outputs uses_guess is the randNum
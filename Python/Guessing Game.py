the_correct_number_is = 9 
i=0
while i<3:
    guess = int(input("Guess the number: "))
    i+=1
    if guess == the_correct_number_is:
        print("You Won!")
        break
else:
    print("You Lose!")
        
        




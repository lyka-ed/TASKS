# Ouestion 1

# Write a program that adds 1000 to a number entered by a user, if the user enters anything less than 1000.

student_score = int(input("Enter your score: "))

if student_score <= 1000:
    print(int(student_score + 1000))
else:
    print("ERROR")


# Ouestion 2

""" Design a program to check if a drinker is above 18 to drink alcohol.
If the user is less than 18, display "You can't drink alcohol !!!".
If the user is above 18, display "Cheers !!! " """

user_age = int(input("How old are you ? "))

if user_age < 18:
    print("You can't drink alcohol !!!")
elif user_age > 18:
    print("Cheers !!!")    
else:
    print("Welcome to adulthood.")    


# Ouestion 3

""" A program that checks the length of a LIST .
If the list is less than 6, display "It is less than 6.".
If it is equal to 6, display "It is equal to 6.".
If it is greater than 6, display "Now we talking.". """


mammary_gland = ["6th rib", "Retromammary space", "Glandular lobubles", "Cooper's ligament", "P.fascia", "P.muscles"]
x = len(mammary_gland)

if x < 6:
    print("It is less than 6.")
elif x == 6:
    print("It is equal to 6.")
else:
    print("Now we talking.")



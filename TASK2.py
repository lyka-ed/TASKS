# Question 1

# Write a program that adds 1000 to a number entered by a user, if the user enters anything less than 1000

""" student_score = int(input("Enter your score: "))

if student_score <= 1000:
    print(int(student_score+ 1000))
else:
    print("ERROR") """


# Question  2

""" Design a program to check if a drinker is above 18 to drink alcohol.
If the user is less than 18, display " You can't drink alcodol !!! " 
if the user is above 18, dispaly " Cheers!" """
""" 
user_age = int(input("How old are you? "))

if user_age > 18:
    print(f"Cheer!")
elif user_age < 18:
    print("You can't drink alcohol")
else:
    print("Welcome into adulthood")   """      


# Question 3

""" A program that cgecks the length of a LIST.
If the list is less than 6, display "is less than 6"
If it is equal to 6 display "is equal to 6"
If it is greater than 6 display "now we talking" """

mammary_gland = ["6th rib", "Retromammary space", "P.fascia", "P.muscles", "Glandular lobules", "Cooper's Ligament"]
x = len(mammary_gland)

if x < 6:
    print("It's less than 6")
elif x == 6:
    print("it's equal to 6")
else:
    print("Now we're talking")


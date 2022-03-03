# -------------- TASKS INVOLVING FUNCTION -----------
"""
QUESTION 1
Write a fuction that converts Fahrenheit to Celsuis.
"""
# Formula for conversion
# (fahrenheit - 32)/ 1.8 

def fahrenheit():
    fahrenheit = float(input("Enter temperature in fahrenheit: "))
    print(f"{fahrenheit}\N{degree sign}F")
    fahrenheit = (fahrenheit - 32)/ 1.8 
    return fahrenheit

celsuis_temp = fahrenheit()
print(f"The temperature in Celsuis is {celsuis_temp}\N{degree sign}C")


""" 
QUESTION 2
Write a fuction that runs a loop 4 times on the input user enters 
"""

def user_name():
    user_name = input('My name is ')
    for i in range(4):
        print(f'{user_name}')

user_name()    

        
        
""" 
QUESTION 3
Remember the market list loop that allows the user to enter stop to end the loop?
Convert it to a function.
"""
def market_list():
    items_list = []
    for items in range(1,9):
        items = input("Mention item: ")
        if items == 'stop' or items == 'STOP':
            break
        else:
            items_list.append(items)
    print("These are the items you need, thanks")
    return items_list
    
x = market_list() 
print(x)




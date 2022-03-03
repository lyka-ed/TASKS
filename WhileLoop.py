# -----------------------------------------------------
# ------------ USING WHILE LOOP -----------------------

""" 
QUESTION 1
Make the while loop spell out Ifiok as a single letter
"""
name = "Ifiok"
x = 0
print("Ifiok spelt in single letters: ")

while x < len(name):
    print(name[x])
    x = x + 1



""" 
QUESTION 2
Write an app that allows the user to write down market items 
the user should enter 'stop' to stop the app.
When the app is stopped, the app should otput the list of market items. 
"""
market_items = []
x = 0

while x in range(10):
    list = input("Mention market items: ")
    if list.upper() != 'STOP':
        x += 1
        market_items.append(list)
    
    else:
        break
print("Below is your market list")
print(market_items)        


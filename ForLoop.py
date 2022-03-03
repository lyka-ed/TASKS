# ------------------ FOR LOOP ------------------

""" 
QUESTION 1
Make the while loop spell out Ifiok as a single letter 
"""
name = "ifiok"
print("Ifiok spelt in single letters: ")

for a in name:
    print(a)

"""
QUESTION 2
Write an app that allows the user to write down market items 
the user should enter 'stop' to stop the app.
When the app is stopped, the app should otput the list of market items. 
"""

market_items = []

for items in range(1,7):
    items = input("Enter items or stop to exist: ")

    if items == "STOP" or items == "stop" :
        break
    else:
        market_items.append(items)
print("These are items you need, thanks. ") 
print(market_items)       


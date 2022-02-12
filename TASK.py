# ------** ## TASKS ## **------ 

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(car.items())

# using get() to print model of car
x_model = car.get("model")
print(x_model)

""" Question 3
Create a dictionary that holds information of a user profile on twitter """

user_info= {
    "Name": "Lyka Ed",
    "Username": "@ibibionerdygirl",
    "Bio": "Anatomist| Community Moderator(MOD)",
    "Location": "Beside You",
    "D.O.B": "11th August",
    "Website": None,
    "Following": 1088,
    "Follower": 255,
}   
for key, value in user_info.items():
    print(f"{key} : {value}")
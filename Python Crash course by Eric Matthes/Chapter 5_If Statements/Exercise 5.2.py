food = "rice"
print(f"Is He eating {food.lower()}?")
print(food == "rice")

print(f"\nWhat about John? Is He eating {food.lower()}?")
print(food == "beans")

my_food = "Pizza"
print(f"\nOk then, right now I'd like to have some {my_food.lower()}. Do you have any?")
print(my_food.lower() == "pasta")

my_food = "Pasta"
print(f"\nWhat about {my_food.lower()}? Do you have any?")
print(my_food.lower() == "pasta")

age = 17
print(f"\nI would like some beer with that but I'm 17 years old. Can I have some?")
print(age >= 18)

print(f"\nWhat about iced juice. Am I old enough to have some juice?")
print(age >= 3)

friend_food = "Burger"
friend_age = 20
print(f"\nHey is he ordering the same dish as me?")
print(friend_food.lower() == my_food.lower() and friend_age >= 18)

print(f"\nIs he ordering anything at all I'm ordering?")
print(friend_food.lower() == my_food.lower() or friend_age <= 18)

print(f"\nIs he ordering a completely different meal combo?")
print(friend_food.lower() != my_food.lower() and friend_age >= 18)

print(f"\nIs he allowed to drink beer?")
print(friend_food.lower() == my_food.lower() or friend_age >= 18)


toys = ["car", "truck", "doll", "puzzle", "teddy bear"]
print("\nIs 'bike' in my toy collection?")
print("bike" in toys)

print("\nIs 'doll' in my toy collection?")
print("doll" in toys)

print("\nIs 'video game' not in my toy collection?")
print("video game" not in toys)

print("\nIs 'puzzle' not in my toy collection?")
print("puzzle" not in toys)



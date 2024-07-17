import random
import abc
songs: list[str] = ["Watch the world burn", "Too sweet", "I am the antichrist to you"]
print (songs)

songs.append("Houdini")
print (songs)

songs.insert(0, "Ride")
print (songs)

numbers: list[int] = []
for i in range (1, 11):
    numbers.append(random.randint (1, 9999))
print (numbers)

bool_values: [bool] = []
for _ in range (1, 11):
    bool_values.append (random.choice([True , False]))
print (bool_values)

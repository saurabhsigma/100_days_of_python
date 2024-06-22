import random

mydict = {
    "Shakira: a musician from Barbados" :  500,
    "Neymar: a footballer from Brazil" : 1000,
    "Akshay kumar: A film star from India" : 1200,
    "Lionel Messi: A footballer from Argentina" : 2000
}

choices = list(mydict.keys())  # Convert dictionary keys to a list for random sampling
votes = list(mydict.values())

x, y = random.sample(choices, 2)  # Randomly select two items from the list of choices

print("Welcome to the game!!!")
print("You are given with two options to choose from")
print("\n\n", x)
print("\n\n\n", y)
print("\n\n ")

# imports random module
import random

# array of the different possible cards
cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

# determine card values
card_values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 10, "King": 10}

# gets first two player cards
card_1 = cards[random.randint(0, 12)]
card_2 = cards[random.randint(0, 12)]

# tells player what their cards are
print(card_1)
print(card_2)

# deals with Ace
if card_1 == "Ace" or card_2 == "Ace":
    user_choice = input("Would you like the value to be 1 or 11?: ")
    if user_choice == 1:
        card_values["Ace"] = 1
    if user_choice == 11:
        card_values["Ace"] = 11

# sum of the values
sum = card_values[card_1] + card_values[card_2]

# outcome if sum is less than 21
while sum < 21:
    user_choice = input("Would you like to hit or pass?: ")
    if user_choice == "hit":
        card = cards[random.randint(0, 12)]
        print(card)
        if card == "Ace":
            user_choice = input("Would you like the value to be 1 or 11?: ")
            if user_choice == 1:
                sum += 1
            if user_choice == 11:
                sum += 11
        sum += card_values[card]
    if user_choice == "pass":
        print("You ended your turn.")

# if sum is 21
if sum == 21:
    print("Congratulations! You won!")
    
# if sum goes over 21
if sum > 21:
    print("You busted! Try again.")

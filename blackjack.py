# imports random module
import random

# array of the different possible cards
cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

# determine card values
card_values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 10, "King": 10}

# gets first two player cards
card_1 = cards[random.randint(0, 12)]
card_2 = cards[random.randint(0, 12)]

# get first two dealer cards
dealer_card_1 = cards[random.randint(0, 12)]
dealer_card_2 = cards[random.randint(0, 12)]

# tells player what their cards are
print("Your first card: " + card_1)
print("Your second card: " + card_2)

#says what one of the dealer's cards are
print("Dealer's first card: " + dealer_card_1)

# if the first card is Ace
if card_1 == "Ace":
    user_choice = input("Would you like the value to be 1 or 11?: ")
    if user_choice == "1":
        card_values["Ace"] = 1
    if user_choice == "11":
        card_values["Ace"] = 11

if dealer_card_1 == "Ace":
    choice = random.randint(1, 2)
    if choice == 1:
        card_values["Ace"] = 1
    if choice == 2:
        card_values["Ace"] = 11

# start the sums of the cards
player_sum = card_values[card_1]
dealer_sum = card_values[dealer_card_1]

#if the second card is Ace
if card_2 == "Ace":
    user_choice = input("Would you like the value to be 1 or 11?: ")
    if user_choice == "1":
        card_values["Ace"] = 1
    if user_choice == "11":
        card_values["Ace"] = 11

if dealer_card_2 == "Ace":
    choice = random.randint(1, 2)
    if choice == 1:
        card_values["Ace"] = 1
    if choice == 2:
        card_values["Ace"] = 11

# update the sums
player_sum += card_values[card_2]
dealer_sum += card_values[dealer_card_2]

# outcome if sum is less than 21
while player_sum < 21:
    user_choice = input("Would you like to hit or pass?: ")
    if user_choice == "hit":
        card = cards[random.randint(0, 12)]
        print("Your next card is: " + card)
        if card == "Ace":
            user_choice = input("Would you like the value to be 1 or 11?: ")
            if user_choice == "1":
                card_values["Ace"] = 1
            if user_choice == "11":
                card_values["Ace"] = 11
        player_sum += card_values[card]
    if user_choice == "pass":
        print("Your total is: " + str(player_sum))
        break

# if player sum is over 21
if player_sum > 21:
    print("Your total is: " + str(player_sum))
    print("You busted! Try again.")
    exit()

# start dealer's turn
print("Dealer's second card: " + dealer_card_2)

# if dealer sum is not 21
while dealer_sum < 21:
    choice = random.randint(1, 2)
    if choice == 1:
        dealer_choice = "hit"
        if dealer_choice == "hit":
            card = cards[random.randint(0, 12)]
            print("Dealer's next card is: " + card)
            if card == "Ace":
                choice = random.randint(1, 2)
                if choice == 1:
                    card_values["Ace"] = 1
                if choice == 2:
                    card_values["Ace"] = 11
            dealer_sum += card_values[card]
    if choice == 2:
        dealer_choice = "pass"
        if dealer_choice == "pass":
            print("Dealer's total is: " + str(dealer_sum))
            break

# if both sums are 21
if player_sum == 21 and dealer_sum == 21:
    print("Game is a tie!")

# if dealer sum is 21 and player sum is not
if dealer_sum == 21 and sum != 21:
    print("The dealer wins. Try again.")

# if dealer sum is over 21
if dealer_sum > 21:
    print("Dealer's total is: " + str(dealer_sum))
    print("The dealer has busted. You win!")

# if player's sum is higher than the dealer's
if player_sum > dealer_sum and player_sum < 21:
    print("Congratulations! You win!")
# if dealer's sum is higher than player's
if dealer_sum > player_sum and dealer_sum < 21:
    print("The dealer has won. Try again.")

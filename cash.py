from cs50 import get_float


# Ask user for input


while True:
    coins = get_float("How much change is needed? ")
    if coins > 0.00:
        break

change = round(coins * 100)

count = 0

# subract quarters
while change > 0:
    if change >= 25:
        change -= 25
        count += 1

    # subtract dimes
    elif change >= 10:
        change -= 10
        count += 1

    # subtract nickels
    elif change >= 5:
        change -= 5
        count += 1

    # subtract cents
    else:
        change -= 1
        count += 1

# total number of coins needed:
print(count, "coins needed. ")


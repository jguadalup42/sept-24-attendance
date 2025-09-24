import random

# Get the user's name
varUserName = input("Hello! What's your name? ")

# Greet the user
print(f"Hey there, {varUserName}! Let's generate some lucky PowerBall numbers for you.")

# Generate the first five numbers (white balls)
# These numbers should be unique and between 1 and 69
white_balls = sorted(random.sample(range(1, 70), 5))

# Generate the last number (red Powerball)
powerball = random.randint(1, 26)

# Print the numbers with the specified spacing
# The `*` unpacks the list so each number is a separate argument to print
print("\nYour PowerBall numbers are:")
print(*white_balls, sep="  ", end="")
print("    ", powerball)

# Provide a farewell message
print(f"\nGood luck with the lottery, {varUserName}!")
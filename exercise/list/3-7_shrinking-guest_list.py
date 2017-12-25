# Make a guest list and print a message to each persons

guests = ['Dave','Ryan','Patrick','Bob']

print("Dear " + guests[0] + " you have been invited to the dinner party.")
print("Dear " + guests[1] + " you have been invited to the dinner party.")
print("Dear " + guests[2] + " you have been invited to the dinner party.")
print("Dear " + guests[3] + " you have been invited to the dinner party.")

# Print message about smaller table

print("Unfortunately, we reserved a smaller dinner table.")

uninvited_guests = []
uninvited_guests.append(guests.pop())
uninvited_guests.append(guests.pop())

# Print message to inform uninvited guests
print("\n")
print("Sorry, " + uninvited_guests[0] + ". We reserved a smaller dinner table.")
print("Sorry, " + uninvited_guests[1] + ". We reserved a smaller dinner table.")

# Print message to inform the guests that are still invited
print("\n")
print("Hello, " + guests[0] + ". You are still invited to the party.")
print("Hello, " + guests[0] + ". You are still invited to the party.")

# Remove the last two guests
del guests[0]
del guests[0]

# Print empty list
print(guests)

# Author: Adomous Wright
# Date: 12/25/17

# Make a guest list and print a message to each persons

guests = ['Dave','Ryan','Patrick','Bob']

print("Dear " + guests[0] + " you have been invited to the dinner party.")
print("Dear " + guests[1] + " you have been invited to the dinner party.")
print("Dear " + guests[2] + " you have been invited to the dinner party.")

# Print message about larger dinner table
print("We found a larger dinner table!")

# Add new people to the beginning, middle, and end of the list
guests.insert(0, 'Dave')
guests.insert(2, 'Tony')
guests.append('Val')

# Print out new invitations
print("Dear " + guests[0] + " you have been invited to the dinner party.")
print("Dear " + guests[1] + " you have been invited to the dinner party.")
print("Dear " + guests[2] + " you have been invited to the dinner party.")
print("Dear " + guests[3] + " you have been invited to the dinner party.")
print("Dear " + guests[4] + " you have been invited to the dinner party.")
print("Dear " + guests[5] + " you have been invited to the dinner party.")

# Author: Adomous Wright
# Date: 12/25/17

# Make a guest list and print a message to each persons

guests = ['Ryan','Patrick','Bob']

print("Dear " + guests[0] + " you have been invited to the dinner party.")
print("Dear " + guests[1] + " you have been invited to the dinner party.")
print("Dear " + guests[2] + " you have been invited to the dinner party.")

# Print the guest that can't make it

print(guests[2] + " will not be able to make it to dinner.")

# Replace that guest with someone who can come

del guests[2]
guests.append('George')

# Print new set of invitations
print("\n")
print("Dear " + guests[0] + " you have been invited to the dinner party.")
print("Dear " + guests[1] + " you have been invited to the dinner party.")
print("Dear " + guests[2] + " you have been invited to the dinner party.")

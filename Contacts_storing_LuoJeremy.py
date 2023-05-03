
#IDLE Open Source
#Note to Viewer: In code
#Jeremy Luo


# import regular expression for the 'match()' function
import re

# Prompt the user for their desired number of contacts
while True:
    number_of_contacts = input("How many contacts would you like to add? ")
    # inputs can only be valid if it is greater than 0
    if not number_of_contacts.isdigit() or int(number_of_contacts) < 1:
        print("Invalid, please try again")
    else:
        number_of_contacts = int(number_of_contacts)
        break

# Initialize lists to store contact names and emails
names = []
emails = []

# Loop through each contact and prompt for name and email
for i in range(number_of_contacts):
    while True:
        name = input(f"Please enter the name of contact {i+1}: ")
        # mark it valid if it is the full first and last name and contains only letters
        if not re.match(r'^[A-Za-z]+\s[A-Za-z]+$', name):
            print("Invalid, please try again")
        else:
            break
    names.append(name)

    while True:
        email = input(f"Please enter the email of contact {i+1}: ")
        # mark it valid if it contains the '@' sign and ends with a '.com'
        if not re.match(r'^[A-Za-z][A-Za-z0-9]*@[A-Za-z]+\.com$', email):
            print("Invalid, please try again")
        else:
            break
    emails.append(email)

# Print out their list of contacts
print("Thanks! Here is your address book:")
for i in range(number_of_contacts):
    print(f"Name: {names[i]}, Email: {emails[i]}")

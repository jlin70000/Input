
#IDLE Open Source
#Note to Viewer: 
#Jeremy Luo

#input asking for username from user
while True:
    username = input("Enter a username: ")
    
    # check for all the different rules for the username

    if len(username) < 8 or len(username) > 15:
        print("* Length of username: ", len(username))
        print("* All characters are alpha-numeric: ", username.isalnum())
        print("* First & last characters are not digits: ", not (username[0].isdigit() or username[-1].isdigit()))

        #setup variables for lower and uppercase rules
        num_upper = sum(1 for c in username if c.isupper())
        num_lower = sum(1 for c in username if c.islower())
        num_numeric = sum(1 for c in username if c.isdigit())
        print("* # of uppercase characters in the username: ", num_upper)
        print("* # of lowercase characters in the username: ", num_lower)
        print("* # of digits in the username: ", num_numeric)
        print("Username is invalid, please try again")
    # if the username is not valid, we still want to print out the rules
    else:
        print("* Length of username: ", len(username))
        print("* All characters are alpha-numeric: ", username.isalnum())
        print("* First & last characters are not digits: ", not (username[0].isdigit() or username[-1].isdigit()))
        num_upper = sum(1 for c in username if c.isupper())
        num_lower = sum(1 for c in username if c.islower())
        num_numeric = sum(1 for c in username if c.isdigit())
    
        print("* # of uppercase characters in the username: ", num_upper)
        print("* # of lowercase characters in the username: ", num_lower)
        print("* # of digits in the username: ", num_numeric)

        #check to see if the username actually abides by the username rule and print
        if not (username.isalnum() and not (username[0].isdigit() or username[-1].isdigit())
                and any(c.isupper() for c in username) and any(c.islower() for c in username)
                and any(c.isdigit() for c in username)):
            print("Username is invalid, please try again.")
        
        else:
            print("Username is valid.!")
            break

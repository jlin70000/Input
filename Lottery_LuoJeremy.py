#IDLE Open Source
#Note to Viewer: 
#Jeremy Luo


#ask the user questions about the lottery winning
total = int(input("How much money did you win?"))
people = int(input("How many people are splitting the winnings?"))
tax_rate  = int(input("What is the tax rate?"))

#get money variables for printing
money_per_person = total / people
tax_per_person = money_per_person * tax_rate/100
take_home_per_person = money_per_person - tax_per_person

#format the variables for printing (dollar signs, decimal places, and make sure to make new variables)
total_format = '$' + format(total, ',.2f')
money_per_person_format = '$' + format(money_per_person, ',.2f')
tax_per_person_format = '$' + format(tax_per_person, ',.2f')
take_home_per_person_format = '$' + format(take_home_per_person, ',.2f')


#print out info for user
print('In total you have won:', total_format)
print('Split', people, 'ways, that amounts to:', money_per_person_format)
print('Tax per person:', tax_per_person_format)
print('Take home per person:', take_home_per_person_format)



      


#IDLE Open Source
#Note to Viewer: Be sure to press enter after putting in your values. Typing in a four digit value will result in error. 
#Jeremy Luo



first_number = int(input('Enter a number between 0 and 999:'))
second_number = int(input('Enter another number between 0 and 999:'))

i = 3                    

sum_of_ones = int(str(first_number)[i-1]) + int(str(second_number)[i-1])
product_of_tens = int(str(first_number)[i-2]) * int(str(second_number)[i-2])
difference_of_hundreds = int(str(first_number)[i-3]) - int(str(second_number)[i-3])

print('Sum of ones =', '  ', int(str(first_number)[i-1]), '+', int(str(second_number)[i-1]), '=', sum_of_ones)
print('Prodcut of tens =', '  ', int(str(first_number)[i-2]), '*', int(str(second_number)[i-2]), '=', product_of_tens)
print('Difference of hundreds =', int(str(first_number)[i-3]), '-', int(str(second_number)[i-3]), '=', difference_of_hundreds)

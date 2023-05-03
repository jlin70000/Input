#IDLE Open Source
#Note to Viewer: In code



# Accept user input
budget = float(input("Enter budget for your party: "))
cost_per_slice = float(input("Cost per slice of pizza: "))
cost_per_pie = float(input("Cost per whole pizza pie (8 slices): "))
num_people = int(input("How many people will be attending your party? "))

# Calculate total number of slices needed
total_slices = 0
for i in range(num_people):
    while True:
        num_slices = int(input("Enter number of slices for person #{}: ".format(i+1)))
        if num_slices < 0:
            print("Not a valid entry, try again!")
        else:
            total_slices += num_slices
            break

# Calculate number of pies and individual slices needed
num_pies = total_slices // 8
num_slices_leftover = total_slices % 8

# Calculate cost
cost = num_pies * cost_per_pie + num_slices_leftover * cost_per_slice

# Check if cost exceeds budget and output result and print appropriate outputs
if cost <= budget:
    print("You should purchase {} pies and {} slices".format(num_pies, num_slices_leftover))
    print("Your total cost will be: {:.2f}".format(cost))
    print("You will still have {:.2f} left after your order".format(budget-cost))
else:
    print("Your order cannot be completed.")
    print("You would need to purchase {} pies and {} slices".format(num_pies, num_slices_leftover))
    print("This would put you over budget by {:.2f}".format(cost - budget))

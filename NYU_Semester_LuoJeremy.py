#IDLE Open Source
#Note to Viewer: Notes given in between functions
#Jeremy Luo


#Ask user for a certain date
date = input("Enter a date in YYYYMMDD format (i.e. 20230219 for February 19th, 2023): ")

#setup the variables with corresponding numbers and its corresponding placement in the 8-digit integer
year = int(date[0:4])
month = int(date[4:6])
day = int(date[6:8])

#setup conditions where date is not an actual date and print 
if month > 12 or day > 31 or (month == 2 and day > 28):
    print("This date is invalid")

#where the date is before semester starts and print
elif date < "20230123":
    print("This date is before the semester begins")

#where the date is after semester ends and print
elif date > "20230508":
    print("This date is after the semester ends")

#where the date is when you have class and print
elif date in "20230123, 20230125, 20230130, 20230201, 20230206, 20230208, 20230213, 20230215, 20230220, 20230222, 20230227, 20230301, 20230306, 20230308, 20230313, 20230315, 202303120, 20230322, 20230327, 20230329, 20230403, 20230405, 202304010, 20230412, 20230417, 20230419, 20230424, 20230426, 20230501, 20230503, 20230508" :
    print("You have class today")

#anything else will be a date when you don't have class and print
else:
    print("You don't have class today")

    

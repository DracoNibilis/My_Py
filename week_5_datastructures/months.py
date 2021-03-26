# months.py
# Program that stores the months of the year (in tuple), 
# from that tuple create another tuple with just the summer months.
# Author: Magdalena Malik

tuple_of_months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October","November","December")
tuple_summer_months = tuple_of_months[4:7]
for month in tuple_summer_months:
    print(month)

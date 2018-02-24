#Homework_number_of_days
#Answer

january = 31
february = 28
march = 31
april = 30
may = 31
june = 30
july = 31
august = 31
september = 30
october = 31
november = 30
december = 31

first_quarter = january + february + march
second_quarter = april + may + june
third_quarter = july + august + september
fourth_quarter = october + november + december

print('The number of days in the first quarter is',first_quarter,
      '\nThe number of days in the second quarter is', second_quarter,
      '\nThe number of days in the third quarter is', third_quarter,
      '\nThe number of days in the fourth quarter is', fourth_quarter)

print('The number of days in the first half of the calendar year is',first_quarter + second_quarter,
      '\nThe number of days in the second half of the calendar year is', third_quarter + fourth_quarter)

print('The number of days in the year is', first_quarter + second_quarter + third_quarter + fourth_quarter)






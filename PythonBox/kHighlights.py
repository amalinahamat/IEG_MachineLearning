import re
number = "987654321"
short = re.match( r'\d{3}', number)
if short:
   print (short.group())
else:
   print ("No short!!")

# i assess

# 1

def date_decoder(date_):

   month_dict = {
   "JAN" : "01",  "FEB" : "02",  "MAR" : "03", "APR" : "04",
   "MAY" : "05",  "JUN" : "06",  "JUL" : "07", "AUG" : "08",
   "SEP" : "09",  "OCT" : "10",  "NOV" : "11", "DEC" : "12"
}
   
   year, month_, day = date_.split("-")

   month = month_dict[month_]

   if int(year) >= 0 and int(year) <= 29:
      full_year = 2000 + int(year)
   elif int(year) >= 30 and int(year) <= 99:
      full_year = 1900 + int(year)

   if(full_year % 4 == 0 and full_year % 100 != 0 or full_year % 400 == 0):
      leap_year_status = "is a leap year"
   else:
      leap_year_status ="is not a leap year"


   return f"({day}, {month}, {full_year}) {leap_year_status}"

date_ = input().strip()

print(date_decoder(date_))

# 2

import math 

def Floor(total_sum):
   return math.floor(total_sum)

def Ceil(total_sum):
   return math.ceil(total_sum)

def Round(total_sum):
   return round(total_sum)

input_user = input().strip().split()

numbers = []
for number in input_user:
   numbers.append(float(number))

total_sum = sum(numbers)

floor_value = Floor(total_sum)
ceil_value = Ceil(total_sum)
round_value = Round(total_sum)

print(f"{(floor_value - ceil_value):.1f}")
print(f"{(ceil_value - round_value):.1f}")
print(f"{(floor_value - round_value):.1f}")


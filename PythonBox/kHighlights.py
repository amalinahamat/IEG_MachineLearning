import re
number = "987654321"
short = re.match( r'\d{3}', number)
if short:
   print (short.group())
else:
   print ("No short!!")
   
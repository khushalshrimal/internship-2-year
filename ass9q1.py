import re
#Email
email = "Khushal@gmail.com"

email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

if re.match(email_pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")

#String 

name = "Khushal"
name1="Khushal14"

string_pattern = r'^[A-Za-z]+$'

if re.match(string_pattern, name):
    print("Valid String")
else:
    print("Invalid String")

if re.match(string_pattern, name1):
    print("Valid String")
else:
    print("Invalid String")

#Mobile no.

mobile = "9876543210"
mobile1="1467836934"

mobile_pattern = r'^[6-9][0-9]{9}$'

if re.match(mobile_pattern, mobile):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")

if re.match(mobile_pattern, mobile1):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")

#Password 

password = "Khushal@123"

password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$'

if re.match(password_pattern, password):
    print("Strong Password")
else:
    print("Weak Password")

#Pincode 

pincode = "302017"

pincode_pattern = r'^[1-9][0-9]{5}$'

if re.match(pincode_pattern, pincode):
    print("Valid Pincode")
else:
    print("Invalid Pincode")
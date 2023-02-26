import re

def phone_number_validator(number):
  valid = r'^[0-9]{3}-[0-9]{3}-[0-9]{4}$'  
  if re.search(valid, number):
    print("Phoone number validation successful")  
  else:
    print("Phone number validation failed")
phone = input("Please enter your phone number: ")
phone_number_validator(phone)
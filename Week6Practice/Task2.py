import re
username_pattern = r'^[a-zA-Z][\w]{4,19}$'
password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
email_pattern = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
username = input("Enter username: ")
password = input("Enter password: ")
email = input("Enter email address: ")
username_valid = re.match(username_pattern, username)
password_valid = re.match(password_pattern, password)
email_valid = re.match(email_pattern, email)
if username_valid and password_valid and email_valid:
    print("Registration successful!")
else:
    print("Registration failed. Please check your input and try again.")
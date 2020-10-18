# You will be given a string. Write a program to check the strength of a supplied password.
#
# Feebacks:
#
# 1. The length of the password must be at least 8 characters in length
# 2. The password must contain at least 1 capital letter
# 3. The password must contain at least 1 digit
# 4. The password must contain at least 1 special character and allowed special characters are (!,@,#,$,&)
#
# We need to provide feedback to the user about the strength of their password
#
# Provide the user with a list of reasons why their password is 'weak'
#
#  Note: Order for feedback should be same as given.
#
# Input Format:
#
# THe first line contains string password
# Output Format:
#
# print the status weeak or strong in wst line in next few lines print feedback
#
# Sample Input 0:
# abcDE12
#
# Sample Output 0:
# Weak
# The length of the password must be at least 8 characters in length
# The password must contain at least 1 capital letter
# The password must contain at least 1 special character and allowed special characters are (!,@,#,$,&)



import re
password = str(input())

regex = re.compile('[!@#$&]')
upper, digit, special, flag = 0, 0, 0, 0

if flag == 0:
    output = 'Weak'
    if len(password) <= 8:
        output += '\nThe length of the password must be at least 8 characters in length'
        flag += 1
    for i in password:
        if str(i).isupper():
            upper += 1
        if i.isdigit():
            digit += 1
    if upper == 0:
        output += '\nThe password must contain at least 1 capital letter'
        flag += 1
    if digit == 0:
        output += '\nThe password must contain at least 1 digit'
        flag +=1
    if regex.search(password) is None:
        output += '\nThe password must contain at least 1 special character and allowed special characters are (!,@,#,$,&)'
        flag += 1

if flag == 0:
    print('Strong')
else:
    print(output)

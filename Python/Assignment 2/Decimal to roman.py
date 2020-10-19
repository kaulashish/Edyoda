# You will be given an integer. You have to convert this intege into roman numbers. If given number is grater then or equal to 4000 print False.
#
# Input Format:
# The First line contains an integer
#
# Output Format:
# Print the Roman value in string format
#
# Sample Input 0:
# 5
# Sample Output 0:
# V



n = 3549

dec_to_roman = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
                (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
output = ''

if n < 4000:
    for dec, rom in dec_to_roman: # 1st iter dec = 1000, rom = M
        while n >= dec: # 3549 > 1000 (1st iter)
            output += rom   # output = M
            n -= dec    # n = 3549 - 1000 = 2549

else:
    output = 'False'

print(output)

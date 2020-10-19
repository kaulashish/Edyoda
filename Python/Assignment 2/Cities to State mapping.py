# You will be given an integer number of elements and for next n
# lines space separeted key values pairs 1st values will be key and remaining will be values.
#
# For example:
# NewHampshire Concord Hanover
# in above given line there are 3 space seprated words NewHamspshire, Concord and Hanover.
# NewHamspshire is key and Concord and Hanover are values so this would be like this
# "NewHamspshire":["Concord","Hanover"]
#
# Make a dict from strings Given a dictionary that associates the names of states
# with a list of the names of cities that appear in it,write a program that creates
# a new dictionary that associates the name of a city with the list of states that it appears in.
#
# Input Format:
# You will be given an integer number of elements and for next n lines space separeted key value pairs
#
# Output Format:
# Print The dictionary.
#
# Sample Input 0:
# 3
# NewHampshire Concord Hanover
# Massachusetts Boston Concord Springfield
# Illinois Chicago Springfield Peori
#
# Sample Output 0:
# {'Concord': ['NewHampshire', 'Massachusetts'], 'Hanover': ['NewHampshire'],
#  'Boston': ['Massachusetts'], 'Springfield': ['Massachusetts', 'Illinois'],
#  'Chicago': ['Illinois'], 'Peoria': ['Illinois']}

n = int(input())
dict1, dict2 = {}, {}

for i in range(n):  #create dict from inputs with 1st item as key and rest as values
    inp = input().split()
    dict1[inp[0]] = inp[1:]

for key, value in dict1.items():
    for i in value:
        if i in dict2:
            dict2[i].append(key)
        else:
            dict2[i] = [key]
print(dict2)

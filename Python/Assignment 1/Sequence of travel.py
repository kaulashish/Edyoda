# You will be given an integer number of elements and for next n lines space
# separeted key value pairs. make a dict from strings of tickets("to":"from").
# find out the sequence of travel.
# Assuming that there will be only one starting point for the journey.

# Input Format:

# You will be given an integer number of elements and for next n lines
# space separeted key value pairs

# Output Format:

# Print The dictionary fro the sequence of travel.

# Sample Input 0:

# {"Chennai":"Bangalore","Bombay":"Delhi","Goa":"Chennai","Delhi":"Goa"}

# Sample Output 0:

# {'Bombay':'Delhi','Delhi':'Goa','Goa':'Chennai','Chennai':'Banglore'}

# ----- Solution -----

# n = int(input())
# dict_ = dict(input().split() for _ in range(n))
# print(dict_)

dict_ = {
         "Chennai": "Bangalore",
         "Bombay": "Delhi",
         "Goa": "Chennai",
         "Delhi": "Goa"
         }

source, dest = list(dict_.keys()), list(dict_.values())
new_source, new_dest = [], []

# create starting point
for i in source:
    if i in source and i not in dest:
        new_source.append(i)

# check dest corresponding to source and append to new_dest and vice-versa
for i in range(0, len(source)):
    new_dest.append(dest[source.index(new_source[i])])

    if new_dest[-1] not in new_source:  # avoiding repitition
        if new_dest[-1] in source:  # avoiding final destination to enter
                                    # new_source, i.e Bangalore
            new_source.append(new_dest[-1])

print(dict(zip(new_source, new_dest)))

# In the pre-smartphone era,each number key is assigned a subset of the alphabet {a,b,…,z}.
# - 2 is assigned {a,b,c},
# - 3 is assigned {d,e,f}
# - 4 is assigned {g,h,i}
# - 5 is assigned {j,k,l}
# - 6 is assigned {m,n,o}
# - 7 is assigned {p,q,r,s}
# - 8 is assigned {t,u,v}
# - 9 is assigned {w,x,y,z}
#
# Input Format:
#
# The first line contains a string it will be number.
#
# Output Format:
#
# Print the string
#
# Sample Input 0:
# 9999335533
#
# Sample Output 0:
# zeke


input_seq = 9999335533
output_seq, count = [], 0
t9 = {2 : ['a', 'b', 'c'],
      3 : ['d', 'e', 'f'],
      4 : ['g', 'h', 'i'],
      5 : ['j', 'k', 'l'],
      6 : ['m', 'n', 'o'],
      7 : ['p', 'q', 'r', 's'],
      8 : ['t', 'u', 'v'],
      9 : ['w', 'x', 'y', 'z']}

input_seq_list = list(map(int, str(input_seq)))
for i in range(0, len(str(input_seq))):
    try:
        if input_seq_list[i] == input_seq_list[i + 1]:
            count += 1
        elif input_seq_list[i] != input_seq_list[i + 1] or input_seq_list[i] == input_seq_list[-1]:
            output_seq.append(t9.get(input_seq_list[i])[count])
            count = 0
    except IndexError:
        output_seq.append(t9.get(input_seq_list[i])[count])
print(*output_seq, sep = '')

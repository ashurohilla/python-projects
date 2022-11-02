import re
patterns = ['term1','term2']
text = 'thisis the string of term1 ,not the other'

# searching using loops
# for pattern in patterns:
#     print("i am searching for "+ pattern)
    #searching using regular expression 
match = re.search('term1', text)
print(match)
print(match.start())

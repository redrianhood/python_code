#!/usr/bin/python3
"""
Alta3 challenge
Review of Lists and Dictionaries
"""

# define a short data set (in real world, we would read this from a file or API)
munsters = {'endDate': 1966, 'startDate': 1964,\
        'names':['Lily', 'Herman', 'Grandpa', 'Eddie', 'Marilyn']}   # {} creates dict

# ----------------------------------

# display value mapped to names
print("names contain:", munsters.get('names'))

# display value mapped to endDate
print("endDate is:", munsters.get('endDate'))

# display value mapped to startDate
print("startDate is:", munsters.get('startDate'))

# add new key 'episodes' mapped to the value of 70
munsters['episodes'] = 70
print(munsters)
print("added value for episodes:", munsters.get('episodes'))

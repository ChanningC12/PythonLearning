# Lists, are donate by brackets and commas
a_list = [13,32,18,44,65,733]
other_list = ['This','is','a','string','list']
mixed_list = [12, 'one', 33, 'out of order', 0.1]

print a_list
print other_list
print mixed_list

# Some operations with lists
a_list_length = len(a_list)
a_list_sum = sum(a_list)
print a_list_length
print a_list_sum

del a_list[2]
print a_list
a_list.remove(44)
print a_list

# slice elements
sliced_a_list = a_list[1:]
print sliced_a_list

print a_list[::2]
sliced_a_list.insert(2,34)

"is" in other_list

# Dictionaries
empty_dict = {}
a_dict = {'ID':13,'Name':'John'}
print a_dict
a_dict['Address'] = '200 Berkeley St'
print a_dict
print len(a_dict)
print a_dict.keys()
print a_dict.values()
'Address' in a_dict

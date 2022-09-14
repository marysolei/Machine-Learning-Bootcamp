#check for duplicates in list
#can't use set
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicate = []
for item in some_list: 
  if item in duplicate:
    print(item)
  if item not in duplicate:
    duplicate.append(item)

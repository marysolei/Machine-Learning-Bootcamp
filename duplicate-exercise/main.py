# return a list of duplicates in a list using python comprehension
my_list = [1,2,2,3,4,4,5]
duplicates = list(set ([num for num in my_list if my_list.count(num)>1]))
print(duplicates)

# filter is used to filter the given sequence 
# lambda is an anonymous function.
my_list=[12,13,14,15]
result = list(filter(lambda x: (x % 3 == 0), my_list))  
print(result)
#map() function returns a map object(which is an iterator) 
# of the results after applying the given function to each item of a given iterable (list, tuple etc.)
n=int(input("Enter the number:"))
result = list(map(lambda x: 2 ** x, range(n)))
for i in range(n):
    print(result[i])
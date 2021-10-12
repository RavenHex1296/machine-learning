dictionary = {1:[], 2:[]}
x = {1:[(0, 1)], 2:[1,2,3]}
dictionary[1].append(x[1][0])
print(dictionary)

print(len(x[1]+x[2]))
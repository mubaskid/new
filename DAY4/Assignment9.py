listy = ['a', 'b', ['c',['d', 'e',['f', 'g'], 'k'], 'l'], 'm', 'n']
lis = ['h', 'i', 'j']

listy[2][1][2].extend(lis)

# list_to_be_added.extend(listy)
# listy.append(list_to_be_added)
print(listy)
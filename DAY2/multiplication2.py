def doubleStuff(aList):
    for position in range(len(aList)):
        aList[position] = 2 * aList[position]

things = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10, 11, 12]
print(things)
doubleStuff(things)
print(things)

# for i in range(1, 10):
#     for j in range(i, (i*10)+1):
#         if (j %i == 0):
#             print(j, end='\t')
#             print()
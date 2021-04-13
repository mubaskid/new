# txt = [5, 20, 15, 20, 25, 50, 20]
# print('the orginal list is: ' + str(txt))

# res = []
# [res.append for x in txt if x not in res]
# print('the lists after removing duplicates is:' + str (res))


# Python 3 code to demonstrate 
# removing duplicated from list 
# using list comprehension 

# initializing list 
test_list = [1, 3, 5, 6, 3, 5, 6, 1] 
print ("The original list is : " + str(test_list)) 

# using list comprehension 
# to remove duplicated 
# from list 
res = [] 
[res.append(x) for x in test_list if x not in res] 

# printing list after removal 
print ("The list after removing duplicates : " + str(res)) 
                                
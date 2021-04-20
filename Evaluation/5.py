test_list = ["A", "B", "C", "D", "E", "F", "G", "H"]


print("The original list : " + str(test_list))


odd_i = []
even_i = []
for i in range(0, len(test_list)):
    if i % 2:
        even_i.append(test_list[i])
    else:
        odd_i.append(test_list[i])

res = odd_i + even_i


print("Seprated odd and even index list: " + str(res))

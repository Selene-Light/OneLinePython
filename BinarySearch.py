binary_search = lambda num, num_list: False if not int(len(num_list)//2) else True if num_list[int(len(num_list)//2)] == num else binary_search(num, num_list[int(len(num_list)//2)+1:]) if num_list[int(len(num_list)//2)] < num else binary_search(num, num_list[:int(len(num_list)//2)])
# use the following code to test it
# print(binary_search(-1, [-3, -1, 2, 3, 5]))
# print(binary_search(-1, [-3, 2, 3, 5]))
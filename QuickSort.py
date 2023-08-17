quick_sort = lambda num_list: num_list if len(num_list) <= 1 else quick_sort([num for num in num_list if num < num_list[0]]) + [num_list[0]] + quick_sort([num for num in num_list if num > num_list[0]])
# run the following code to test it
# num_list = [64, 34, 25, 12, 22, 11, 90]
# print(quick_sort(my_list))
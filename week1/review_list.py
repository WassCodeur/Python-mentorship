
>>> my_list1 = [1, True, "Hello"]
>>> my_list2 = my_list1[:]
>>> print(my_list2)
[1, True, 'Hello']
>>> print(my_list1)
[1, True, 'Hello']
>>> my_list2.append([1, 3, 4])
>>> print(my_list1)
[1, True, 'Hello']
>>> print(my_list2)
[1, True, 'Hello', [1, 3, 4]]
>>> my_list2 = my_list1
>>> print(my_list2)
[1, True, 'Hello']
>>> print(my_list1)
[1, True, 'Hello']
>>> my_list2.append([1, 3, 4])
>>> print(my_list1)
[1, True, 'Hello', [1, 3, 4]]
>>> print(my_list2)
[1, True, 'Hello', [1, 3, 4]]
>>> 


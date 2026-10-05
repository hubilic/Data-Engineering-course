import numpy as np

a = np.array([1, 2, 3])
b = np.eye(3)
c = np.zeros((10, 10))
d = np.array([[1, 2, 3], [4, 5, 6]])

list1 = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])


list2 = np.array([
        [7, 8, 9],
        [10, 11, 12]
    ])

list3 = list1 * 3
list4 = list2 * list1
list5 = sum(list1)
list6 = list1[-1:, -1:]
list7 = np.transpose(list1)
list8 = list5.dtype
list9 = np.where(list1 % 2 == 0)
list10 = list1[list1 % 2 == 0]

print(list4)
print(list5)
print(list6)
print(list7)
print(list8)
print(list9)
print(list10)

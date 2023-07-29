from collections import Counter

n = int(input("enter the length of array"))


arr = []

for i in range (0, n):
    x = (int(input("enter the next element in array")))
    arr.append(x)

# 
count_dict = Counter(arr)
second_most_frequent_number = count_dict.most_common(2)[-1][0]

print(arr)
print(second_most_frequent_number)
# enter the input from the user
num_dig_arr = int(input("Enter the number of digits in the array: "))
arr = list(map(int, input("Enter the elements of the array (space-separated): ").split()))
quss_num = int(input("Enter the number of questions: "))
questions = list(map(int, input("Enter the questions (space-separated): ").split()))

# Sort the array in order for searching
arr.sort()

# Answer user questions
for x in questions:
    count = 0
    for num in arr:
        if num < x:
            count += 1
        else:
            break  # Optimization: No need to continue once numbers are >= x
    print(count, end= "  ")
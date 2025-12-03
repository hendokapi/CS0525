def calculate_group_mean(the_list, start, end):
    group = the_list[start : end]
    # print(group)
    mean = sum(group) / len(group)
    return mean
    
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
window = 3

mean_values = []

for index in range(window - 1):
    mean_values.append(calculate_group_mean(numbers, 0, index+1))

for index in range(len(numbers) - window + 1):
    mean = calculate_group_mean(numbers, index, index+window)
    mean_values.append(mean)

print(mean_values)


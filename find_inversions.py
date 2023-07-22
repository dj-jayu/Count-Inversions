# read the file with the numbers, and append them to an array
array = []
with open('numbers.txt') as my_file:
    for line in my_file:
        line = line.strip()
        array.append(int(line))

# count all inversions using divide and conquer
def count_inversions(my_array):
    n = len(my_array)
    if n == 1:
        return my_array, 0
    left_array, left_inversions = count_inversions(my_array[:n//2])
    right_array, right_inversions = count_inversions(my_array[n//2:])
    final_array, crossed_inversions = merge(left_array, right_array)

    return final_array, left_inversions + right_inversions + crossed_inversions

# merge two arrays in sorted order, counting the inversions between them
def merge(left_array, right_array):
    final_array = []
    inversions = 0
    left_pointer = 0
    right_pointer = 0
    while left_pointer < len(left_array) or right_pointer < len(right_array):
        if left_pointer >= len(left_array):
            final_array.extend(right_array[right_pointer:])
            break
        if right_pointer >= len(right_array):
            final_array.extend(left_array[left_pointer:])
            break
        else:
            if left_array[left_pointer] < right_array[right_pointer]:
                final_array.append(left_array[left_pointer])
                left_pointer += 1
            else:
                final_array.append(right_array[right_pointer])
                inversions += len(left_array) - left_pointer
                right_pointer += 1
    return final_array, inversions

print(f'Total number of inversions: {count_inversions(array)[1]}')

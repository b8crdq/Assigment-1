#
# student = ("Talha",21,"Male")
#
# print(student.index("Talha"))
# print(student.count("Male"))
#
# for x in student:
#             print(x)
#             if "Talha" in student:
#                               print("Talha is Here")
#
#
# # Set
#
# utensils = {"FOrk","Spoon","Knife"}
# dishes = {"Plate","cup","Bowl","Knife"}
# dishes.update(utensils)
# # print(dishes.update("Knife"))
# # dishes_table = utensils.union(dishes)
# # for x in dishes_table:
# #       print(x)
#
# print(dishes.difference(utensils))
#
# capitals = {'Gemrany':'Berlin',
#         'Paris':'Moscow'}
#
# print(capitals.get("Germany"))
#
#
# userName = input("ENter your name :")
# userAge = input("Enter Your age:")
# print("hELLO " "+ userAge+"   "you are" "+userAge+" "years old.")
# print(f"Hello {userName}" + {userAge})

# Task1
def sum(a, b):
    return (a + b)

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

print(f'Sum of {a} and {b} is {sum(a, b)}')

# Task 2
def find_maximum_value(lst):
    if not lst:
        print("The list is empty.")
        return None

    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num

    print("Maximum value:", max_val)
    return max_val
numbers = [7, 12, 4, 9, 22, 3]
max_value = find_maximum_value(numbers)
# Task 3

def reverse_list_in_place(lst):
    lst.reverse()
    print("Reversed list:", lst)

my_list = [1, 2, 3, 4]
reverse_list_in_place(my_list)

# Task 4

def remove_duplicates(lst):
    seen = set()  # To keep track of seen elements
    result = []   # To store the unique elements in the original order

    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)

    print("List with duplicates removed:", result)
    return result
my_list = [1, 2, 2, 3, 4, 4, 5]
result_list = remove_duplicates(my_list)

# Task 5

def list_intersection(list1, list2):
    common_elements = [item for item in list1 if item in list2]
    print("Common elements:", common_elements)
    return common_elements

list_a = [1, 2, 3, 4]
list_b = [3, 4, 5, 6]
common_elements_list = list_intersection(list_a, list_b)

# Task 6

def rotate_list(lst, positions):
    positions %= len(lst)  # Handle positions larger than list size
    rotated_list = lst[positions:] + lst[:positions]
    print("Rotated list:", rotated_list)
    return rotated_list

original_list = [1, 2, 3, 4, 5]
rotated_list = rotate_list(original_list, 2)

# Task 7

def sort_list_alphabetically(lst):
    sorted_list = sorted(lst)
    print("Sorted list:", sorted_list)
    return sorted_list
string_list = ["apple", "banana", "cherry", "date"]
sorted_string_list = sort_list_alphabetically(string_list)

# Task 8

def slice_list(lst, start, end):
    sliced_list = lst[start:end+1]
    print("Sliced list:", sliced_list)
    return sliced_list
original_list = [1, 2, 3, 4, 5]
sliced_list = slice_list(original_list, 1, 3)

# Task 9

def flatten_nested_list(nested_lst):
    flat_lst = [item for sublist in nested_lst for item in sublist]
    print("Flattened list:", flat_lst)
    return flat_lst

nested_list = [[1, 2], [3, 4], [5, 6]]
flattened_list = flatten_nested_list(nested_list)







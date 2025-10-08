favoritefoods = ["ramen", "dumplings", "curry", "salad", "noodles"]
print(favoritefoods[1])
print(favoritefoods[-1])

favoritefoods.append("falafel")
favoritefoods.insert(0, "apple")
del favoritefoods[2]
print(len(favoritefoods))

for food in favoritefoods:
    print(food.upper())
first_last_foods = [favoritefoods[0], favoritefoods[-1]]
print(first_last_foods)

if "potato" in favoritefoods:
    print("A potato!")
else:
    print("No potato!")

numbers = list(range(0, 21))

def get_first_15(numbers):
    return numbers[:15]

def get_every_5th(lst):
    return lst[::5]

def reverse_and_stride(lst):
    reversed_list = lst[::-1]
    return reversed_list[::3]

step1 = get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)
print(step1, step2, step3)

numbers_nested = [
    [2, 4, 6],
    [3, 5, 7],
    [8, 10, 12]
]
print(numbers_nested[2])
print(numbers_nested[1][1])
numbers_nested.append([10, 11, 12])

def sum_nested(nested_list):
    total = 0
    for row in nested_list:
        for number in row:
            total += number
    return total

print(sum_nested(numbers_nested))

def create_5x5():
    grid = []
    num = 1
    for _ in range(5):
        row = []
        for _ in range(5):
            row.append(num)
            num += 1
        grid.append(row)
    return grid

five_by_five = create_5x5()

def replace_multiples_of_3(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] % 3 == 0:
                matrix[i][j] = "?"
    return matrix

updated_list = replace_multiples_of_3(five_by_five)

def sum_non_question(matrix):
    total = 0
    for row in matrix:
        for element in row:
            if element != "?":
                total += element
    return total

result_sum = sum_non_question(updated_list)
print(updated_list)
print(result_sum)

ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}
print(ages["Katie"])
ages["Mira"] = 100
ages["Milana"] = 52
del ages["Mariam"]
for name, age in ages.items():
    print(name, age)

print(create_5x5())

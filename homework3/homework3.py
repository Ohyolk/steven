def say_goodbye(name):
    print("Goodbye", name)

say_goodbye("Steven")

def Area_of_circle(radius):
    return(radius ** 2 * 3.14)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def what_to_wear(temps):
    return(min(temps),max(temps))


def is_weekend(intday):
    if intday > 5:
        return "Its the weekend!"
    else:
        return "Its not the weekend."
    
def fuel_efficiency(miles,gallons):
    return(miles/gallons)


def secret(num):
    last_num = num % 10
    rest_num = num // 10
    return(str(last_num) + str(rest_num))

def oski_power(x,y):
    product = 1
    if(y == 0):
        return product
    else:
        while(y > 0):
            product *= x
            y -= 1
    return product

def for_max(nums):
    max = nums[0]
    for num in nums:
        if(num > max):
            max = num
    return max

def for_min(nums):
    min = nums[0]
    for num in nums:
        if(num < min):
            min = num 
    return min

def find_max_while(nums):
    maximum = nums[0]
    i = 0
    while i < len(nums):
        if nums[i] > maximum:
            maximum = nums[i]
        i += 1
    return maximum

def find_min_while(nums):
    minimum = nums[0]
    i = 0
    while i < len(nums):
        if nums[i] < minimum:
            minimum = nums[i]
        i += 1
    return minimum

def sum_of_digits(n):
    sum = 0
    for d in str(n):
        sum += int(d)
    return sum


#favorite code below

def sum_of_digits(n):
    sum = 0
    for d in str(n):
        sum += int(d)
    return sum

print(sum_of_digits(9812145))
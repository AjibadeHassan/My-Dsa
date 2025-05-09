#TIME COMPLEXITY
studentList = ["John", "Jane", "Doe", "Smith", "Doe"]  # O(1)
def anyFunction(students):
    total = 0  # O(1)
    newlist = []  # O(1)

    for student in students:
        total += 1  # O(n)
        newlist.append(student)  # O(n)
    print(newlist)  # O(1)
    return total  # O(1)

print(anyFunction(studentList))  # O(5 + 2n)

# Big O of n squared

num_list = [1, 2, 3, 4, 5, 6, 7]


def randFunction(props):
    total = 0
    for num1 in num_list:
        for num2 in num_list:
            print(num1, num2)
            total += 1
    return total 


print(randFunction(num_list)) 




# SPACE
# COMPLEXITY 

# Big O(1) constant
def display_cubes(items):

    result = pow(items[0], 3) 
    print(result)
items = [2,3,4,5,6,7]
display_cubes(items)


# Big O(n) Linear

def all_cubes(values):
    result = []
    for item in values:
        result.append(pow(item,3)) # O(n)
    print(result)
values = [2,3,4,5,6,7]
all_cubes(values)
#TIME COMPLEXITY
def anyFunction(students):
    total = 0  # O(1)
    newlist = []  # O(1)

    for student in students:
        total += 1  # O(n)
        newlist.append(student)  # O(n)
    print(newlist)  # O(1)
    return total  # O(1)
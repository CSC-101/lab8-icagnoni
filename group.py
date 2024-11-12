#Task 1

def groups_of_3(numbers: list[int])-> list[list[int]]:
    return [numbers[i:i+3] for i in range(0, len(numbers), 3)]




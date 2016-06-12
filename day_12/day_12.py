import re


def is_num(char):
    try:
        int(char)
        return True
    except:
        return False


def red_in_object(object):
    object = str(object)
    for char in range(0, len(object) - 2):
        if object[char:char + 3] == 'red':
            return True
    return False


def subdivide(puzzle_input):
    subdivided_objects = []
    i = 0
    bracket_count = 0
    start = 0
    end = 0
    for char in puzzle_input:
        if char == '{' and bracket_count == 0:
            start = i
            bracket_count += 1
            non_objects.append(puzzle_input[end + 1:start])
        elif char == '{':
            bracket_count += 1
        elif char == '}' and bracket_count - 1 == 0:
            end = i
            bracket_count -= 1
            objects.append(str(puzzle_input[start:end + 1]))
        elif char == '}':
            bracket_count -= 1

        i += 1


# ~~~~~~~~~~ Part 1 ~~~~~~~~~~
raw_puzzle_input = open('data', 'r')
puzzle_input = [line.strip('\n') for line in raw_puzzle_input][0]
# puzzle_input = '[1,"red",5]'
puzzle_input_list = list(puzzle_input)

numbers = re.findall(r'([-]*[0-9]+)', puzzle_input)

total_of_all_numbers = sum(int(num) for num in numbers)

print(total_of_all_numbers)


# ~~~~~~~~~~ Part 2 ~~~~~~~~~~
start = 0
end = 0
bracket_count = 0
i = 0
objects = []
non_objects = []

# Separate the string into lists of objects, and the strings between objects
for char in puzzle_input:
    if char == '{' and bracket_count == 0:
        start = i
        bracket_count += 1
        non_objects.append(puzzle_input[end + 1:start])
    elif char == '{':
        bracket_count += 1
    elif char == '}' and bracket_count - 1 == 0:
        end = i
        bracket_count -= 1
        objects.append(str(puzzle_input[start:end + 1]))
    elif char == '}':
        bracket_count -= 1
    i += 1

for char in puzzle_input:
    for char in puzzle_input[i::]:
        if char == '{' and bracket_count == 0:
            start = i
            bracket_count += 1
            non_objects.append(puzzle_input[end + 1:start])
        elif char == '{':
            bracket_count += 1
        elif char == '}' and bracket_count - 1 == 0:
            end = i
            bracket_count -= 1
            objects.append(str(puzzle_input[start:end + 1]))
        elif char == '}':
            bracket_count -= 1
    i += 1

non_objects.append(puzzle_input[end::])

valid_objects = [object for object in objects if not red_in_object(object)]

numbers = re.findall(r'([-]*[0-9]+)', ''.join(valid_objects)) + re.findall(r'([-]*[0-9]+)', ''.join(non_objects))
numbers = [int(number) for number in numbers]

for num in numbers:
    print(num)
    total_of_all_numbers += num

print(total_of_all_numbers)
print('All Objects:')
for object in objects:
    print(object)
print('~~~~~~~~~~~~~~~~~~~~~~~')
print('Valid Objects:')
for object in valid_objects:
    print(object)
print('~~~~~~~~~~~~~~~~~~~~~~~')
print('Non-Objects:')
for object in non_objects:
    print(object)
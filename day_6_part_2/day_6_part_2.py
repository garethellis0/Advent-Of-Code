class Instruction:
    def __init__(self, command, x1, y1, x2, y2):
        self.command = command
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


def toggle_light_state(lights, x, y):
    # Toggles the light state of a light at a given coordinate
    lights[x][y] += 2
    return lights


def toggle_lights_state(lights, x1, y1, x2, y2):
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            lights = toggle_light_state(lights, x, y)
    return lights


def change_lights_state(lights, x1, y1, x2, y2, state):
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if state == 0 and lights[x][y] > 0:
                    lights[x][y] -= 1
            if state == 1:
                lights[x][y] += 1
    return lights


def format_instruction(raw_instruction):
    instruction1 = raw_instruction.replace(',', ' ').split(' ')
    instruction1 = [x.strip('\n') for x in instruction1]
    if instruction1[0] == 'turn':
        command = ' '.join(instruction1[0:2])
        x1 = int(instruction1[2])
        y1 = int(instruction1[3])
        x2 = int(instruction1[5])
        y2 = int(instruction1[6])
    else:
        command = instruction1[0]
        x1 = int(instruction1[1])
        y1 = int(instruction1[2])
        x2 = int(instruction1[4])
        y2 = int(instruction1[5])
    return Instruction(command, x1, y1, x2, y2)


# An array of [x, y] coordinates, representing all lights on
lights = [[0 for x in range(0, 1000)] for y in range(0, 1000)]

raw_instructions = open('data', 'r')
raw_instructions = list(raw_instructions)

instructions = [format_instruction(instruction) for instruction in raw_instructions[0:len(list(raw_instructions)) - 1]]

for instruction in instructions:
    print(instruction.command)
    print(instruction.x1)
    print(instruction.y1)
    print(instruction.x2)
    print(instruction.y2)
    if instruction.command == 'toggle':
        lights = toggle_lights_state(lights, instruction.x1, instruction.y1, instruction.x2, instruction.y2)
    elif instruction.command == 'turn on':
        lights = change_lights_state(lights, instruction.x1, instruction.y1, instruction.x2, instruction.y2, 1)
    elif instruction.command == 'turn off':
        lights = change_lights_state(lights, instruction.x1, instruction.y1, instruction.x2, instruction.y2, 0)

ticker = 0

for row in lights:
    print(row)
    for light in row:
        ticker += light

print(ticker)
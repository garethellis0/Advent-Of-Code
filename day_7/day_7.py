# --- Day 7: Some Assembly Required ---
#
# This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.
#
# Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.
#
# The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.
#
# For example:
#
#     123 -> x means that the signal 123 is provided to wire x.
#     x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
#     p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
#     NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.
#
# Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.
#
# For example, here is a simple circuit:
#
# 123 -> x
# 456 -> y
# x AND y -> d
# x OR y -> e
# x LSHIFT 2 -> f
# y RSHIFT 2 -> g
# NOT x -> h
# NOT y -> i
#
# After it is run, these are the signals on the wires:
#
# d: 72
# e: 507
# f: 492
# g: 114
# h: 65412
# i: 65079
# x: 123
# y: 456
#
# In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?
#
# Your puzzle answer was 3176.
# --- Part Two ---
#
# Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires (including wire a). What new signal is ultimately provided to wire a?
#
# Your puzzle answer was 14710.

import re

# BASICALLY DONT<  JUST NEED TO FIX REGEX
class Instruction():
    def __init__(self, input_wires, cmd, cmd_val, output_wire):
        self.input_wires = input_wires
        self.cmd = cmd
        self.cmd_val = cmd_val
        self.output_wire = output_wire


def print_instructions(instructions):
    for instruction in instructions:
        print('----------')
        print(instruction.cmd)
        print(instruction.cmd_val)
        print(instruction.input_wires)
        print(instruction.output_wire)


def get_instruct(line):
    try:
        command = re.findall('([A-Z]+)', line)[0]
    except:
        command = None
    cmd_val = None
    inputs = None
    output = None
    if command == 'LSHIFT' or command == 'RSHIFT':
        cmd_val = re.findall('([0-9]+)', line)[0]
        inputs = re.findall('([a-z]+)', line.split('->')[0])[0]
        output = re.findall('([a-z]+)', line.split('->')[1])[0]
    elif command == 'AND' or command == 'OR':
        inputs = [line.split('->')[0].split(' ')[0], line.split('->')[0].split(' ')[2]]
        #inputs = re.findall('([a-z]+)', line.split('->')[0])
        output = re.findall('([a-z]+)', line.split('->')[1])[0]
    elif command == 'NOT':
        inputs = re.findall('([a-z]+)', line.split('->')[0])[0]
        output = re.findall('([a-z]+)', line.split('->')[1])[0]
    elif command == None:
        try:
            cmd_val = re.findall('([0-9]+)', line)[0]
        except:
            inputs = re.findall('([a-z]+)', line.split('->')[0])[0]
        output = re.findall('([a-z]+)', line.split('->')[1])[0]
    return Instruction(inputs, command, cmd_val, output)


def get_instructions():
    raw_instructions = open('data', 'r')
    raw_instructions2 = [line for line in raw_instructions]
    instructions = [get_instruct(line) for line in raw_instructions2[0:len(raw_instructions2) - 1]]
    return instructions


def convert_str_to_int(instructions):
    for instruct in instructions:
        try:
            for wire in instruct.input_wires:
                try:
                    wire = int(wire)
                except:
                    None
        except:
            None
        if instruct.cmd_val != None:
            instruct.cmd_val = int(instruct.cmd_val)
    return instructions


def is_int(text):
    try:
        int(text)
        return True
    except:
        return False


def solve(wire, instructions, visited, solved_vals):
    for val in solved_vals:
        if val[0] == wire:
            return val[1]
    if is_int(wire):
        return int(wire)
    for instruct in instructions:
        if instruct.output_wire == wire:
            #print_instructions([instruct])
            if instruct not in visited:
                visited.append(instruct)
            #print("%d Instructions visted" % len(visited))
            #print("Solved for %d values\n" % len(solved_vals))
            if instruct.cmd == None:
                if instruct.cmd_val == None:
                    return solve(instruct.input_wires, instructions, visited, solved_vals)
                else:
                    solved_vals.append([wire, instruct.cmd_val])
                    return instruct.cmd_val
            elif instruct.cmd == 'AND':
                val = solve(instruct.input_wires[0], instructions, visited, solved_vals) & solve(instruct.input_wires[1], instructions, visited, solved_vals)
                solved_vals.append([instruct.output_wire, val])
                return val
            elif instruct.cmd == 'OR':
                val = solve(instruct.input_wires[0], instructions, visited, solved_vals) | solve(instruct.input_wires[1], instructions, visited, solved_vals)
                solved_vals.append([instruct.output_wire, val])
                return val
            elif instruct.cmd == 'NOT':
                val = ~solve(instruct.input_wires, instructions, visited, solved_vals)
                solved_vals.append([instruct.output_wire, val])
                return val
            elif instruct.cmd == 'LSHIFT':
                val = solve(instruct.input_wires, instructions, visited, solved_vals) << instruct.cmd_val
                solved_vals.append([instruct.output_wire, val])
                return val
            elif instruct.cmd == 'RSHIFT':
                val = solve(instruct.input_wires, instructions, visited, solved_vals) >> instruct.cmd_val
                solved_vals.append([instruct.output_wire, val])
                return val

instructions = get_instructions()
instructions = convert_str_to_int(instructions)

# ~~~~~~~~~~~~~~~~~~~~~~~ Part 1 ~~~~~~~~~~~~~~~~~~~~~~~
print('Working......')
wire_a_val = solve('a', instructions, [], [])
print('The wire a will have a value of %d' % wire_a_val)

# ~~~~~~~~~~~~~~~~~~~~~~~ Part 2 ~~~~~~~~~~~~~~~~~~~~~~~
# Find and replace the value of b with the value of a
for instruct in instructions:
    if instruct.output_wire == 'b' and instruct.cmd == None:
        instruct.cmd_val = wire_a_val
        break

new_wire_a_val = solve('a', instructions, [], [])

print('Using the value of a (%d) for the start value of wire b, wire a will have a value of %d' %
      (wire_a_val, new_wire_a_val))







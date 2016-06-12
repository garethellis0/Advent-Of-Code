# --- Day 3: Perfectly Spherical Houses in a Vacuum ---
#
# Santa is delivering presents to an infinite two-dimensional grid of houses.
#
# He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.
#
# However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?
#
# For example:
#
#     > delivers presents to 2 houses: one at the starting location, and one to the east.
#     ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
#     ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
#
# Your puzzle answer was 2572.
# --- Part Two ---
#
# The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.
#
# Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.
#
# This year, how many houses receive at least one present?
#
# For example:
#
#     ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
#     ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
#     ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.
#
# Your puzzle answer was 2631.

# ~~~~~~~~~~~~~~~~~~~~ Part One ~~~~~~~~~~~~~~~~~~~~


def houses_visited(directions):
    # Gets the all houses visited from a given set of directions (ignoring repeated houses)
    xcoor = 0  # Present x-coordinate
    ycoor = 0  # Present y-coordinate
    visited = []  # List of all coordinates visited [x,y]

    for direction in directions:
        if direction == 'v':
            ycoor -= 1
        elif direction == '^':
            ycoor += 1
        elif direction == '>':
            xcoor += 1
        elif direction == '<':
            xcoor -= 1

        new_coordinates = [xcoor, ycoor]

        if new_coordinates not in visited:
            visited.append(new_coordinates)

    return visited

# Get the puzzle data from local file
puzzle_data = open('data', 'r')
raw_directions = list(puzzle_data)
directions = list(raw_directions[0].strip('\n'))


print("The first year Santa will deliver at presents to %d lucky houses!" % len(houses_visited(directions)))

# ~~~~~~~~~~~~~~~~~~~~ Part Two ~~~~~~~~~~~~~~~~~~~~

santa_directions = []
robo_santa_directions = []

# Divide up directions into santa directions and robo-santa directions
for x in range(0, len(directions)):
    if x % 2 == 0:
        santa_directions.append(directions[x])
    else:
        robo_santa_directions.append(directions[x])

santa_visited = houses_visited(santa_directions)
robo_santa_visited = houses_visited(robo_santa_directions)

merged_visited = []  # Locations visited by Santa and Robo-Santa (with duplicates removed)

# Add all locations visited by Santa and Robo-Santa to merged_visited, ignoring duplicates between the two lists
for location in santa_visited:
    if location not in robo_santa_visited:
        merged_visited.append(location)

merged_visited += robo_santa_visited


print("The second year, santa and robo-santa will visit a total of %d lucky houses!" % len(merged_visited))



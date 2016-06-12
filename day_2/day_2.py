
def required_wrapping_paper(length, width, height):
    # Returns the amount of wrapping paper required for a gift of given length, width, and height
    side1 = length * width
    side2 = width * height
    side3 = height * length
    area = 2*side1 + 2*side2 + 2*side3 + min([side1, side2, side3])
    return area


def required_ribbon(length, width, height):
    side1 = 2 * length + 2 * width
    side2 = 2 * width + 2 * height
    side3 = 2 * height + 2 * length
    ribbon_length = min(side1, side2, side3) + (length * width * height)
    return ribbon_length


# Get raw puzzle data
raw_puzzle_input = open('puzzle_data', 'r')
gift_dimensions = [line.split('x') for line in raw_puzzle_input]
# Remove last (empty) line from data
gift_dimensions = gift_dimensions[0:len(gift_dimensions) - 2]

# Strip /n from all dimensions, and convert dimensions to integers
for x in range(0, len(gift_dimensions)):
    for y in range(0, 3):
        gift_dimensions[x][y] = gift_dimensions[x][y].strip('\n')
        gift_dimensions[x][y] = int(gift_dimensions[x][y])

required_wrapping_paper_list = [required_wrapping_paper(x[0], x[1], x[2]) for x in gift_dimensions]
required_ribbon_list = [required_ribbon(x[0], x[1], x[2]) for x in gift_dimensions]

print("The elves will need %d square feet of wrapping paper and %d feet of ribbon" %
      (sum(required_wrapping_paper_list), sum(required_ribbon_list)))

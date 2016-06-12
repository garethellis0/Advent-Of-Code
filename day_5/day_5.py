# --- Day 5: Doesn't He Have Intern-Elves For This? ---
#
# Santa needs help figuring out which strings in his text file are naughty or nice.
#
# A nice string is one with all of the following properties:
#
#     It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
#     It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
#     It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
#
# For example:
#
#     ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
#     aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
#     jchzalrnumimnmhp is naughty because it has no double letter.
#     haegwjzuvuyypxyu is naughty because it contains the string xy.
#     dvszwmarrgswjxmb is naughty because it contains only one vowel.
#
# How many strings are nice?
#
# Your puzzle answer was 238.
# --- Part Two ---
#
# Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.
#
# Now, a nice string is one with all of the following properties:
#
#     It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
#     It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
#
# For example:
#
#     qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
#     xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
#     uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
#     ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
#
# How many strings are nice under these new rules?
#
# Your puzzle answer was 69.


text_file = open('data', 'r')

lines = []

for line in text_file:
    lines.append(line.strip('\n'))


# ~~~~~~~~~~~~~~~~~ Part 1 ~~~~~~~~~~~~~~~~~


def contains_3_vowels(line):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0

    for char in line:
        if char in vowels:
            vowel_count += 1
            if vowel_count >= 3:
                return True

    return False


def has_duplicate_char(line):
    for char in range(0, len(line) - 1):
        if line[char] == line[char + 1]:
            return True
    return False


def does_not_contain_bad_string(line):
    bad_strings = ['ab', 'cd', 'pq', 'xy']
    for char in range(0, len(line) - 1):
        if line[char:char + 2] in bad_strings:
            return False
    return True


def valid(line):
    if contains_3_vowels(line) and has_duplicate_char(line) and does_not_contain_bad_string(line):
        return True
    else:
        return False


valid_string_count = 0

for line in lines:
    if valid(line):
        valid_string_count += 1

print("Under the old model there are %d valid strings in the list!" % valid_string_count)


# ~~~~~~~~~~~~~~~~~ Part 2 ~~~~~~~~~~~~~~~~~

def duplicate_no_overlap(line):
    for char in range(0, len(line) - 1):
        for another_char in range(char + 2, len(line) - 1):
            if line[char: char + 2] == line[another_char:another_char + 2]:
                return True
    return False


def repeat_with_one_in_between(line):
    for char in range(0, len(line) - 2):
        if line[char] == line[char + 2]:
            return True
    return False


def valid(line):
    if duplicate_no_overlap(line) and repeat_with_one_in_between(line):
        return True
    else:
        return False

valid_string_count = 0

for line in lines:
    if valid(line):
        valid_string_count += 1

print("Under the new model there are %d valid strings in the list!" % valid_string_count)
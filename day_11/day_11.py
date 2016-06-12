import string

alphabet = list(string.ascii_lowercase)


def previous_two_char_in_alphabet(alphabet, char):
    # Gets the two characters before a given character in the alphabet
    for letter in range(2, len(alphabet)):
        if alphabet[letter] == char:
            return alphabet[letter - 2] + alphabet[letter - 1]
    return []


def has_increasing_string(password, alphabet):
    # Checks if password has at least one 3 long string of increasing characters
    # ie. 'abc', 'cde' 'ghi' 'xyz'
    for char in range(2, len(password)):
        # print(previous_two_char_in_alphabet(alphabet, password[char]))
        # print(password[char - 2:char])
        if password[char - 2:char] == previous_two_char_in_alphabet(alphabet, password[char]):
            return True
    return False

def no_invalid_characters(password):
    # Checks to make sure the password does not contain 'i', 'o', or 'l'
    for char in password:
        if char == 'i' or char == 'o' or char == 'l':
            return False
    return True


def contains_pairs(password):
    # Checks to make sure that the password contains two different, non-overlapping pairs of letters
    # ie. 'aa' 'xx'
    pair_count = 0
    for char in range(1, len(password)):
        if password[char - 1] == password[char] and password[char - 2] != password[char]:
            pair_count += 1
    if pair_count >= 2:
        return True
    else:
        return False

def valid(password, alphabet):
    # Checks if the password meets all conditions for a valid password
    if has_increasing_string(password, alphabet) and no_invalid_characters(password) and contains_pairs(password):
        return True
    else:
        return False

def next_char(char, alphabet):
    for letter in range(0, len(alphabet) - 1):
        if alphabet[letter] == char:
            if letter == len(alphabet) - 2:
                return alphabet[0]
            else:
                return alphabet[letter + 1]


def solve(password, alphabet):
    for i in range(2):
        while not valid(password, alphabet):
            r = list(password)[::-1]
            i = 0
            for c in r:
                print(password)
                if c == 'z':
                    r[i] = 'a'
                else:
                    r[i] = chr(ord(c)+1)
                    break
                i += 1
            password = ''.join(r[::-1])
            if valid(password, alphabet):
                return password


original_password = 'cqjxjnds'

# I feel bad about this section, it's digusting, but I can't be arsed to clean it up at this point
pass1 = solve(original_password, alphabet)
pass2 = solve('cqjyxyzz', alphabet)
print(pass1)
print(pass2)
# print(has_increasing_string('hijklmmn', alphabet))
# print(contains_pairs('cqjxxxyz'))





# --- Day 4: The Ideal Stocking Stuffer ---
#
# Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.
#
# To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.
#
# For example:
#
#     If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
#     If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....
#
# Your puzzle answer was 346386.
# --- Part Two ---
#
# Now find one that starts with six zeroes.
#
# Your puzzle answer was 9958218.
#
# Both parts of this puzzle are complete! They provide two gold stars: **
#
# At this point, you should return to your advent calendar and try another puzzle.
#
# Your puzzle input was iwrupvqb.

import hashlib
import datetime


def is_advent_coin2(str, zero_length):
    # Checks if a given hash digest is advent coin (starts with zero length number of zeros)
    for x in range(0, zero_length):
        if str[x] != '0':
            return False
    return True


def find_coin(base_str, zero_length):
    # Finds a advent coin with zero_length number of zeros at the start, based on given str
    ticker = 0
    hex_digest = hashlib.md5(base_str.encode('utf-8')).hexdigest()
    hash = hashlib.md5()
    # Initalize hash with given str
    hash.update(base_str.encode('utf-8'))

    while not is_advent_coin2(hex_digest, zero_length):
        present_hash = hash.copy()  # Make copy of hash
        present_hash.update(str(ticker).encode('utf-8'))  # Update copy with ticker
        hex_digest = present_hash.hexdigest()  # Get hexdigest value of hash
        ticker += 1

    return ticker - 1

ORIGINAL_KEY = 'iwrupvqb'

# ~~~~~~~~~~~~~ Part 1 ~~~~~~~~~~~~~
start_time = datetime.datetime.now()
key = ORIGINAL_KEY + str(find_coin(ORIGINAL_KEY, 5))
end_time = datetime.datetime.now()
time_taken = (end_time - start_time).microseconds

print("Found a advent coin! The key is %s and it took %d microseconds to find it" %
      (key, (end_time - start_time).microseconds))
# ~~~~~~~~~~~~~ Part 2 ~~~~~~~~~~~~~
start_time = datetime.datetime.now()
key = ORIGINAL_KEY + str(find_coin(ORIGINAL_KEY, 6))
end_time = datetime.datetime.now()
time_taken = (end_time - start_time).microseconds

print("Found a advent coin! The key is %s and it took %d seconds to find it" %
      (key, (end_time - start_time).seconds))







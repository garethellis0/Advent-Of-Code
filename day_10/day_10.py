puzzle_input = "1321131112"

def look_and_say(look):
    say = []
    ticker = 1
    for char in range(1, len(look)):
        if look[char] == look[char - 1]:
            ticker += 1
        else:
            say.append(str(ticker) + look[char - 1])
            ticker = 1
    say.append(str(ticker) + str(look[len(look) - 1]))
    return ''.join(say)

def inter_look_and_say(x, look):
    print("Working....")
    for i in range(x):
        look = look_and_say(look)
    return look

print(len(inter_look_and_say(50, puzzle_input)))

def symboltonumber(symbol):
    if symbol == "A":
        return 0
    if symbol == "C":
        return 1
    if symbol == "G":
        return 2
    if symbol == "T":
        return 3
    
def patterntonumber(pattern):
    if len(pattern) == 0:
        return 0
    symbol = pattern[-1]
    prefix = pattern[:-1]
    return 4 * patterntonumber(prefix) + symboltonumber(symbol)

print(patterntonumber("TGCCGGCCCGTGAATACCTACG"))
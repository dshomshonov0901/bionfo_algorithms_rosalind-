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

def computingfreqs(text, k):
    freqarray = {}
    for i in range(0, ((4**k))):
        freqarray[i] = 0
    for i in range(0, len(text) - k + 1):
        pattern = text[i: i+k]
        j = patterntonumber(pattern)
        freqarray[j] = freqarray[j] + 1
    print(' '.join(str(x) for x in freqarray.values()))

print(computingfreqs("ACTCGTATGGCCCCGGCACGATTGACTACCCTACGCTCTACATCCCAGGCAACCAGAGAGCCGACACTCAGAGTGCAGAGTGAAATCACAGGGGTGGACCTAATCCGGCTGGGGGAAACCATGTTACCGCGAGAGTCTGTTATCCTTACTCATGCGTAGGTGAAAGATTCTCGGAAACATTCTTCTCTGCATTCGGGTCAATAAGGACAGGCTTTAGTCGCGGAAAGACGTCGCAACGCTGGAATGTTGATCGCCATCGGACATGGTCATAGAAAAGCCACATTCAGCAGCCTATCTTGTCATCACAAGGTGGAGTAGGCTCCCGTAAAGAACGTCTGCCAAGAGGACGGAGCAAACGTATCCCCGGTAGAGCCCTGCTTTATCAGCCGGCGGTGCGATGGGTCCATGTGAGTAACCCACCTAACCGCGATAGTCGAGATTTTGCTGTTCAGAGTCGAGGGGTCTTGGTCAGACGCGCTTATAAAATCGTTATCCCGGTTACCCTTCACCGGTCCATCATTCTGATTATTTTTATAAGCCTCTTAGCTGGCACCCATACCATAACACAAATTAATCCTGATGCCTACGGCGTTGCTTGCAGCAAATCCTATGTTATGATCTC", 7))

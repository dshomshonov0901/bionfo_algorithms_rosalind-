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

def numbertosymbol(index):
    if index == 0:
        return "A"
    if index == 1:
        return "C"
    if index == 2:
        return "G"
    if index == 3:
        return "T"
def numbertopattern(index, k):
    if k == 1:
        return numbertosymbol(index)
    prefixindex = index // 4
    r = index % 4
    symbol = numbertosymbol(r)
    prefixpattern = numbertopattern(prefixindex, k-1)
    return prefixpattern + symbol

def count(text, pattern):
    count = 0
    for i in range(0,(len(text)-len(pattern))+1):
        if text[i: i+ len(pattern)] == pattern:
            count += 1
    return count

def freqwords(text, k):
    freqpatterns = []
    count_dict = {}
    for i in range(0, (len(text)- k+ 1)):
        pattern = text[i:i+k]
        count_dict[pattern] = count(text,pattern)
    maxcount = max(count_dict.values())
    print(maxcount)
    for i in range(0,(len(text)- k + 1)):
        for pattern, cnt in count_dict.items():
            if cnt == maxcount:
                freqpatterns.append(pattern)
    unique_list = list(set(freqpatterns))
    print(unique_list)

def computingfreqs(text, k):
    freqarray = {}
    for i in range(0, ((4**k))):
        freqarray[i] = 0
    for i in range(0, len(text) - k + 1):
        pattern = text[i: i+k]
        j = patterntonumber(pattern)
        freqarray[j] = freqarray[j] + 1
    return freqarray

def fasterfreqwords(text, k):
    freqpatterns = []
    freqarray = computingfreqs(text, k)
    maxcount = max(freqarray.values())
    for i in range(0, 4**k - 1):
        if freqarray[i] == maxcount:
            pattern = numbertopattern(i,k)
            freqpatterns.append(pattern)
    return freqpatterns

print(fasterfreqwords("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4))

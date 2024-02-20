a = [1,4,9,16]
b = [4,7,9,9,11]

def merge_sorted(a,b):
    c = []
    maxLen = max(len(a), len(b))
    for i in range(maxLen - 1):
        valorePiccolo = min(a[i], b[i])
        valoreGrande = max(a[i], b[i])
        c.append(valorePiccolo)
        c.append(valoreGrande)
    return c
print(merge_sorted(a,b))
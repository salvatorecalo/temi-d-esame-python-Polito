def merge(a,b):
    c = []
    i1 = 0
    i2 = 0
    Min = min(len(a),len(b))
    Max = max(len(a),len(b))
    while i1 < Min:
        c.append(a[i1])
        c.append(b[i1])
        i1+=1
    while i2 < (Max-Min):
        if Max == len(a):
            c.append(a[i2+i1])
        else:
            c.append(b[i2+i1])
        i2+=1
    return c

def main():
    a = [9,7,4,9,11]
    b = [1,4,9,16]
    print(merge(a,b))
    merge(a,b)
main()
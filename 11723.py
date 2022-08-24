import sys

M = int(sys.stdin.readline())
S = set()

for i in range(M):
    com = sys.stdin.readline()
    com = com[:-1]

    if com[1] == "d":   #add
        n = int(com[4:])
        S.add(n)
    elif com[0] == "r":   #remove
        n = int(com[6:])
        S.discard(n)
    elif com[0] == "c":   #check
        n = int(com[5:])
        if n in S:
            print(1)
        else:
            print(0)
    elif com[0] == "t":    #toggle
        n = int(com[6:])
        if n in S:
            S.remove(n)
        else:
            S.add(n)
    elif com[0] == "a":    #all
        S = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
    elif com[0] == "e":   #empty
        S = set()



#keyerror 집합에서 없는 원소를 remove하려고 할때 발생.

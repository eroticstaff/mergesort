data = "45321768"

def merge(A, B):
    i = 0
    j = 0
    C = [0]*len(A)*2
    print(A)
    Aflag = True
    Bflag = True
    for k in range(len(A)*2):
        l = len(A)
        As = A[i]
        Bs = B[j]

        if int(A[i]) < int(B[j]):
            if i < len(A) and Aflag:
                C[k] = A[i]
            if i+1 < len(A):

                i = i + 1
            else:
                Aflag=False
                C[k+1] = B[j]
                if j+1 < len(B):
                    j  +=1
                else:
                    return C
        else:
            if j < len(B) and Bflag:
                C[k] = B[j]
            if j+1 < len(B):
                j = j + 1
            else:
                Bflag=False
                C[k+1] = A[i]
                if i+1 < len(A):
                    i += 1
                else:
                    return C
    print(C)
    return C

def alhorith(data):
    n = len(data)
    A = data[0: n // 2]
    B = data[n // 2:n]
    if len(A)*2 > 1:
        A = alhorith(A)
        B = alhorith(B)
        C = merge(A,B)
        print("C",C)
        return C
    else:
        return data
print(alhorith(data))

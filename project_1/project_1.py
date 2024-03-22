import csv
import sys

d = -2

def S(A, B):
    s = -1
    if A == B:
        s = 1
    return s


def find_solution(OPT, x, y) :
    m = len(x)
    n = len(y)
    alignment_1 = ''
    alignment_2 = ''
    i = m
    j = n

    while i > 0 and j > 0:
        current_score = OPT[i][j]
        if current_score == OPT[i][j-1] + d:
            alignment_1 = "-" + alignment_1
            alignment_2 = y[j-1] + alignment_2
            j -= 1
        elif current_score == OPT[i-1][j] + d:
            alignment_1 = x[i-1] + alignment_1
            alignment_2 = "-" + alignment_2
            i -= 1
        else:
            alignment_1 = x[i-1] + alignment_1
            alignment_2 = y[j-1] + alignment_2
            i -= 1
            j -= 1
            

    while i > 0:
        alignment_1 = x[i-1] + alignment_1
        alignment_2 = "-" + alignment_2
        i -= 1
    while j > 0:
        alignment_1 = "-" + alignment_1
        alignment_2 = y[j-1] + alignment_2
        j -= 1

    return alignment_1, alignment_2, OPT[m][n]

def alignment(x, y) : 
    m = len(x)
    n = len(y)
    OPT = []
    for i in range(m+1) :
        row = []
        for j in range(n+1) :
            row.append(0)
        OPT.append(row)
    for i in range(1, m+1): 
        OPT[i][0] = i * d
    for j in range(1, n+1):
        OPT[0][j] = j * d

    for i in range(1, m+1):
        for j in range(1, n+1): 
            A = x[i-1]
            B = y[j-1]
            F_1 = OPT[i-1][j-1] + S(A, B)
            F_2 = OPT[i][j-1] + d
            F_3 = OPT[i-1][j] + d
            OPT[i][j] = max(F_1, F_2, F_3)
        
    return find_solution(OPT, x, y)

if len(sys.argv) > 1:
    input_file = sys.argv[1]
    with open(input_file, newline='') as csvfile:
        sequence_pairs = csv.reader(csvfile)
        next(sequence_pairs)
        for sequence_pair in sequence_pairs:
            sequence_1, sequence_2 = sequence_pair
            alignment_1, alignment_2, score = alignment(sequence_1, sequence_2)
            print(f"{alignment_1} {alignment_2} {score}")
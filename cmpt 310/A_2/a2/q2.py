from typing import final


success = 0
failure = 0
final_print = ""
answer = ""

d = [
    [1, 2, 3, 4, 5, 6], 
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4],
    [1, 2, 3, 4]
]

def isValid(A, B=None, C=None, D=None, E=None, F=None):
    a = False
    if(A>1):
        a = True
    if(B!=None):
        if(abs(A-B)==1 and B % 2 == 1):
            a = True
        else:
            a = False
    if(C!=None):
        if(A!=C and (B+C)==4):
            a = True
        else:
            a = False
    if(D!=None):
        if((B+D)%3==0 and D % 2 == 0): # (B+D)%3=0, D even,
            a = True
        else:
            a = False
    if(E!=None):
        if(C >= E and (D-E) % 2 == 1): # C≥E, D-E odd,
            a = True
        else:
            a = False
    if(F!=None):
        if(E<F and (E+F) % 2 == 0): # E<F, E+F even
            a = True
        else:
            a = False
    return a

print(isValid(2,1))


a = False
def solution(d,success,failure, final_print, answer):
    counterA = 0
    counterB = 0
    counterC = 0
    counterD = 0
    counterE = 0
    counterF = 0
    for i in d[0]:
        final_print = final_print + "A = " + str(i) + " "
        if(isValid(i) == False):
            final_print = final_print + "Failure\n"
            failure += 1
        else:
            # counterA += 1
            for j in d[1]:
                if(d[1].index(j) == 0):
                    final_print = final_print + "B = " + str(j) + " "
                else: 
                    final_print = final_print +"      B = " + str(j) + " "
                if (isValid(i,j) == False):
                    final_print = final_print + "Failure \n"
                    failure += 1
                else:
                    # counterB += 1
                    # if(d[1].index(j) == 0 and counterA == 1):
                    #     final_print = final_print + "A = " + str(i) + " "
                    for k in d[2]:
                        if(d[2].index(k) == 0):
                            final_print = final_print + "C = " + str(k) + " "
                        else: 
                            final_print = final_print +"            C = " + str(k) + " "
                        if (isValid(i,j,k) == False):
                            final_print = final_print + "Failure\n"
                            failure += 1 
                        else:
                            # if(d[2].index(k) == 0 and counterB == 1):
                            #     final_print = final_print + "      B = " + str(j) + " "
                            for l in d[3]:
                                if(d[3].index(l) == 0):
                                    final_print = final_print +"D = " + str(l) + " "
                                else:
                                    final_print = final_print +"                  D = " + str(l) + " "
                                if (isValid(i,j,k,l) == False):
                                    final_print = final_print + "Failure\n"
                                    failure += 1
                                else:
                                    for m in d[4]:
                                        if(d[4].index(m) == 0):
                                            final_print = final_print + "E = " + str(m) + " "
                                        else:
                                            final_print = final_print + "                        E = " + str(m) + " "
                                        if (isValid(i, j, k, l, m) == False):
                                            final_print = final_print + "Failure\n"
                                            failure += 1
                                        else:
                                            for n in d[5]:
                                                if(d[5].index(n) == 0):
                                                    final_print = final_print + "F = " + str(n) + " "
                                                else:
                                                    final_print = final_print +"                              F = " + str(n) + " "
                                                if (isValid(i, j, k, l, m, n) == False):
                                                    final_print = final_print + "Failure\n"
                                                    failure += 1
                                                else:
                                                    final_print = final_print + "Solution\n"
                                                    answer = answer + "solution " + str(success+1) + " = " + str(i) + " " + str(j)+ " " + str(k)+ " "+ str(l)+ " "+ str(m)+ " "+ str(n) + "\n"
                                                    success += 1

    print(final_print)

    print(answer)

    print("Number of failures: " + str(failure))
    print("Number of successes: " + str(success) + "\n")


solution(d,success,failure, final_print, answer)


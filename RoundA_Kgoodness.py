def Kgoodness(N, K, S):
    letters=list()
    for i in S:
        letters.append(i)
    K1=0
    for i in list(range(int(N/2))):
        if not letters[i] == letters[N-i-1] :
            K1 += 1
    return   print("Case #{}:".format(x), abs(K1-K))
  
T= int(input())
for x in range(1,T+1):
    N,K = map(int,input().split(" "))
    S = (input())
    Kgoodness(N, K, S)




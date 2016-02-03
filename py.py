A = [-1000,1000]
s = 0
p = 0
t = 0
m=2000
for a in A:
    s+=a
for i in range(len(A)-1):
    p+=A[i]
    t = abs(s-p-p)
    print t
    if t<m:
        m = t
print m
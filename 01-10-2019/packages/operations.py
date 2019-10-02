def addition(p,q):
    r=p+q
    print(r)
def prime(i):
    fact=0
    for k in range(1,i+1):
        if i%k==0:
            fact+=1
    if fact==2:
        return True
    else:
        return False
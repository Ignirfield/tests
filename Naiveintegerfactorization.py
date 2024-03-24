def isprime(b):
    o=0
    for i in range(1,(b//2)+1):
        if b%i==0:
            o+=1
    if o==1:  
        return True
    else:
        return False
    
    

def factorization(A):
    L=[]
    G=[]
    if isprime(A)==True:
        return 'A is already a prime number'
    else:
        
        for i in range(2,(A//2)+1):
            for k in range(1,100):
            
                if A%(i**k)==0 and isprime(i)==True:
                    L.append((i,k)) 
    
        for nombre in range(len(L)-1):
                if L[nombre][0]!=L[nombre+1][0]:
                    G.append(L[nombre])
        G.append(L[-1])
    return G
        
print(factorization(1277))

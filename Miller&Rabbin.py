import random
 
def power(x, y, p):
     
    res = 1;
     
    # MàJ x si x est sup ou égal à p
    x = x % p;
    while (y > 0):
         
        if (y & 1):
            res = (res * x) % p;
 
        # y doit etre pair
        y = y>>1; # y = y/2
        x = (x * x) % p;
     
    return res;
 

def miillerTest(d, n):
     
    # Prendre un nombre aléatoire dans  [2..n-2]
    
    a = 2 + random.randint(1, n - 4);
 
    x = power(a, d, n);
 
    if (x == 1 or x == n - 1):
        return True;
 
    while (d != n - 1):
        x = (x * x) % n;
        d *= 2;
 
        if (x == 1):
            return False;
        if (x == n - 1):
            return True;
 
    # Composé
    return False;
 
def isPrime( n, k):
     
    if (n <= 1 or n == 4):
        return False;
    if (n <= 3):
        return True;
 
    # Trouver r de telle sorte que n =2^d * r + 1 pour un r >= 1
    d = n - 1;
    while (d % 2 == 0):
        d //= 2;
 
    # k fois
    for i in range(k):
        if (miillerTest(d, n) == False):
            return False;
 
    return True;
 

 
def main():

    k = 4;
    
    n = int (input ("donner le nombre que vous voulez tester sa primalité :"))
    print (isPrime(n,k))
    

if __name__ == "__main__":
     main()
 



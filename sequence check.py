from math import *
import numpy as np

def sequence_check (N=100,n=10):
    "#########this is a function to calculate the probabilty of sequence with same order \n\n #########note that N >= n \n\n #########using strling formular"
    if n > N:
        raise Exception("Invalid sequence legth!", N,n)
    prob = 0.0;
    p=floor(N/n);
    for k in range(1,p+1):
        q = N-n*k
        if q <0.001:
            ln_prob = (k*n)*log(0.25)
        else:
            ln_prob = (k*n)*log(0.25)+ln_stl(k+q)-ln_stl(k)-ln_stl(q)
        prob += ((-1)**(k+1))*exp(ln_prob)
    
    return prob

def ln_stl (N=50):
    "###########to calculate gamma with strling formula as alternative"
    if N<51:
        return log(gamma(N+1))
    else :
        return (0.5)*log(2*pi*N)+N*log(N/e)

def main():
    p=sequence_check(N=30000,n=19)
    print(p)
    np.array

main()
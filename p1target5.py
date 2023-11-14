def jacobi(k,n,exec_feedback):
    
    if k<0 or n%2 == 0:
        raise ValueError("'K' has to be positive and 'n' has to be an odd integer.")  
        
    
    k %= n
    jacobi = 1
    exec_feedback['approach_level']=1
    while k>0:
        print(f"Here  k is {k} and n is {n}")
        while k%2==0:
            k/=2
            r = n % 8 
            print(f"here k is {k} and n is {n} and r is {r}")
            if r == 3 or r == 5:
                jacobi = -jacobi 
            
        n,k = k,n 
        print(f"Done swapping k is {k} and n is {n}")
        
        if k % 4 == 3 and   n % 4 == 3:
            jacobi = -jacobi 
        k %= n 
    if n==1:
        exec_feedback['approach_level']=0
        return jacobi 
    
    exec_feedback['TargetReached'],exec_feedback['approach_level']=True,None
    return 0 # Target 5
def jacobi(k,n,exec_feedback):
    approach_level=0
    exec_feedback['approach_level']=approach_level
    if k<0 or n%2 == 0:
       
        exec_feedback['TargetReached'],exec_feedback['approach_level']=True,None
        raise ValueError("'K' has to be positive and 'n' has to be an odd integer.")  # TARGET 1
        
    
    k %= n
    jacobi = 1
    while k>0:
        while k%2==0:
            k/=2
            r = n % 8 
            if r == 3 or r == 5:
                jacobi = -jacobi 
            
        n,k = k,n 

        if k % 4 == 3 and   n % 4 == 3:
            jacobi = -jacobi
        k %= n 
    
    if n==1:
        return jacobi 
    
    return 0 



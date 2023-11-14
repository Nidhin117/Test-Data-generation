
BIG = (10**50) + 151
BIG_TWO = 2

def compareTo(a,b):
    if a == b:
        return 0
    elif a < b:
        return -1
    else:
        return 1




class Point(object):
    x = None
    y = None

    def __init__(self, x,  y): 
        self.x = x
        self.y = y
        

    
    def __str__(self):
        return f"({self.x},{self.y})" 
    

class Triple(object):
    x = None
    y = None
    b = None

    def __init__(self, x,  y,  b):
        self.x = x
        self.y = y 
        self.b = b 
    

    def __str__(self):
        return f"({self.x},{self.y},{self.b})"    


def cipolla(ns,ps,exec_feedback) :
    
    n = int(ns)
    p = None

    if ps == '' or ps == None:
        p = BIG 
    else:
        p = int(ps)

    ls = lambda  a :  pow(a,(p-1)//2,p)
    

    #  Step 0, validate arguments
    
    if ls(n) != 1:
        print("A") 
        exec_feedback['approach_level']=2
        exec_feedback['bd_a'] = ls(n) 
        exec_feedback['bd_b'] = 1
        triple = Triple(0,0,False)
        return triple
    

    # Step 1, find a, omega2
    a = 0
    omega2 = None
    frequency = 1
    while (True):
        if(frequency >= 15):
            break
        omega2 = (((a*a) + p) - n) % p 
        if ls(omega2) == p-1:
             
            print("B") # Target 2
            break

        print("C") # Target 3
        frequency += 1
        a += 1
    

    #  multiplication in Fp2
    finalOmega = omega2
    def mul(aa: Point, bb: Point):
        return Point(
            ((aa.x * bb.x) + (aa.y * bb.y * finalOmega)) % p,
            ((aa.x * bb.y) + (bb.x * aa.y)) % p
        )
    
    

    # Step 2, compute power
    r = Point(1, 0)
    s = Point(a, 1)
    nn =  ((p + 1) >> 1) % p

    exec_feedback['approach_level']=1
    exec_feedback['bd_a'] = compareTo(nn,0) 
    exec_feedback['bd_b'] = 0
    while (compareTo(nn,0) > 0):
        
        exec_feedback['approach_level']=0
        exec_feedback['bd_a'] = nn & 1 
        exec_feedback['bd_b'] = 1
        if (nn & 1) == 1 :
            exec_feedback['TargetReached'],exec_feedback['approach_level']=True,None

            print("D") # Target 4
            r = mul(r, s)
        
        print("E")
        s = mul(s, s)
        nn = nn >> 1
    

    #  Step 3, check x in Fp
    if r.y != 0:
        print("F")
        return Triple(0, 0, False)
    

    #  step 5, check x * x = n
    if ((r.x * r.x) % p) != n: 
        print("G")
        return Triple(0, 0, False)
    

    #  Step 4, solutions
    print("H")
    return Triple(r.x, p - r.x, True)
    

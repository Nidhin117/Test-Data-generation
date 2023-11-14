import random as rd
# import sys
from math import sqrt
from p2target1 import cipolla as cp1
from p2target2 import cipolla as cp2
from p2target3 import cipolla as cp3
from p2target4 import cipolla as cp4
from p2target5 import cipolla as cp5
from p2target6 import cipolla as cp6
from p2target7 import cipolla as cp7

#print (sys.maxsize)


ip_domain_min=0
ip_domain_max=10000000 #sys.maxsize

#function to calculate actual fitness value
def calc_fitness(approach_level,branch_dist):
    #fit(t,i) = approach level(t,i) + normalise(branch distance(t,i))
    #normalise(d) = 1 - 1.001 pow -d
    normalised_brndist= 1 - pow(1.001, -branch_dist)
    fit= approach_level + normalised_brndist
    return fit

#Function to calculate branch distance for target 1
def calc_branchdist_t1(a,b,approach_level):
    #condition is (ls(n) != 1) . a= ls(n) , b= 1
    #formula for a!=b => if abs(a-b)!=0 then 0 else k
    #values for a and b are received as feedback by executing cipolla function
    if approach_level==0: #if (ls(n) != 1):
        constant=100
        if abs(a-b) != 0:
            cost1=0
        else:
            cost1 = constant
        branch_dist= cost1
    return branch_dist

#Function to calculate branch distance for target 2
def calc_branchdist_t2(a,b,approach_level):
    #condition is ls(omega2) == p-1 . a= ls(omega2) , b= p-1
    #formula for a==b => if abs(a-b)=0 then 0 else abs(a-b)+K
    #values for a and b are received as feedback by executing cipolla function
    #approach level 1 is when code returns from condition ls(n) != 1
    #target 2 can be reached only if ls(n) != 1 is not satisfied.
    constant=100
    if approach_level == 0  or approach_level == 1: #if ls(omega2) == p-1: or ls(n) != 1: should not be satisfied, so checking for ls(n) == 1:
        if abs(a-b)== 0:
            cost1=0
        else:
            cost1=abs(a-b)+constant
        branch_dist= cost1
    return branch_dist

#Function to calculate branch distance for target 3
def calc_branchdist_t3(a,b,approach_level):
    #target 3 can be reached only if previous if condition ls(omega2) == p-1 is not satisfied
    #hence the new condition to reach target is ls(omega2) != p-1 . a= ls(omega2) , b= p-1
    #formula for a!=b => if abs(a-b)!=0 then 0 else k
    #values for a and b are received as feedback by executing cipolla function
    #approach level 1 is when code returns from condition ls(n) != 1
    #target 2 can be reached only if ls(n) != 1 is not satisfied.
    constant = 100
    if approach_level == 0 : #ls(omega2) != p-1
        if abs(a-b) != 0:
            cost1=0
        else:
            cost1 = constant
        branch_dist= cost1
    elif approach_level==1: #ls(n) != 1: should not be satisfied, so checking for ls(n) == 1:
        if abs(a-b)== 0:
            cost1=0
        else:
            cost1=abs(a-b)+constant
        branch_dist= cost1
    return branch_dist

#Function to calculate branch distance for target 4
def calc_branchdist_t4(a,b,approach_level):
    #condition at approach level 0 (nn & 1) == 1 . a= (nn & 1) , b= 1
    #condition at approach level 1 (compareTo(nn,0) > 0) . a= compareTo(nn,0) , b= 0
    #formula for a==b => if abs(a-b)=0 then 0 else abs(a-b)+K
    #formula for a > b => if b-a < 0 then 0 else (b-a) + k
    #values for a and b are received as feedback by executing cipolla function
    constant = 100
    if approach_level == 0 or approach_level==2: #(nn & 1) == 1 : or ls(n) != 1: should not be satisfied, so checking for ls(n) == 1:
        if abs(a-b)== 0:
            cost1=0
        else:
            cost1=abs(a-b)+constant
        branch_dist= cost1
    elif approach_level==1 : #while(compareTo(nn,0) > 0)
        if (b-a)<0:
            cost1=0
        else:
            cost1= (b-a)+constant
        branch_dist = cost1
    return branch_dist

#Function to calculate branch distance for target 5
def calc_branchdist_t5(a,b,approach_level):
    #condition at approach level 0 r.y != 0 . a= r.y, b= 0
    #formula for a!=b => if abs(a-b)!=0 then 0 else k
    #values for a and b are received as feedback by executing cipolla function
    constant=100
    if approach_level==0: #if r.y != 0:
        if abs(a-b) != 0:
            cost1=0
        else:
            cost1 = constant
        branch_dist= cost1
    elif approach_level==1: #ls(n) != 1: should not be satisfied, so checking for ls(n) == 1:
        if abs(a-b)== 0:
            cost1=0
        else:
            cost1=abs(a-b)+constant
        branch_dist= cost1
    return branch_dist

#Function to calculate branch distance for target 6
def calc_branchdist_t6(a,b,approach_level):
    #condition at approach level 0 (r.x * r.x) % p) != n . a= (r.x * r.x) % p) , b= n
    #formula for a!=b => if abs(a-b)!=0 then 0 else k
    #values for a and b are received as feedback by executing cipolla function
    constant=100
    if approach_level==0: #if (r.x * r.x) % p) != n:
        if abs(a-b) != 0:
            cost1=0
        else:
            cost1 = constant
        branch_dist= cost1
    elif approach_level==2  or approach_level == 1: #ls(n) != 1: should not be satisfied, so checking for ls(n) == 1 OR r.y != 0: so checking r.y == 0:
        if abs(a-b)== 0:
            cost1=0
        else:
            cost1=abs(a-b)+constant
        branch_dist= cost1
    return branch_dist

#Function to calculate branch distance for target 7
def calc_branchdist_t7(a,b,approach_level):
    #target 3 can be reached only if previous if condition ((r.x * r.x) % p) != n is not satisfied
    #and also if previous if condition ls(n) != 1 is not satisfied
    #hence the new condition to reach target at level 0 is ((r.x * r.x) % p) == n  . a= ((r.x * r.x) % p) , b= n
    #and new condition at level 1 is ls(n) == 1. a= ls(n) , b= 1
    #formula for a==b => if abs(a-b)=0 then 0 else abs(a-b)+K
    #values for a and b are received as feedback by executing cipolla function
    constant=100
    if approach_level==0 or approach_level==1 or approach_level == 2: #if ((r.x * r.x) % p) == n :
        if abs(a-b)== 0:
           cost1=0
        else:
           cost1=abs(a-b)+constant
        branch_dist= cost1
    # elif approach_level==1: #ls(n) != 1: should not be satisfied, so checking for ls(n) == 1:
    #     if abs(a-b)== 0:
    #         cost1=0
    #     else:
    #         cost1=abs(a-b)+constant
    #     branch_dist= cost1
    return branch_dist


class Individual(object):
    # Class representing individual in population

    def __init__(self, testcase,target):
        self.testcase = testcase
        #print(f"In constructor for {testcase}")
        self.fitness = self.execute_func(testcase,target)

    
    
    #function for creating an individual test data as input variable
    @classmethod
    def create_individual(self):
        #select two random numbers between minimum and maximum integer values defined
        #for the second integer, pick the closest prime number
        ele=[]
        num1= rd.randint(ip_domain_min, ip_domain_max)
        ele.append(num1)        
        num2=rd.randint(ip_domain_min, ip_domain_max)
        # if num2 <= 2:
        #     num2=3
        # isprime = chk_prime(num2)
        # if not isprime:
        #     num2=closest_prime(num2)
        ele.append(num2)             
        return ele
    
    
    #function that interacts with Cipolla probgram  to 
    #identify best test data for each target
    @staticmethod
    def execute_func(testcase,target):
        feedback={'TargetReached':False,'approach_level':None,'bd_a':None,'bd_b':None}
        # print(f"In exec func{testcase}")
        k,n=testcase
        # print(f"In exec func K and N is {k}, {n}")
        #dynamically invoke cipolla function from differnt files
        #calls cp1, cp2, cp3, cp4,cp6,cp7 based on current value for target
        j=target_pack_map[target](str(k),str(n),feedback)
        # print(f"In exec func Feedback is{feedback}")
        if feedback['TargetReached']: 
            # print("In exec func Target has been reached")
            return 0 # return 0 as fitness as target reached
        else:
            # print("In exec func Target has not been reached")
            #calculate branch distance for  each target 
            #pass the value for "a" and "b" to be used in formula for calculation
            #of branch distance 
            # print(f"In exec func Feedback a, b {feedback['bd_a']} {feedback['bd_b']}")
            branch_distance=target_function_map[target](feedback['bd_a'],feedback['bd_b'],feedback['approach_level'])
            # print(f"In exec func Branch distace {branch_distance}")
            #calcuate actual fitness value which is a sum of approach
            #level and normalized branch distance
            fitness=calc_fitness(feedback['approach_level'],branch_distance)
            # print(f"In exec func Fitness is {fitness}")
            return fitness


population=[]
total_population=35
found=False
all_test_dataset={}
generation = 1

#create a dictionary to map branch distance calculation function for each target
target_function_map = {'target1':calc_branchdist_t1,'target2':calc_branchdist_t2,'target3':calc_branchdist_t3,'target4':calc_branchdist_t4,'target5':calc_branchdist_t5,'target6':calc_branchdist_t6,'target7':calc_branchdist_t7}
#target_function_map = {'target7':calc_branchdist_t7}

#create a dictionary to map cipolla function to be called for each target
target_pack_map = {'target1':cp1,'target2':cp2,'target3':cp3,'target4':cp4,'target5':cp5,'target6':cp6,'target7':cp7}

#Loop through each target and run the GA for each target
#Main Driver code 
def main():
    for current_target in list(target_function_map.keys()):
        generation = 1
        population=[]
        found = False
        print(f"In main loop for target {current_target}")
        #Create a population of individual test data which is a list of two integers
        #first element in list is a regular integer and 2nd element in the list is a prime number
        for _ in range(total_population):
            test_data=Individual.create_individual()
            # print(f"In main loop {test_data}")
            test_obj=Individual(test_data,current_target)
            population.append(test_obj)
            

        while not found:
            #sort the population in the decreasing order of their fitness
            population = sorted(population, key=lambda x: x.fitness)
            # print("In main loop Done with sorting")

            #evaluate the initial population, if taget has been reached, exit and move  on to next target
            #Set a termination criteria incase the target is not reached. Exit after 500 generations
            if generation >= 600:
                all_test_dataset[current_target] = {'Test data':None,'Generation':generation}
                break
            
            if population[0].fitness==0:
                found=True
                res = f"Solution for {current_target}:: Gen:{generation} score:{population[0].fitness} testdata:{population[0].testcase}"
                all_test_dataset[current_target] = {'Test data':population[0].testcase,'Generation':generation}
                print(f"In main loop {res}")
                break

            else:
                    print(f"Not found gen: {generation}")
                    generation += 1

    print(f"result dictionary:: {all_test_dataset}")


if __name__ == '__main__':
    main()
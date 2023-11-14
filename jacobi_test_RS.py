import random as rd
from p1target1 import jacobi as jb1
from p1target2 import jacobi as jb2
from p1target3 import jacobi as jb3
from p1target4 import jacobi as jb4
from p1target5 import jacobi as jb5

# population = []
total_population = 5
all_test_dataset={}
ip_domain_min=0
ip_domain_max=1000

def calc_fitness(approach_level,branch_dist):
    #fit(t,i) = approach level(t,i) + normalise(branch distance(t,i))
    #normalise(d) = 1 - 1.001 pow -d
    normalised_brndist= 1 - pow(1.001, -branch_dist)
    fit= approach_level + normalised_brndist
    return fit

def calc_branchdist_t1(k,n,approach_level):
    #k<0 => if (a-b)<0 then 0 else (a-b)+k
    #n%2 == 0 => if abs(a-b)=0 then 0 else abs(a-b)+k
    #OR => min (cost(a),cost(b))
    if approach_level==0: #only one approach level for target 1
        constant=100
        if (k-0) < 0:
            cost1=0
        else:
            cost1=(k-0) + constant
        if abs((n%2)-0)== 0:
            cost2=0
        else:
            cost2=abs((n%2))+constant
        branch_dist= min(cost1,cost2)
    return branch_dist

def calc_branchdist_t2(k,n,approach_level):
    #r==3 => if abs(a-b)=0 then 0 else abs(a-b)+k
    #r==5 => if abs(a-b)=0 then 0 else abs(a-b)+k
    #OR => min (cost(a),cost(b))
    #from code we see r= n%8 so r is replaced with n%8
    constant=100
    if approach_level == 0 : #if r == 3 or r == 5:
        if abs((n%8)-3)== 0:
            cost1=0
        else:
            cost1=abs((n%8)-3)+constant
        if abs((n%8)-5)== 0:
            cost2=0
        else:
            cost2=abs((n%8)-5)+constant
        branch_dist= min(cost1,cost2)
    elif approach_level==1 : #while k%2==0
        if abs((k%2)-0)== 0:
            cost1=0
        else:
            cost1=abs((k%2)-0)+constant
        branch_dist = cost1
    elif approach_level==2: #while target k>0
        #if b-a < 0 then 0 else (b-a) + k
        if (0-k)<0:
            cost1=0
        else:
            cost1= (0-k)+constant
        branch_dist = cost1
    elif approach_level==3:
        branch_dist=calc_branchdist_t1(k,n,0)
    return branch_dist

def calc_branchdist_t3(k,n,approach_level):
    #k%4==3 => if abs(a-b)=0 then 0 else abs(a-b)+k
    #n%4==3 => if abs(a-b)=0 then 0 else abs(a-b)+k
    #AND => cost(a) + cost(b)
    constant = 100
    if approach_level == 0 : #if k % 4 == 3 and   n % 4 == 3:
        if abs((k%4)-3)== 0:
            cost1=0
        else:
            cost1=abs((k%4)-3)+constant
        if abs((n%4)-3)== 0:
            cost2=0
        else:
            cost2=abs((n%4)-3)+constant
        branch_dist= cost1+cost2
    elif approach_level==1 : #while target k>0
        #if b-a < 0 then 0 else (b-a) + k
        if (0-k)<0:
            cost1=0
        else:
            cost1= (0-k)+constant
        branch_dist = cost1
    elif approach_level==3:
        branch_dist=calc_branchdist_t1(k,n,0)
    return branch_dist


def calc_branchdist_t4(k,n,approach_level):
    #n==1 => if abs(a-b)=0 then 0 else abs(a-b)+k
    constant = 100
    if approach_level == 0 : #if k % 4 == 3 and   n % 4 == 3:
        if abs(n-1)== 0:
            cost1=0
        else:
            cost1=abs(n-1)+constant
        branch_dist = cost1
    elif approach_level==1 : #while target k>0
        #if b-a < 0 then 0 else (b-a) + k
        if (0-k)<0:
            cost1=0
        else:
            cost1= (0-k)+constant
        branch_dist = cost1
    elif approach_level==3:
        branch_dist = calc_branchdist_t1(k,n,0)
    return branch_dist

def calc_branchdist_t5(k,n,approach_level):
    #n!=1 => if abs(a-b)!=0 then 0 else k
    constant = 100
    if approach_level == 0 : #if k % 4 == 3 and   n % 4 == 3:
        if abs(n-1)!= 0:
            cost1=0
        else:
            cost1=constant
        branch_dist = cost1
    elif approach_level==1 : #while target k>0
        #if b-a < 0 then 0 else (b-a) + k
        if (0-k)<0:
            cost1=0
        else:
            cost1= (0-k)+constant
        branch_dist = cost1
    elif approach_level==3:
        branch_dist = calc_branchdist_t1(k,n,0)
    return branch_dist

target_function_map = {'target1':calc_branchdist_t1,'target2':calc_branchdist_t2,'target3':calc_branchdist_t3,'target4':calc_branchdist_t4,'target5':calc_branchdist_t5}
target_pack_map = {'target1':jb1,'target2':jb2,'target3':jb3,'target4':jb4,'target5':jb5}

class Individual(object):
    # Class representing individual in population

    def __init__(self, testcase,target):
        self.testcase = testcase
        #print(f"In constructor for {testcase}")
        self.fitness = self.execute_func(testcase,target)

    
    
    #function for creating a population of test data input variables
    @classmethod
    def create_individual(self):
        ele=[]
        num1= rd.randint(ip_domain_min, ip_domain_max)
        ele.append(num1)
        num2=rd.randint(ip_domain_min, ip_domain_max)
        ele.append(num2)
        return ele
    
    #function for crossover and mutation    
    # def crossover_mutation(self,par2,target):
    #     par1 = self.testcase
    #     child=[]
    #     #get a random crossover probablity to pick between 2 parents
    #     prob = rd.random()
    #     print(prob)
    #     if prob < 0.35:
    #         child=rd.choice(list(zip(par1,par2)))
    #     elif prob < 0.7:
    #         child=rd.choice(list(zip(par2,par1)))
    #     else:
    #         #performing Uniform radom mutation by add interger 1
    #         child=[x+1 for x in par2 ] #adds 1 to each element in list
    #     return Individual(child,target)
    
    #function that interacts with jacobi probgram  to 
    #identify best test data for each target
    @staticmethod
    def execute_func(testcase,target):
        feedback={'TargetReached':False,'approach_level':None}
        try:
            k,n=testcase
            print(k,n)
            #jb1(k,n,feedback)
            #dynamically invoke jacobi function from differnt files
            #calls jb1, jb2, jb3, jb4,jb5 based on current value for target
            j=target_pack_map[target](k,n,feedback)
            print(f"In try {feedback}")
            if feedback['TargetReached']: 
                print("Target has been reached")
                return 0 # return 0 as fitness as target reached
            else:
                print("Target has not been reached")
                #calculate branch distance for  each target 
                #branch_distance=calc_branchdist_t1(k,n) 
                branch_distance=target_function_map[target](k,n,feedback['approach_level'])
                print(f"Branch distace {branch_distance}")
                #calcuate actual fitness value which is a sum of approach
                #level and normalized branch distance
                fitness=calc_fitness(feedback['approach_level'],branch_distance)
                print(f"Fitness is {fitness}")
                return fitness
        except Exception as e:
            print (str(e))
            print(feedback)
            if feedback['TargetReached']:
                print("Target has been reached")
                return 0 # return 0 as fitness as target reached
            else:
                #if it goes into first exception,
                #assuming highest approach level to be 3
                print("Going to calc bd for exception case")
                branch_distance=target_function_map[target](k,n,3)
                fitness=calc_fitness(3,branch_distance)
                return fitness

def main():
    print(f"Try:: {list(target_function_map.keys())}")
    for current_target in list(target_function_map.keys()):
        population=[]
        found = False
        generation = 1

        for _ in range(total_population):
            test_data=Individual.create_individual()
            
            print(test_data)
            test_obj=Individual(test_data,current_target)
            population.append(test_obj)
        print(f"Population created for gen: {generation}")
        while not found:
            if generation >= 100:
                print("Generation reached 100")
                all_test_dataset[current_target] = {'Test data':population[0].testcase,'Generation':generation}
                break
            population = sorted(population, key=lambda x: x.fitness)
            if population[0].fitness==0:
                found=True
                res = f"Solution for {current_target}:: Gen:{generation} score:{population[0].fitness} testdata:{population[0].testcase}"
                all_test_dataset[current_target] = {'Test data':population[0].testcase,'Generation':generation}
                print(res)
                break
            else:
                print(f"Not found gen: {generation}")
                generation += 1
        
    
    print(f"result dictionary:: {all_test_dataset}")

if __name__ == "__main__":
    print("callin main")
    main()
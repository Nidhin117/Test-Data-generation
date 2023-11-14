import random as rd
import math
from p1target1 import jacobi as jb1
from p1target2 import jacobi as jb2
from p1target3 import jacobi as jb3
from p1target4 import jacobi as jb4
from p1target5 import jacobi as jb5

#print (sys.maxsize)

ip_domain_min=0
ip_domain_max=1000
elitism_rate= 10
crossover_rate=0.7
mutation_rate=0.1

#function that returns fittest parent among two parents
def select_fitter(ind1,ind2):
    if ind1.fitness < ind2.fitness:
        return ind1
    else:
        return ind2

#Function that is used for calculation of actual fiteness
def calc_fitness(approach_level,branch_dist):
    #fit(t,i) = approach level(t,i) + normalise(branch distance(t,i))
    #normalise(d) = 1 - 1.001 pow -d
    normalised_brndist= 1 - pow(1.001, -branch_dist)
    fit= approach_level + normalised_brndist
    return fit

#Function to calculate branch distance for target 1
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

#Function to calculate branch distance to avoid raise value exception
def calc_bd_not_exception(k,n,approach_level):
    # will be opposite of k<0 or n%2 == 0, so actual condition is k>0 or n%2!=0
    #only then path will not lead to the first exception
    #k>0 =>if b-a < 0 then 0 else (b-a) +k
    #n%2!=0=>if abs(a-b)!=0 then 0 else K
    constant=100 
    if (0-k) < 0:
        cost1= 0
    else:
        cost1= (0-k)+ constant
    if abs((n%2)-0) != 0:
            cost2=0
    else:
        cost2=constant
    branch_dist= min(cost1,cost2)
    return branch_dist

#Function to calculate branch distance for target 2
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
    elif approach_level==3: #when it goes into raise value error exception
        branch_dist=calc_bd_not_exception(k,n,0)
    return branch_dist

#Function to calculate branch distance for target 3
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
    elif approach_level==3: #when it goes into raise value error exception
        branch_dist=calc_bd_not_exception(k,n,0)
    return branch_dist

#Function to calculate branch distance for target 4
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
    elif approach_level==3: #when it goes into raise value error exception
        branch_dist = calc_bd_not_exception(k,n,0)
    return branch_dist

#Function to calculate branch distance for target 5
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
    elif approach_level==3: #when it goes into raise value error exception
        branch_dist = calc_bd_not_exception(k,n,0)
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
        ele=[]
        num1= rd.randint(ip_domain_min, ip_domain_max)
        ele.append(num1)
        num2=rd.randint(ip_domain_min, ip_domain_max)
        ele.append(num2)
        return ele
    
    #function for crossover 
    @classmethod    
    def crossover(self,par1,par2,target):
        #Based on cross over rate perform crossover or send parentes as it is to next generation
        child1=[]
        child2=[]
        prob = rd.random()
        if prob < crossover_rate:
           child1=rd.choice(list(zip(par1.testcase,par2.testcase)))
           child2=rd.choice(list(zip(par2.testcase,par1.testcase)))
        else:
            child1,child2=par1.testcase,par2.testcase
        return Individual(list(child1),target), Individual(list(child2),target)
    
    #Function to perform mutation
    @classmethod
    def mutation(self,new_generation,target):
        #Based on mutation rate pick percentage of population and mutate them
        for i in range (0,math.ceil(mutation_rate*total_population)):
            child_idx=rd.randint(0,len(new_generation)-1)
            print(f"childidx {child_idx},{new_generation[child_idx].testcase}")

            #Performing uniform random mutation by addition the testcases by 1
            mutant = [x+1 for x in new_generation[child_idx].testcase ]
            # new_generation[child_idx]=[x+1 for x in new_generation[child_idx] ]
            mutant=Individual(mutant,target)
            print(mutant.testcase)
            new_generation[child_idx]=mutant
        return  new_generation

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


# population=[]
total_population=5
# found=False
all_test_dataset={}
# generation = 1


#create a dictionary to map branch distance calculation function for each target
target_function_map = {'target1':calc_branchdist_t1,'target2':calc_branchdist_t2,'target3':calc_branchdist_t3,'target4':calc_branchdist_t4,'target5':calc_branchdist_t5}

#create a dictionary to map jacobi function to be called for each target
target_pack_map = {'target1':jb1,'target2':jb2,'target3':jb3,'target4':jb4,'target5':jb5}

#Loop through each target and run the GA for each target
#Main Driver code 
for current_target in list(target_function_map.keys()):
    generation = 1
    population=[]
    found = False

    #Create a population of individual test data which is a list of two integers
    for _ in range(total_population):
        test_data=Individual.create_individual()
        print(test_data)
        test_obj=Individual(test_data,current_target)
        population.append(test_obj)
        

    while not found:
        #sort the population in the decreasing order of their fitness
        population = sorted(population, key=lambda x: x.fitness)

        print("Done with sorting")

        #evaluate the initial population, if taget has been reached, exit and move  on to next target
        if population[0].fitness==0:
            found=True
            res = f"Solution for {current_target}:: Gen:{generation} score:{population[0].fitness} testdata:{population[0].testcase}"
            all_test_dataset[current_target] = {'Test data':population[0].testcase,'Generation':generation}
            print(res)
            break

        #Set a termination criteria incase the target is not reached. Exit after 500 generations
        if generation >= 500:
            all_test_dataset[current_target] = {'Test data':None,'Generation':generation}
            break
            
        # Otherwise generate new generation
        new_generation = []

        # Perform Elitism and include top 10% of fittest parents into next generation
        s = int((10*total_population)/100)
        new_generation.extend(population[:s])
        print(f"Done with elitism {new_generation}")

        while len(new_generation) < total_population:
            ind1 = rd.choice(population)
            ind2 = rd.choice(population)
            parent1 = select_fitter(ind1,ind2)
            ind3 = rd.choice(population)
            ind4 = rd.choice(population)
            parent2 = select_fitter(ind3,ind4)
            print(f"In Main loop {parent1.testcase},{parent2.testcase}")
            child1,child2=Individual.crossover(parent1,parent2,current_target)
            print(f"Done with crossover  {child1.testcase},{child2.testcase}")
            new_generation.append(child1)
            new_generation.append(child2)

        print(len(new_generation))
        new_generation2=Individual.mutation(new_generation,current_target)

        population = new_generation2

        generation += 1
 
print(f"result dictionary:: {all_test_dataset}")
    

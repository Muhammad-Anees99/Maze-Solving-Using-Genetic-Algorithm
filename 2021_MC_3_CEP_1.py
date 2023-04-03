from pyamaze import *
from random import *
import csv
ROW_SIZE=15
COLUMN_SIZE=15
path,path_coordinates,infeasible_,Actual_Fitness=[],[],[],[]
Iteration_Num=0
fittest_found=0
weight_l,weight_f,weight_t=2,3,3
a=maze(ROW_SIZE,COLUMN_SIZE)
a.CreateMaze(ROW_SIZE,COLUMN_SIZE,loopPercent=100)
pr_sol=agent(a,1,1,footprints=True,color='red')
grid=a.maze_map
POPULATION_SIZE=500
#User defined functions
#random population
def Generate_population():
        return [[[1]+[randint(1,ROW_SIZE) for _ in range (COLUMN_SIZE-2)]+[ROW_SIZE],[randint(0,1) for _ in range(2)]] for _ in range (POPULATION_SIZE)]
# Turns counting function
def Total_Turns():
    return [sum([1 for i in range(COLUMN_SIZE-1) if chromosome[i]!=chromosome[i+1]]) for chromosome,orient in population]
# pathlegth,infeasible finding function
def Fitness_Function(popList):
    chromosome, [orientation, direction] = popList
    infeasible_=[]
    path=[]
    if fittest_found==1:
        path.append((1,1))
    if ROW_SIZE!=COLUMN_SIZE:
        orientation=0
    decide=orientation^direction
    pre_coordinate,inc,infeasible_=(1,1),1,[]
    for i in range (0,len(chromosome)-1):
        next_move=i+1
        control=(chromosome[i+1]+1) if chromosome[i+1]>chromosome[i] else (chromosome[i+1]-1)
        while inc!= control:
            if orientation==0:
                popst_coordinate=(inc,next_move+decide)
            else:
                popst_coordinate=(next_move+decide,inc)
            if fittest_found==1 and popst_coordinate not in ((1,1),(ROW_SIZE,COLUMN_SIZE)):
                path.append(popst_coordinate)
            if popst_coordinate[0]-pre_coordinate[0]!=0:
                if popst_coordinate[0]-pre_coordinate[0]>0:
                    if grid[pre_coordinate]['S']==0:
                            infeasible_.append(1)
                    else:
                        infeasible_.append(0)
                else:
                    if grid[pre_coordinate]['N']==0:
                            infeasible_.append(1)
                    else:
                        infeasible_.append(0)
            elif popst_coordinate[1]-pre_coordinate[1]!=0:
                if popst_coordinate[1]-pre_coordinate[1]>0:
                    if grid[pre_coordinate]['E']==0:
                            infeasible_.append(1)
                    else:
                        infeasible_.append(0)
                else:
                    if grid[pre_coordinate]['W']==0:
                            infeasible_.append(1)
                    else:
                        infeasible_.append(0)
            pre_coordinate=popst_coordinate
            if chromosome[i+1]>chromosome[i]:
                    inc+=1
            else: 
                    inc-=1
        if chromosome[i+1]>chromosome[i]:
            inc-=1
        else:
            inc+=1
    if fittest_found==1:
        path.append((ROW_SIZE,COLUMN_SIZE))
        return path,len(infeasible_),sum(infeasible_)
    return len(infeasible_),sum(infeasible_)   
# generating half population 
def Cross_over(chromosome):
    cross_point=randint(2,COLUMN_SIZE-2)
    let=int(POPULATION_SIZE/2)
    for i in range (let,(POPULATION_SIZE-1),2):
        chromosome[i][0]=chromosome[i-let][0][0:cross_point]+chromosome[i-let+1][0][cross_point:]
        chromosome[i+1][0]=chromosome[i-let+1][0][0:cross_point]+chromosome[i-let][0][cross_point:]
# muatates 
def Mutation(chromosome):
    for i in range (POPULATION_SIZE):
        chromo,bits=chromosome[i]
        chromo[randint(2,COLUMN_SIZE-2)]=randint(1,ROW_SIZE)
        if i>=int(POPULATION_SIZE/2):
            bits[0],bits[1]=randint(0,1),randint(0,1)
# Actual fitness calculator
def fitness(turns, length, infeasible):
    inf_min=0
    f_t=1-(turns-min(Turn))/(max(Turn)-min(Turn))
    f_l=1-(length-min(path_coordinates))/(max(path_coordinates)-min(path_coordinates))
    f_inf=1-(infeasible-inf_min)/(max(infeasible_)-inf_min)
    return (100*weight_f*f_inf)*((weight_l*f_l)+(weight_t*f_t))/(weight_l+weight_t)
#sorts population according to fitness
def Sort_pop(population,Turn,Actual_Fitness):
    pop=list(zip(population,Actual_Fitness))
    Sorted_pop=sorted(pop,key= lambda x: x[1],reverse=True)
    population=[x[0] for x in Sorted_pop]
    t=list(zip(Turn,Actual_Fitness))
    Sorted_t=sorted(t,key= lambda x: x[1],reverse=True)
    Turn=[x[0] for x in Sorted_t]
    return population,Turn,Actual_Fitness
#store data in csv
def store():
    with open('data16.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([min(infeasible_), min(Turn),min(path_coordinates),max(Actual_Fitness),Iteration_Num])
#Main
population=Generate_population()
Turn=Total_Turns()        
while(Iteration_Num<10000):
    print(f'Current Iteration No.: {Iteration_Num}')       
    inf=[Fitness_Function(chromosome) for chromosome in population]
    for i in range (POPULATION_SIZE):
        path_coordinates.append(inf[i][0]); infeasible_.append(inf[i][1])
    for i in range (POPULATION_SIZE):
        fit=fitness(Turn[i], path_coordinates[i], infeasible_[i])
        Actual_Fitness.append(fit)
        if infeasible_[i]==0:
            fittest_found=1
            Path_solution, Path_solution_coordinates, Solution_infeasible = Fitness_Function(population[i])
            Solution_Turn = Turn[i]
            print(population[i][0], Path_solution, Solution_Turn, Path_solution_coordinates, Solution_infeasible)
            a.tracePath({pr_sol:Path_solution}, delay=100)
            a.run()
            break
    population,Turn,Actual_Fitness=Sort_pop(population,Turn,Actual_Fitness)
    if fittest_found==1:
        break
    Cross_over(population)
    Mutation(population)
    store()
    Iteration_Num+=1
    print(f'Min Infeasible :{min(infeasible_)} | Max Fitness :{max(Actual_Fitness):.2f}\n ')
    path,path_coordinates,infeasible_,Actual_Fitness=[],[],[],[]
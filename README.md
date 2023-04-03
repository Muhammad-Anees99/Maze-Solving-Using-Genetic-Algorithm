# Maze-Solving-Using-Genetic-Algorithm
15 x 15 Maze Solving Using Genetic Algorithm.
Genetic Algorithm for Maze Solving
Genetic algorithms serve as a valuable tool in the application of machine learning, particularly for tackling problems that involve an immense number of possible solutions. By mimicking biological processes through software, these algorithms continuously generate potential solutions, assess their fitness against desired outcomes, and refine the most promising candidates. This approach enables the exploration of large search spaces and can yield optimal solutions to complex problems.
Path planning in Maze:
In this problem, the fittest path is generated using Genetic Algorithm. The implementation of this Algorithm is explained below.
Pyamaze:
The purpose of the pyamaze module is to simplify the creation of customizable random mazes and enable easy implementation of search algorithms. With this module, there is no need to write GUI code or use Object-Oriented Programming, as the module provides support for these functionalities.You can install pyamaze by following command.
pip install pyamaze
Implementation:
There are the following steps in implementation:
Population Generation
Fitness Function
Parent Selection
Cross-over
Mutation

Population Generation:
The population is represented as a collection of lists, where each sublist corresponds to a chromosome. Each chromosome contains two bits that indicate the position to which we need to move. Essentially, the chromosome encodes a path through the maze by specifying a sequence of movements.
We have fixed the first and last gene in a chromosome and have generated remaining genes by random.randint function.
Fitness Function:
In this function, we will find the number of turns, number of infeasible steps, and path length. First of all, we will find the number of turns. For this, we will compare a gene to the next gene and if they are not equal we will increment turn.
Now we will find infeasible steps and path length. Here we will decide that which path should it take by orientation and direction bits. We are appending (1,1) in path. Then decide variable will decide where we have to move column-wise column first or row-wise row first. Here pre_coordinate is the coordinate where agent is at that time and post_coordinate is coordinate where it will jump in next step. We are finding Boundary by comparing gene with next gene for up and down move. Then we are deciding our post_coordinate by decide variable and next. Then we checked if our postcoordinate belogs to start or goal or not. If not then we append it to path.
In next part, we are checking if there any obstacle in path, if any we will append 1 in infeasible_ list otherwise will append 0. At the end sum of this list will give number of infeasible steps and length of this list will give us pathlength.
In this part we will compare gene with next gene if it is greater we will increment to move up and vive versa.

Solution-Check:
This function will check if any chromosome with 0 infeasible steps if any it will print a solution and the path will be given to the maze and m.run, will display the robot moving in the maze.
Parent selection:
We have calculated fitness based on turns, infeasible steps, and path length. We have set their weights.
Cross-Over:
In the crossover, after we have generated a randomly generated cross point excluding 1st and last gene. Then we generated the last half of the population by crossing over two chromosomes by a gap of two.

Mutation:
In this, we randomly generated an index between column size-1 and at that index, we assigned it a random value in the range of row size. After that we mutated the last half of the population's bits.

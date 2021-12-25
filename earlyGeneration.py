import numpy as np
import random
import copy

class earlyGeneration:

	def __init__(self, graph, NODES, start, stop,POPULATION_SIZE):
		self.graph = graph
		self.numberOfNodes = NODES
		self.start = start
		self.stop = stop
		self.route = []
		self.availableNodes = []
		self.size=POPULATION_SIZE
		self.population=[]


	def random_path(self):
		newgraph = copy.deepcopy(self.graph)
		self.route = []
		self.route.append(self.start)
		i = 0
		while self.route[-1]!=self.stop:
			self.availableNodes = []
			available = 0
			for j in range(self.numberOfNodes):
				if newgraph[self.route[-1]][j] > 0:
					self.availableNodes.append(j)
					available += 1

			for k in range(self.numberOfNodes):
				newgraph[k][self.route[-1]] = 0
				newgraph[self.route[-1]][k] = 0

			if available==0:
				i = 0
				self.route = []
				self.route.append(self.start)
				newgraph = copy.deepcopy(self.graph)
			else:
				self.route.append(self.availableNodes[random.randint(0, available-1)])
				i += 1
		return self.route

	def generate_population(self):
		for i in range(self.size):
			self.population.append(self.random_path())


	def fitness_calculation(self,chromosome):
		cost=0
		for i in range(len(chromosome)-1):
			cost+= self.graph[chromosome[i]][chromosome[i+1]]
		return(cost)

	def selection(self):
			parents=[]
			if(len(self.population)>0):
				cost_min1=self.fitness_calculation(self.population[0])
				fitter=0
				#1er parent
				for i in range(1,self.size):
					if(self.fitness_calculation(self.population[i])<cost_min1):
						cost_min1=self.fitness_calculation(self.population[i])
						fitter=i
				parents.append(self.population[fitter])
				#2ème parent
				cost_min2=self.fitness_calculation(self.population[0])
				i=0
				fitter=0
				while(cost_min2==cost_min1 and i<len(self.population)-1):#si le fitter chromosome est le 1er parent et en même temps le premier random individu
					i+=1
					cost_min2=self.fitness_calculation(self.population[i])
					fitter=i
				if(i!=self.size):#si il existe encore des chromosomes différents que le premier parent(cout)
					for i in range(1,self.size):
						if(self.fitness_calculation(self.population[i])<cost_min2 and cost_min1!=self.fitness_calculation(self.population[i])):
							cost_min2=self.fitness_calculation(self.population[i])
							fitter=i

				parents.append(self.population[fitter])

			return parents

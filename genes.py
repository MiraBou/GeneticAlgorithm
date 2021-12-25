
import math
import numpy as np
import random

class genes:

	def __init__ (self, GRAPH, ITERATION, NODES, CHILDS, MUT, start, stop, firstParent, secondParent):
		self.iteration = ITERATION
		self.numberOfNodes = NODES
		self.numberOfChilds = CHILDS
		self.mutateLvl = MUT
		self.GRAPH = GRAPH
		self.start = start
		self.stop = stop
		self.newChilds = []
		#newchilds stocke les enfants(childs) après l'évaluation
		self.bestRoute = []
		self.offSpring1 = []
		self.offSpring2 = []
		self.costOfParent1 = 0
		self.costOfParent2 = 0
		self.parent1 = firstParent
		self.parent2 = secondParent

	def mutation(self,off_sp):
			mutate = random.randint(1, 100)
			size    =   len(off_sp)
			if ( mutate < self.mutateLvl and size>2):
				choose=random.randint(0,1)
				if(choose==0): #mutatation des gènes
					if(size>3):
							#swap des 2 genes dans le même chromosome
							k = random.randint(1, size-2)
							j = random.randint(1, size-2)
							while(j==k):
								j = random.randint(1, size-2)
								#swap
							a = off_sp[k]
							off_sp[k] = off_sp[j]
							off_sp[j] = a
					elif(size==3):
						# mutation d'un gène
						if(self.numberOfNodes>3):
							j = random.randint(0,self.numberOfNodes-1)
							while(j==self.start or j==self.stop or j==off_sp[1]):
								j = random.randint(0,self.numberOfNodes-1)
							off_sp[1]=j
				elif(size>=3): #suppression d'un gène
					j = random.randint(1,size-2)
					del off_sp[j]

	def crossover(self):
		couple = []
		self.offSpring1=[]
		self.offSpring2=[]
		self.offSpring1.append(self.start)
		self.offSpring2.append(self.start)
		k_couple = 0
		for i in range(1,len(self.parent1)-1):
				j=1
				while(j<len(self.parent2)-1 and self.parent1[i]!=self.parent2[j]):
					j+=1

				if(i<len(self.parent1)-1 and j<len(self.parent2)-1 and self.parent1[i]==self.parent2[j]):
					couple.append([i,j])
					k_couple += 1

		rd_cross = random.randint(0,1)
		if(k_couple>0 and rd_cross==0):
			rd_numb = random.randint(0,k_couple-1)
			for i in range(1,len(self.parent1)):
				if(i<couple[rd_numb][0]):
					self.offSpring1.append(self.parent1[i])
			for i in range(1,len(self.parent2)):
				if(i<couple[rd_numb][1]):
					self.offSpring2.append(self.parent2[i])

			for i in range(couple[rd_numb][0],len(self.parent1)):
					self.offSpring2.append(self.parent1[i])

			for i in range(couple[rd_numb][1],len(self.parent2)):
					self.offSpring1.append(self.parent2[i])

		else :           #uniform crossover
				for k in range(1, self.numberOfNodes):
					choose = random.randint(0, 1)

					if((choose==0 or k>len(self.parent2))and (k<len(self.parent1))):
							self.offSpring1.append(self.parent1[k])
							if(self.parent1==self.stop):
								break
					elif(choose==1 or k>len(self.parent1))and (k<len(self.parent2)):
							self.offSpring1.append(self.parent2[k])
							if(self.parent2[k]==self.stop):
								break

				for k in range(1, self.numberOfNodes):
					choose = random.randint(0, 1)

					if(choose==0 or k>len(self.parent2))and (k<len(self.parent1)):
						self.offSpring2.append(self.parent1[k])
						if(self.parent1[k]==self.stop):
								break

					elif(choose==1 or k>len(self.parent1))and (k<len(self.parent2)):
						self.offSpring2.append(self.parent2[k])
						if(self.parent2==self.stop):
								break




	def removeLoop(self,off_sp):
	#vérifier l'existence d'un cycle
		loop=False
		for k in range(len(off_sp)-1):
			for k2 in range(k+1,len(off_sp)):
				if off_sp[k] == off_sp[k2] and off_sp[k] != -1:
					loop=True
					break
	#supprimer le cycle en cas d'existence
		if(loop==True):
			diff = k2-k
			for i in range(diff):
				del off_sp[k+1]



	def evaluate(self,off_sp):
		#rechercher les mêmes gènes dans le chromosome
		for k in range(len(off_sp)-1):
			for k2 in range(k+1,len(off_sp)):
				if off_sp[k] == off_sp[k2] and off_sp[k] != -1:
				   return False

	   #vérifier si le chemin  existe
		for k in range(1, len(off_sp)):
			if off_sp[k-1] != -1 and off_sp[k] != -1:
				if self.GRAPH[off_sp[k-1]][off_sp[k]] <= 0:
				   return False

	   #vérifier si la destination existe comme dernier gène
			if off_sp[len(off_sp)-1] != self.stop:
			   return False

		return True


	def makeRoute(self):
		self.setParents()

		for i in range(self.iteration):
			nChild = 0
			self.newChilds=[]
			print('Itération n°:  '+ str(i+1))
			self.printParents()
			self.printBestRoute()
			print(' ')

			for j in range(self.numberOfChilds):
				self.crossover()

				self.removeLoop(self.offSpring1)
				self.removeLoop(self.offSpring2)
				#print("after crossover")
				#print(self.offSpring1)
				#print(self.offSpring2)
				self.mutation(self.offSpring1)
				self.mutation(self.offSpring2)

				#print("after mutation")
				#print(self.offSpring1)
				#print(self.offSpring2)

				if self.evaluate(self.offSpring1) == True:
					self.newChilds.append(self.offSpring1)
					nChild +=1

				if self.evaluate(self.offSpring2) == True:
					self.newChilds.append(self.offSpring2)
					nChild += 1

			#self.printChilds(nChild)
#fitness evaluation
			for j in range(nChild):
					cost = 0
					diff = 0
					for k in range(1, len(self.newChilds[j])):
						if self.newChilds[j][k]==-1: break
						cost += self.GRAPH[self.newChilds[j][k-1]][self.newChilds[j][k]]
					diff = self.costOfParent1 - self.costOfParent2
					if diff >= 0 and cost<=self.costOfParent1:
						self.parent1 = []
						for i in range(len(self.newChilds[j])):
							self.parent1.append(self.newChilds[j][i])
						self.costOfParent1 = cost

					if diff<0 and cost<=self.costOfParent2:
						self.parent2 = []
						for i in range(len(self.newChilds[j])):
							self.parent2.append(self.newChilds[j][i])
						self.costOfParent2 = cost

					if cost<=self.costOfBestRoute:
						self.bestRoute = []
						for i in range(len(self.newChilds[j])):
							self.bestRoute.append(self.newChilds[j][i])
						self.costOfBestRoute = cost


		print("Fin d'itérations!")

		self.printBestRoute()


	def setParents(self):
		for i in range(len(self.parent1)-1):
			self.costOfParent1 += self.GRAPH[self.parent1[i]][self.parent1[i+1]]

		for i in range(len(self.parent2)-1):
			self.costOfParent2 += self.GRAPH[self.parent2[i]][self.parent2[i+1]]

		if self.costOfParent1 > self.costOfParent2:
			self.costOfBestRoute = self.costOfParent2
			for i in range(len(self.parent2)):
				self.bestRoute.append(self.parent2[i])
		else:
			self.costOfBestRoute = self.costOfParent1
			for i in range(len(self.parent1)):
				self.bestRoute.append(self.parent1[i])


	def printParents(self):
		print('1er parent: '+str(self.parent1)+'        Coût: ' + str(self.costOfParent1))
		print('2ème parent: '+str(self.parent2)+'        Coût: ' + str(self.costOfParent2))



	def printBestRoute(self):
		print('')
		print('Le plus court chemin est: '+str(self.bestRoute))
		print('    Coût: ' + str(self.costOfBestRoute))


	def printChilds(self, childsNum):
		print('La nouvelle génération: ')
		for i in range(childsNum):
			for j in range(len(self.newChilds[i])):
				print(self.newChilds[i][j])


import Graphyy
import copy
import csv
import numpy as np

import earlyGeneration
import genes


ITERATION = 10
CHILDS = 50
MUTATION_level = 50 #pourcentage
POPULATION_SIZE=10
g_matrix = [[]]
PARENTS=[] #matrice qui stocke les deux premiers parents

########l'initialisation du graph par un fichier cvs######
#NODES=0
#with open('/Users/usermac/Desktop/BOUSSARENDAL_GeneticAlgorithm/data.csv', "rt") as f:
#	reader = csv.reader(f)
#	for line in reader:
#		for x in range(len(line)):
#			g_matrix[NODES].append(int(line[x]))
#		if(NODES>0):
#			g_matrix[NODES].remove(NODES)
#		NODES += 1
#		g_matrix.append([NODES])
#g_matrix.pop()
##############

#l'initialisation du graph par l'utilisateur
g=Graphyy.Graphyy()
g_matrix=g.matrix()
NODES=g.nb_vertex

start =int(input("Veuillez saisir l'id de votre source(de 0 à " + str(NODES-1) + "):" ))
stop = int(input("Veuillez saisir l'id de votre destination(de 0 à " + str(NODES-1) + "):" ))

path = earlyGeneration.earlyGeneration(g_matrix,NODES, start, stop,POPULATION_SIZE)
path.generate_population()
parents=path.selection()

if(len(parents)>0):
		gen = genes.genes(g_matrix, ITERATION, NODES, CHILDS, MUTATION_level, start, stop, parents[0], parents[1])
		gen.makeRoute()


class Graphyy:
	def __init__ (self):
		self.nb_vertex=0
		self.nb_edge=0
		self.Graphyy=[]

	def matrix(self):
		self.nb_vertex = int(input('Entrez le nombre de sommets ? ' ))
		self.nb_edge = int(input('Entrez le nombre des arcs ? ' ))
		#initialisation de la matrice avec des 0
		for j in range(self.nb_vertex):
			self.Graphyy.append([0]*self.nb_vertex)

		print("Les ids des sommets sont comme suivants:")
		for i in range(self.nb_vertex):
			print('Sommet '+str(i))

		for i in range(self.nb_edge):
			a=int(input("Saisir l'id source du 1er sommet de l'arc:"))
			b=int(input("Saisir l'id source du 2eme sommet de l'arc:"))
			c=int(input("Le cout de l'arc:"))
			self.Graphyy[a][b]=c
			self.Graphyy[b][a]=c

		return(self.Graphyy)

import sys

class NodParcurgere:
	gr=None #trebuie setat sa contina instanta problemei
	def __init__(self, info, parinte, cost=0, h=0):
		self.info=info
		self.parinte=parinte #parintele din arborele de parcurgere
		self.g=cost
		self.h=h
		self.f=self.g+self.h
	
	def obtineDrum(self):
		l=[self]
		nod=self
		while nod.parinte is not None:
			l.insert(0, nod.parinte)
			nod=nod.parinte
		return l

	def afisDrum(self, afisCost=False, afisLung=False): #returneaza si lungimea drumului
		l=self.obtineDrum()
		f = open('output.txt', 'a')
		i=1
		for nod in l:
			if nod.parinte is not None:
				if nod.parinte.info[3]==1:
					mbarca1=self.__class__.gr.malInitial
					mbarca2=self.__class__.gr.malFinal
				else:
					mbarca1=self.__class__.gr.malFinal
					mbarca2=self.__class__.gr.malInitial
				f.write(">>> Barca s-a deplasat de la malul {} la malul {} cu {} fantome, {} canibali si {} misionari.\n".format(mbarca1, mbarca2, abs(nod.info[2]-nod.parinte.info[2]),abs(nod.info[0]-nod.parinte.info[0]), abs(nod.info[1]-nod.parinte.info[1])))
			f.write(str(i) + ") " + str(nod) + "\n")
			i=i+1
			print(str(nod) + "\n")
		if afisCost:
			f.write("\nCost: " + str(self.g) + "\n")
		if afisCost:
			f.write("Nr noduri: " + str(len(l)) + "\n")
		f.close()
		return len(l)

	def contineInDrum(self, infoNodNou):
		nodDrum=self
		while nodDrum is not None:
			if(infoNodNou==nodDrum.info):
				return True
			nodDrum=nodDrum.parinte
		return False
		
	def __repr__(self):
		sir=""		
		sir+=str(self.info)
		return(sir)

class Graph: #graful problemei
	def __init__(self, nume_fisier):
		f=open(nume_fisier,"r")
		textFisier=f.read()
		f.close()
		listaInfoFisier=textFisier.split()
		#print(listaInfoFisier)

		self.__class__.N=0
		self.__class__.M=0
		self.__class__.NF=0
		self.__class__.malInitial='0'
		self.__class__.malFinal='0'
		for i in listaInfoFisier:
			li = i.split("=")
			if li[0] == 'N':
				self.__class__.N=int(li[1])
			elif li[0] == 'M':
				self.__class__.M=int(li[1])
			elif li[0] == 'NF':
				self.__class__.NF=int(li[1])
			elif li[0] == 'MalInitial':
				self.__class__.malInitial=li[1]
			elif li[0] == 'MalFinal':
				self.__class__.malFinal=li[1]
		'''
		self.__class__.N=int(listaInfoFisier[0])
		self.__class__.M=int(listaInfoFisier[1])
		self.__class__.NF=int(listaInfoFisier[2])
		self.__class__.malInitial=listaInfoFisier[3]
		self.__class__.malFinal=listaInfoFisier[4]
		'''
		self.start=(self.__class__.N,self.__class__.N,self.__class__.NF,1) #informatia nodului de start
		#self.scopuri=[(0,0,0,0)]

	def testeaza_scop(self, nodCurent):
		if nodCurent.info[0]==0 and nodCurent.info[1]==0 and nodCurent.info[3]==0 and nodCurent.info[2]==Graph.NF:
			return True
		return False

	def genereazaSuccesori(self, nodCurent,tip_euristica="euristica banala"):
		def test_conditie(mis, can, fan):
			#return mis==0 or mis>=can
			return mis==0 or mis>=can and fan<mis+can

		listaSuccesori=[]
		#nodCurent.info va contine (c_i, m_i, f_i, barca)
		barca=nodCurent.info[3]
		if barca==1:
			canMalCurent=nodCurent.info[0]
			misMalCurent=nodCurent.info[1]
			fanMalCurent=nodCurent.info[2]
			canMalOpus=Graph.N-canMalCurent
			misMalOpus=Graph.N-misMalCurent
			fanMalOpus=Graph.NF-fanMalCurent
		else:
			canMalOpus=nodCurent.info[0]
			misMalOpus=nodCurent.info[1]
			fanMalOpus=nodCurent.info[2]
			canMalCurent=Graph.N-canMalOpus			
			misMalCurent=Graph.N-misMalOpus	
			fanMalCurent=Graph.NF-fanMalOpus
					
		maxMisionariBarca=min(Graph.M, misMalCurent)
		for misBarca in range(maxMisionariBarca+1):
			if misBarca==0:
				maxCanibaliBarca=min(Graph.M, canMalCurent)
				minCanibaliBarca=1
			else:
				maxCanibaliBarca=min(Graph.M-misBarca, canMalCurent, misBarca)
				minCanibaliBarca=0

			for canBarca in range(minCanibaliBarca, maxCanibaliBarca+1):
				if misBarca==0: #fantomele
					fanBarca=min(Graph.M-canBarca, fanMalCurent, canBarca)
				else: #daca avem misionari in barca, nu vom avea fantome
					fanBarca=0

				#consideram mal curent nou ca fiind acelasi mal de pe care a plecat barca
				canMalCurentNou=canMalCurent-canBarca
				misMalCurentNou=misMalCurent-misBarca
				fanMalCurentNou=fanMalCurent-fanBarca
				canMalOpusNou=canMalOpus+canBarca
				misMalOpusNou=misMalOpus+misBarca
				fanMalOpusNou=fanMalOpus+fanBarca
				if not test_conditie(misMalCurentNou,canMalCurentNou,fanMalCurentNou):
					continue
				if not test_conditie(misMalOpusNou,canMalOpusNou,fanMalOpusNou):
					continue	
				if barca==1: #testul este pentru barca nodului curent (parinte) deci inainte de mutare
					infoNodNou= (canMalCurentNou,misMalCurentNou,fanMalCurentNou, 0)	
				else:				
					infoNodNou= (canMalOpusNou,misMalOpusNou,fanMalOpusNou, 1)
				if not nodCurent.contineInDrum(infoNodNou):
					costSuccesor=canBarca+misBarca-fanBarca
					listaSuccesori.append(NodParcurgere(infoNodNou,nodCurent,cost=nodCurent.g+costSuccesor, h=1))

		return listaSuccesori

def a_star(gr, nrSolutiiCautate, tip_euristica):
	#in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
	#c=[NodParcurgere(gr.start, None, 0, gr.calculeaza_h(gr.start))]
	c=[NodParcurgere(gr.start, None, 0, 1)]
	
	while len(c)>0:
		nodCurent=c.pop(0)
		
		if gr.testeaza_scop(nodCurent):
			nodCurent.afisDrum(afisCost=True, afisLung=True)
			f = open("output.txt", "a")
			f.write("==========================")
			f.close()
			nrSolutiiCautate-=1
			if nrSolutiiCautate==0:
				return
		lSuccesori=gr.genereazaSuccesori(nodCurent,tip_euristica=tip_euristica)	
		for s in lSuccesori:
			i=0
			gasit_loc=False
			for i in range(len(c)):
				#diferenta fata de UCS e ca ordonez dupa f
				if c[i].f>=s.f :
					gasit_loc=True
					break
			if gasit_loc:
				c.insert(i,s)
			else:
				c.append(s)

def uniform_cost(gr, nrSolutiiCautate=1):
	#c=[NodParcurgere(gr.start, None, 0, gr.calculeaza_h(gr.start))]
	c=[NodParcurgere(gr.start, None, 0, 1)]
	
	while len(c)>0:
		nodCurent=c.pop(0)
		
		if gr.testeaza_scop(nodCurent):
			nodCurent.afisDrum()
			f = open("output.txt", "a")
			f.write("==========================")
			f.close()
			nrSolutiiCautate-=1
			if nrSolutiiCautate==0:
				return
		lSuccesori=gr.genereazaSuccesori(nodCurent)	
		for s in lSuccesori:
			i=0
			gasit_loc=False
			for i in range(len(c)):
				#ordonez dupa cost(notat cu g aici și în desenele de pe site)
				if c[i].g>s.g :
					gasit_loc=True
					break
			if gasit_loc:
				c.insert(i,s)
			else:
				c.append(s)

gr=Graph("input.txt")	
NodParcurgere.gr = gr

f = open("output.txt", "w")
f.close()

a_star(gr, nrSolutiiCautate=1, tip_euristica="euristica banala")
#uniform_cost(gr, nrSolutiiCautate=1)
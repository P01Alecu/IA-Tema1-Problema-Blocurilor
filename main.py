'''
Documentatie: https://docs.google.com/document/d/1ZUyqkFChdxvniIWOeMFsLlHfhXCt4lEWL9-Af9beiBo/edit?usp=sharing
'''
import copy
import sys
import time
from multiprocessing import Process #pentru timeout

# informatii despre un nod din arborele de parcurgere (nu din graful initial)
class NodParcurgere:
    def __init__(self, info, parinte, cost=0, h=0, timp=0):
        self.info = info
        self.parinte = parinte  # parintele din arborele de parcurgere
        self.g = cost  # consider cost=1 pentru o mutare
        self.timp = timp
        self.h = h
        self.f = self.g + self.h

    def obtineDrum(self):
        l = [self]
        nod = self
        while nod.parinte is not None:
            l.insert(0, nod.parinte)
            nod = nod.parinte
        return l

    def afisDrum(self, afisCost=False, afisLung=False, afisTimp=False):  # returneaza si lungimea drumului
        l = self.obtineDrum()
        f = open(sys.argv[2], 'a')
        
        i = 1 #numarul de ordine al fiecarui nod in drum
        t1 = 0
        t2 = 0
        for nod in l:
            f.write(str(i) + ")\n")
            if afisTimp and i==1:
                t1 = nod.timp
            if afisTimp and i==len(l)-1:
                t2 = nod.timp
            i += 1
            f.write(str(nod) + "\n")
        if afisCost:
            f.writelines("Cost: " + str(self.g) + "\n")
        if afisLung:
            f.writelines("Lungime: " + str(len(l)) + "\n")
        if afisTimp:
            f.writelines("Timp: " + str(t2 - t1) + " secunde.\n")
        f.close()
        return len(l)

    def contineInDrum(self, infoNodNou):
        nodDrum = self
        while nodDrum is not None:
            if (infoNodNou == nodDrum.info):
                return True
            nodDrum = nodDrum.parinte

        return False

    def __repr__(self):
        sir = ""
        sir += str(self.info)
        return (sir)

    def __str__(self):
        sir = ""

        maxInalt = max([len(stiva) for stiva in self.info])
        for inalt in range(maxInalt, 0, -1):
            for stiva in self.info:
                if len(stiva) < inalt:
                    sir += "   "
                else:
                    sir += stiva[inalt - 1][0] +'[' + stiva[inalt - 1][1] + "] "
            sir += "\n"
        sir += "-" * (2 * len(self.info) - 1)
        return sir

class Graph:  # graful problemei
    def __init__(self, nume_fisier):
        def obtineStive(sir):
            stiveSiruri = sir.strip().split("\n")
            listaStive = [sirStiva.strip().split("/") if sirStiva != "-" else [] for sirStiva in stiveSiruri]

            #listaF = [[sr.translate({ord('['): None, ord(']'): None}).split(" ")] for sirF in listaStive for sr in sirF]   #for sirF in s in listaStive
            #l.append([sr.translate({ord(']'): None}).split("[") for sirF in listaStive for sr in sirF])
            lFin = []
            for i in listaStive:
                lTemp = []
                for j in i:
                    lTemp.append(j.split(" "))
                lFin.append(lTemp)
            return lFin

        f = open(nume_fisier, 'r')
        continutFisier = f.read()
        self.culoareScop = continutFisier[0]
        self.start = obtineStive(continutFisier[1:].translate({ord('['): ' ', ord(']'): None}))

        #print("Culoarea scop: ", self.culoareScop)
        #print("Stare Initiala: ", self.start)

    def verificareValiditateInput(self):
        """
        Verifica daca avem suficiente culori si blocuri pentru a atince scopul.
        Trebuie sa avem cel putin 2 culori scop si cel putin cate un bloc pentru fiecare stiva
        """
        nrCulori = 0
        nrTotal = 0
        for i in self.start:
            nrTotal += len(i)
            for j in i:
                if j[1] == self.culoareScop:
                    nrCulori += 1
        if((nrTotal < len(self.start)) or (nrCulori < 2 and len(self.start) > 1)):
            return False
        else:
            return True

    def testeaza_scop(self, stareCurenta):
        esteScop = True
        for i in stareCurenta.info:
            if len(i) > 0:
                if i[-1][1] != self.culoareScop:
                    esteScop = False
                    break
            else:
                esteScop = False
                break
        return esteScop

    # va genera succesorii sub forma de noduri in arborele de parcurgere
    def genereazaSuccesori(self, nodCurent, tip_euristica="euristica banala"):
        listaSuccesori = []
        stive_c = nodCurent.info  # stivele din nodul curent
        nr_stive = len(stive_c)
        for idx in range(nr_stive):
            copie_interm = copy.deepcopy(stive_c)
            if len(copie_interm[idx]) == 0:
                continue
            bloc = copie_interm[idx].pop()
            for j in range(nr_stive):
                if idx == j:
                    continue
                stive_n = copy.deepcopy(copie_interm)  # lista noua de stive
                if(len(stive_n[j]) > 0):    #verifica culoarea (daca este aceeasi nu poate pune blocul aici)
                    if(stive_n[j][-1][1] == bloc[1]):
                        continue

                #verifica daca are vecin pe acelasi nivel (stanga sau dreapta) de aceeasi paritate
                veciniOK = False
                existaStanga = False
                existaDreapta = False
                #daca nu este primul stack, incearca sa verifice vecinul din stanga (daca este primul nu are vecin in stanga)
                if(j > 0): #verifica stanga
                    if(len(stive_n[j - 1]) >= len(stive_n[j]) + 1):
                        if(int(stive_n[j - 1][len(stive_n[j]) - 1][0]) % 2 == int(bloc[0]) % 2):
                            veciniOK = True
                        existaStanga = True
                if(j < len(stive_n) - 1): #verifica dreapta
                    if (len(stive_n[j + 1]) >= len(stive_n[j]) + 1):
                        if (int(stive_n[j + 1][len(stive_n[j]) - 1][0]) % 2 == int(bloc[0]) % 2):
                            veciniOK = True
                        existaDreapta = True

                if((existaStanga == False and existaDreapta == False) or (existaStanga == False and j == len(stive_n) - 1) or (existaDreapta == False and j == 0)): #daca nu are vecini nici stanga, nici dreapta, atunci blocul poate fi pus aici
                    veciniOK = True
                if(veciniOK == False): #daca vecinii nu indeplinesc conditiile trece la urmatoarea stiva
                    continue

                stive_n[j].append(bloc)
                costMutareBloc = int(bloc[0]) + int(len(copie_interm[idx]))

                #daca blocul de dedesubt este prins intre 2 culori identice, o va primi si acesta (de dedesubt)
                if(len(stive_n[j]) >= 3):
                    if(stive_n[j][-3][1] == stive_n[j][-1][1]):
                        #print(stive_n[j][-3][1] + ' + mijloc: ' + stive_n[j][-2][1] + ' : +' + stive_n[j][-1][1])
                        stive_n[j][-2][1] = stive_n[j][-1][1]

                nod_nou = NodParcurgere(stive_n, nodCurent, cost=nodCurent.g + costMutareBloc,
                                        h=self.calculeaza_h(stive_n, tip_euristica), timp=time.time())
                if not nodCurent.contineInDrum(stive_n):
                    listaSuccesori.append(nod_nou)

        return listaSuccesori

    # euristica banala
    def calculeaza_h(self, infoNod, tip_euristica="euristica banala"):
        if tip_euristica == "euristica banala":
            for i in infoNod:
                if len(i) != 0:
                    if i[-1][1] != self.culoareScop:
                        return 1
                else:
                    return 1
            return 0

        elif tip_euristica == "euristica nebanala1":
            indexMinim = 1
            mutariMinime = 0
            for i in infoNod:
                if len(i) != 0:
                    #if i[-1][1] != self.culoareScop:
                    mutariMinime += 1
                    if indexMinim > int(i[-1][0]):
                        indexMinim = int(i[-1][0])
                else:
                    mutariMinime += 1
            return indexMinim * mutariMinime

        elif tip_euristica == "euristica neadmisibila":
            cost = 0
            for i in infoNod:
                if len(i) != 0:
                    if i[-1][1] != self.culoareScop:
                        cost += int(i[-1][0]) + len(i)
            return cost
        return 10
        '''
            # calculez cate blocuri nu sunt la locul fata de fiecare dintre starile scop, si apoi iau minimul dintre aceste valori
            euristici = []
            for (iScop, scop) in enumerate(self.scopuri):
                h = 0
                for iStiva, stiva in enumerate(infoNod):
                    for iElem, elem in enumerate(stiva):
                        try:
                            # exista în stiva scop indicele iElem dar pe acea pozitie nu se afla blocul din infoNod
                            if elem != scop[iStiva][iElem]:
                                h += 1
                        except IndexError:
                            # nici macar nu exista pozitia iElem in stiva cu indicele iStiva din scop
                            h += 1
                euristici.append(h)
            return min(euristici)
        '''
        return 1

def breadth_first(gr, nrSolutiiCautate):
    # in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
    c = [NodParcurgere(gr.start, None, timp=time.time())]
    max = 0

    while len(c) > 0:
        if(max < len(c)):
            max = len(c)
        nodCurent = c.pop(0)

        if gr.testeaza_scop(nodCurent):
            nodCurent.afisDrum(afisCost=True, afisLung=True, afisTimp=True)
            f = open(sys.argv[2], 'a')
            f.write("\n#########################################\n")
            f.close()
            nrSolutiiCautate -= 1
            if nrSolutiiCautate == 0:
                f = open(sys.argv[2], 'a')
                f.write("\nNumarul total de noduri calculate: " + str(max) + "\n")
                f.close()
                return
        lSuccesori = gr.genereazaSuccesori(nodCurent)
        c.extend(lSuccesori)


def a_star(gr, nrSolutiiCautate, tip_euristica):
    # in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
    c = [NodParcurgere(gr.start, None, 0, gr.calculeaza_h(gr.start), timp=time.time())]
    max = 0
    
    while len(c) > 0:
        if max < len(c):
            max = len(c)
        nodCurent = c.pop(0)
        if gr.testeaza_scop(nodCurent):
            nodCurent.afisDrum(afisCost=True, afisLung=True, afisTimp=True)
            f = open(sys.argv[2], 'a')
            f.write("\n#########################################\n")
            f.close()
            nrSolutiiCautate -= 1
            if nrSolutiiCautate == 0:
                f = open(sys.argv[2], 'a')
                f.write("\nNumarul total de noduri calculate: " + str(max) + "\n")
                f.close()
                return
        lSuccesori = gr.genereazaSuccesori(nodCurent, tip_euristica=tip_euristica)
        for s in lSuccesori:
            i = 0
            gasit_loc = False
            for i in range(len(c)):
                # diferenta fata de UCS e ca ordonez dupa f
                if c[i].f >= s.f:
                    gasit_loc = True
                    break
            if gasit_loc:
                c.insert(i, s)
            else:
                c.append(s)

def uniform_cost(gr, nrSolutiiCautate=1):
	#in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
	c=[NodParcurgere(gr.start, None, 0, gr.calculeaza_h(gr.start), timp=time.time())]
	max = 0
	while len(c)>0:
		if(max < len(c)):
		    max = len(c)
		nodCurent=c.pop(0)
		
		if gr.testeaza_scop(nodCurent):
			nodCurent.afisDrum(afisCost=True, afisLung=True, afisTimp=True)
			nrSolutiiCautate-=1
			if nrSolutiiCautate==0:
			    f = open(sys.argv[2], 'a')
			    f.write("\nNumarul total de noduri calculate: " + str(max) + "\n")
			    f.close()
			    return
				#return
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

def ida_star(gr, nrSolutiiCautate, tip_euristica="euristica banala"):
	nodStart=NodParcurgere(gr.start, None, 0, gr.calculeaza_h(gr.start, tip_euristica), timp=time.time())
	limita=nodStart.f
	f=open(sys.argv[2], 'a')
	while True:
		#print("Limita de pornire: ", limita)
		nrSolutiiCautate, rez= construieste_drum(gr, nodStart,limita,nrSolutiiCautate, tip_euristica)
		if rez=="gata":
			break
		if rez==float('inf'):
			f.write("\nNu exista solutii\n")
			break
		limita=rez
def construieste_drum(gr, nodCurent, limita, nrSolutiiCautate, tip_euristica):
	if nodCurent.f>limita:
		return nrSolutiiCautate, nodCurent.f
	if gr.testeaza_scop(nodCurent) and nodCurent.f==limita :
		nodCurent.afisDrum(afisCost=True, afisLung=True, afisTimp=True)
		f = open(sys.argv[2], 'a')
		f.write("\n========================\n")
		f.close()
		nrSolutiiCautate-=1
		if nrSolutiiCautate==0:
			return 0,"gata"
	lSuccesori=gr.genereazaSuccesori(nodCurent)	
	minim=float('inf')
	for s in lSuccesori:
		nrSolutiiCautate, rez=construieste_drum(gr, s, limita, nrSolutiiCautate, tip_euristica)
		if rez=="gata":
			return 0,"gata"
		if rez<minim:
			minim=rez
	return nrSolutiiCautate, minim

if __name__ == '__main__':
    if(len(sys.argv) < 2):
        sys.argv.append('input.txt') #daca nu a fost dat fiesier de input
    if(len(sys.argv) < 3):
        sys.argv.append('output.txt')   #daca nu a fost dat fisier de output
    if(len(sys.argv) < 4):
        sys.argv.append(1)   #daca nu a fost dat numar de solutii
    if(len(sys.argv) < 5):
        sys.argv.append(3)   #daca nu a fost dat timeout

    t1 = time.time()
    gr = Graph(sys.argv[1])

    #daca inputul este bun
    if(gr.verificareValiditateInput()):
        #reseteaza fisierul de output
        f = open(sys.argv[2], 'w')
        f.close()

        #p = Process(target=breadth_first, args=(gr, int(sys.argv[3]), ))
        p = Process(target=a_star, args=(gr, int(sys.argv[3]), "euristica nebanala1", ))
        #p = Process(target=uniform_cost, args=(gr, int(sys.argv[3]), ))
        #p = Process(target=ida_star, args=(gr, int(sys.argv[3]), "euristica nebanala1", ))
        p.start()
        p.join(timeout=int(sys.argv[4]))
        p.terminate()
        if p.exitcode is None:
            print('Timeout!!!')
            f = open(sys.argv[2], 'a')
            f.write("\nTimeout\n")
            f.close()

        ###breadth_first(gr, nrSolutiiCautate=int(sys.argv[3]))
        ###a_star(gr, nrSolutiiCautate=int(sys.argv[3]),tip_euristica="euristica nebanala")
        ###uniform_cost(gr, nrSolutiiCautate=int(sys.argv[3]))
        t2 = time.time()
        print(str(t2-t1) + " secunde. (timpul total de rulare)")
    else:
        f = open(sys.argv[2], 'w')
        f.write('Inputul este gresit')
        f.close()

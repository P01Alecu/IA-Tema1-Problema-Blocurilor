import copy
import sys

# informatii despre un nod din arborele de parcurgere (nu din graful initial)
class NodParcurgere:
    def __init__(self, info, parinte, cost=0, h=0):
        self.info = info
        self.parinte = parinte  # parintele din arborele de parcurgere
        self.g = cost  # consider cost=1 pentru o mutare
        self.h = h
        self.f = self.g + self.h

    def obtineDrum(self):
        l = [self]
        nod = self
        while nod.parinte is not None:
            l.insert(0, nod.parinte)
            nod = nod.parinte
        return l

    def afisDrum(self, afisCost=False, afisLung=False):  # returneaza si lungimea drumului
        l = self.obtineDrum()
        f = open('output.txt', 'a')

        for nod in l:
            #print(str(nod))
            f.write(str(nod) + "\n")
        if afisCost:
            #print("Cost: ", self.g)
            f.writelines("Cost: " + str(self.g) + "\n")
        if afisCost:
            #print("Lungime: ", len(l))
            f.writelines("Lungime: " + str(len(l)) + "\n")
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
        nrTotal = 0
        for i in self.start:
            nrTotal += len(i)
        if(nrTotal < len(self.start)):
            return False
        else:
            return True

    def testeaza_scop(self, stareCurenta):
        esteScop = True
        for i in stareCurenta.info:
            if len(i) > 0:
                #print(i[-1])
                if i[-1][1] != self.culoareScop:
                    esteScop = False
                    break
            else:
                esteScop = False
                #print([])
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
                costMutareBloc = int(bloc[0]) + int(len(copie_interm[idx]))        ########cost  bloc[0] + len(idx)

                #schimba culoarea de dedesubt daca***** pentru stive_n[j-1] daca stive_n[j-2] are aceeasi culoare cu cea a blocului adaugat
                if(len(stive_n[j]) >= 3):
                    if(stive_n[j][-3][1] == stive_n[j][-1][1]):
                        #print(stive_n[j][-3][1] + ' + mijloc: ' + stive_n[j][-2][1] + ' : +' + stive_n[j][-1][1])
                        stive_n[j][-2][1] = stive_n[j][-1][1]


                nod_nou = NodParcurgere(stive_n, nodCurent, cost=nodCurent.g + costMutareBloc,
                                        h=self.calculeaza_h(stive_n, tip_euristica))
                if not nodCurent.contineInDrum(stive_n):
                    listaSuccesori.append(nod_nou)

        return listaSuccesori

    # euristica banala
    def calculeaza_h(self, infoNod, tip_euristica="euristica banala"):
        '''
        if tip_euristica == "euristica banala":
            if infoNod not in self.scopuri:
                return 1
            return 0
        else:
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
    c = [NodParcurgere(gr.start, None)]

    while len(c) > 0:
        nodCurent = c.pop(0)

        if gr.testeaza_scop(nodCurent):
            nodCurent.afisDrum(afisCost=True, afisLung=True)
            f = open('output.txt', 'a')
            f.write("\n#########################################\n")
            f.close()
            nrSolutiiCautate -= 1
            if nrSolutiiCautate == 0:
                return
        lSuccesori = gr.genereazaSuccesori(nodCurent)
        c.extend(lSuccesori)


def a_star(gr, nrSolutiiCautate, tip_euristica):
    # in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
    c = [NodParcurgere(gr.start, None, 0, gr.calculeaza_h(gr.start))]

    while len(c) > 0:
        nodCurent = c.pop(0)

        if gr.testeaza_scop(nodCurent):
            print("Solutie: ")
            nodCurent.afisDrum(afisCost=True, afisLung=True)
            print("\n#########################################\n")
            input()
            nrSolutiiCautate -= 1
            if nrSolutiiCautate == 0:
                return
        lSuccesori = gr.genereazaSuccesori(nodCurent, tip_euristica=tip_euristica)
        for s in lSuccesori:
            i = 0
            gasit_loc = False
            for i in range(len(c)):
                # diferenta fata de UCS e ca ordonez dupa f
                if c[i].f >= s.f:
                    gasit_loc = True
                    break;
            if gasit_loc:
                c.insert(i, s)
            else:
                c.append(s)

if(len(sys.argv) == 1):
    gr = Graph("input.txt")
else:
    gr = Graph(sys.argv[1]) #primul parametru este fisierul de input
#al doilea este fisierul de output
#nr solutii
#timeout

#daca inputul este bun
if(gr.verificareValiditateInput()):
    #reseteaza fisierul de output
    f = open('output.txt', 'w')
    f.close()

    #Rezolvat cu breadth first
    #print("Solutii obtinute cu breadth first:")
    breadth_first(gr, nrSolutiiCautate=3)

    #print("\n\n##################\nSolutii obtinute cu A*:")
    #print("\nObservatie: stivele sunt afisate pe orizontala, cu baza la stanga si varful la dreapta.")
    #nrSolutiiCautate=3
    #a_star(gr, nrSolutiiCautate=3,tip_euristica="euristica nebanala")
else:
    f = open('output.txt', 'w')
    f.write('Inputul este gresit')
    f.close()

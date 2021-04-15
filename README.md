# IA-Tema1-Problema-Blocurilor

Linkuri utile

https://repl.it/@IrinaCiocan/cautare-BFDFDFI-complet#main.py
https://repl.it/@IrinaCiocan/uniform-cost-search#main.py
https://repl.it/@IrinaCiocan/a-star#main.py
https://repl.it/@IrinaCiocan/problemablocurilor#main.py (E implementat cu BF si A*)
https://repl.it/@IrinaCiocan/exemplu-afisare-timp-folosit (cum calculam timpul de executie a unei secvente de cod)
https://repl.it/@IrinaCiocan/problema-canibalilor-si-misionarilor#main.py (observatie: e o alta varianta de generare a succesorilor mai complicata dar mai eficienta decat cea de la laborator). E implementat cu BF si A*) Variantele de la laborator sunt: https://repl.it/@IrinaCiocan/353-canibali-si-misionari#main.py, https://repl.it/@IrinaCiocan/352-canibali-si-misionari#main.py, https://repl.it/@IrinaCiocan/354-can-mis#main.py - din câte îmi amintesc cu 351 am lucrat pe repl.it-ul de la una dintre celelalte grupe
https://repl.it/@IrinaCiocan/exemplu-iterare-prin-folder
http://irinaciocan.ro/inteligenta_artificiala/python-comprehensions.php la secțiunea cu argumentele programului, respectiv timeout
http://irinaciocan.ro/inteligenta_artificiala/cum-rezolvam-o-problema.php modul general de abordare a unei probleme
Barem (punctajul e dat in procentaje din punctajul maxim al temei; procentajul maxim este 100%):

(5%)Fișierele de input vor fi într-un folder a cărui cale va fi dată în linia de comanda. În linia de comandă se va da și calea pentru un folder de output în care programul va crea pentru fiecare fișier de input, fișierul sau fișierele cu rezultatele. Tot în linia de comandă se va da ca parametru și numărul de soluții de calculat (de exemplu, vrem primele NSOL=4 soluții returnate de fiecare algoritm). Ultimul parametru va fi timpul de timeout. Se va descrie în documentație forma în care se apelează programul, plus 1-2 exemple de apel.
(5%) Citirea din fisier + memorarea starii. Parsarea fișierului de input care respectă formatul cerut în enunț
(15%) Functia de generare a succesorilor
(5%) Calcularea costului pentru o mutare
(10%) Testarea ajungerii în starea scop (indicat ar fi printr-o funcție de testare a scopului)
(15% = 2+5+5+3 ) 4 euristici:
(2%) banala
(5%+5%) doua euristici admisibile posibile (se va justifica la prezentare si in documentație de ce sunt admisibile)
(3%) o euristică neadmisibilă (se va da un exemplu prin care se demonstrează că nu e admisibilă). Atenție, euristica neadmisibilă trebuie să depindă de stare (să se calculeze în funcție de valori care descriu starea pentru care e calculată euristica).
(10%) crearea a 4 fisiere de input cu urmatoarele proprietati:
un fisier de input care nu are solutii
un fisier de input care da o stare initiala care este si finala (daca acest lucru nu e realizabil pentru problema, aleasa, veti mentiona acest lucru, explicand si motivul).
un fisier de input care nu blochează pe niciun algoritm și să aibă ca soluții drumuri lungime micuță (ca să fie ușor de urmărit), să zicem de lungime maxim 20.
un fisier de input care să blocheze un algoritm la timeout, dar minim un alt algoritm să dea soluție (de exemplu se blochează DF-ul dacă soluțiile sunt cât mai "în dreapta" în arborele de parcurgere)
dintre ultimele doua fisiere, cel putin un fisier sa dea drumul de cost minim pentru euristicile admisibile si un drum care nu e de cost minim pentru cea euristica neadmisibila
(15%) Pentru cele NSOL drumuri(soluții) returnate de fiecare algoritm (unde NSOL e numarul de soluții dat în linia de comandă) se va afișa:
numărul de ordine al fiecărui nod din drum
lungimea drumului
costului drumului
timpul de găsire a unei soluții (atenție, pentru soluțiile de la a doua încolo timpul se consideră tot de la începutul execuției algoritmului și nu de la ultima soluție)
numărul maxim de noduri existente la un moment dat în memorie
numărul total de noduri calculate (totalul de succesori generati; atenție la DFI și IDA* se adună pentru fiecare iteratie chiar dacă se repetă generarea arborelui, nodurile se vor contoriza de fiecare dată afișându-se totalul pe toate iterațiile
între două soluții de va scrie un separator, sau soluțiile se vor scrie în fișiere diferite.
Obținerea soluțiilor se va face cu ajutorul fiecăruia dintre algoritmii studiați:

Pentru studenții de la seria CTI problema se va rula cu algoritmii: BF, DF, DFI, UCS, Greedy, A*.
Pentru studenții din seriile Mate-Info și Informatică, problema se va rula cu algoritmii: UCS, A* (varianta care dă toate drumurile), A* optimizat (cu listele open și closed, care dă doar drumul de cost minim), IDA*.
Pentru toate variantele de A* (cel care oferă toate drumurile, cel optimizat pentru o singură soluție, și IDA*) se va rezolva problema cu fiecare dintre euristici. Fiecare din algoritmi va fi rulat cu timeout, si se va opri daca depășește acel timeout (necesar în special pentru fișierul fără soluții unde ajunge să facă tot arborele, sau pentru DF în cazul soluțiilor aflate foarte în dreapta în arborele de parcurgere).
(5%) Afisarea in fisierele de output in formatul cerut
(5%) Validări și optimizari. Veți implementa elementele de mai jos care se potrivesc cu varianta de temă alocată vouă:
găsirea unui mod de reprezentare a stării, cât mai eficient
verificarea corectitudinii datelor de intrare
găsirea unor conditii din care sa reiasă că o stare nu are cum sa contina in subarborele de succesori o stare finala deci nu mai merita expandata (nu are cum să se ajungă prin starea respectivă la o stare scop)
găsirea unui mod de a realiza din starea initială că problema nu are soluții. Validările și optimizările se vor descrie pe scurt în documentație.
(5%) Comentarii pentru clasele și funcțiile adăugate de voi în program (dacă folosiți scheletul de cod dat la laborator, nu e nevoie sa comentați și clasele existente). Comentariile pentru funcții trebuie să respecte un stil consacrat prin care se precizează tipul și rolurile parametrilor, căt și valoarea returnată (de exemplu, reStructured text sau Google python docstrings).
(5%) Documentație cuprinzând explicarea euristicilor folosite. În cazul euristicilor admisibile, se va dovedi că sunt admisibile. În cazul euristicii neadmisibile, se va găsi un exemplu de stare dintr-un drum dat, pentru care h-ul estimat este mai mare decât h-ul real. Se va crea un tabel în documentație cuprinzând informațiile afișate pentru fiecare algoritm (lungimea și costul drumului, numărul maxim de noduri existente la un moment dat în memorie, numărul total de noduri). Pentru variantele de A* vor fi mai multe coloane în tabelul din documentație: câte o coloană pentru fiecare euristică. Tabelul va conține datele pentru minim 2 fișiere de input, printre care și fișierul de input care dă drum diferit pentru euristica neadmisibilă. În caz că nu se găsește cu euristica neadmisibilă un prim drum care să nu fie de cost minim, se acceptă și cazul în care cu euristica neadmisibilă se obțin drumurile în altă ordine decât crescătoare după cost, adică diferența să se vadă abia la drumul cu numărul K, K>1). Se va realiza sub tabel o comparație între algoritmi și soluțiile returnate, pe baza datelor din tabel, precizând și care algoritm e mai eficient în funcție de situație. Se vor indica pe baza tabelului ce dezavantaje are fiecare algoritm.
Doar pentru studenții de la seria CTI: se dă bonus 10% pentru implementarea Greedy și analizarea acestuia împreună cu ceilalți algoritmi.
Doar pentru studenții de la seria CTI: se dă bonus câte 10% pentru fiecare dintre următoarele optimizări pentru cazul în care se cere o singură soluție (deci în program veți avea un if care verifică dacă numărul inițial de soluții cerut era 1):
la BF să se returneze drumul imediat ce nodul scop a fost descoperit, și nu neapărat când ajunge primul în coadă
la UCS+A* (bonusul ar fi 10%+10% dacă se face pt ambele) să nu avem duplicate ale informației din noduri în coadă. În cazul în care tocmai dorim să adăugăm un nod în coadă și vedem că există informația lui deja, păstram în coadă, dintre cele 2 noduri doar pe cel cu costul cel mai mic
Tema nu se puncteaza fara prezentare. Se va da o nota pe prezentare de la 1 la 10 in functie de cat de bine a stiut studentul sa explice ce a facut. Punctajul temei se va inmulti cu nota_prezentare/10. Astfel, daca cineva stie sa explice doar jumatate din ce a facut, primeste jumatate din punctaj; daca nu stie nimic primeste 0.

Temele copiate duc la anularea notei atat pentru cel care a dat tema cat si pentru cel care a copiat, iar numele studentilor cu aceasta problema vor fi comunicate profesorului titular de curs.









<div style="font-weight:normal">
				<div class="exercitiu">
				<b>Atentie! acest exercitiu necesita prezentare!</b><br>Identificator: <b>ex-cautare-informata-exemple-modificate</b><br>	
	
<hr class="despartitor_tema">
<p>Pornind de la programul problemei blocurilor scrieti un program asemanator in care se considera ca fiecare bloc contine un numar si are o anumita culoare.</p>

<p>Exemplu de stare initiala:</p>
<figure>
<img class="w200" src="./imagini/exercitii/ex-cautare-informata-exemple-modificate/pb-blocuri/pb-blocuri-culori-numere(stare-initiala).png" alt="configuratie initiala">
</figure>

<p>Mutarea blocurilor se face cu urmatoarele restrictii si efecte:</p>
<ul>
	<li>putem muta un bloc b1 peste alt bloc b2 doar dacă cele două au culori diferite. In plus, pe stivele vecine din stanga si/sau din dreapta, daca exista blocuri la acelasi nivel cu noua pozitie a lui b1, macar unul din cele 2 blocuri vecine trebuie sa aiba aceeasi paritate cu blocul b1 mutat. Dacă stivele vecine nu ajung la înălțimea blocului mutat, aceasta restricție nu se aplică.</li>
	<li>
	daca mutam un bloc b1 cu culoarea c peste un bloc b2 si sub blocul b2 se afla un bloc b3 cu aceeasi culoare c, blocul b2 capata culoarea c.</li>
</ul>
<p>De exemplu, pentru starea de mai sus, nu putem muta 1 peste 5 sau 10 pentru ca au aceeasi culoare. De asemenea, nu putem muta 10 peste 2 deoarece avem blocuri in stanga si dreapta si niciunul nu este par. Tot din acelasi motiv nu putem muta 2 peste 10 (deoarece exista un bloc in stanga noii pozitii (3) care este impar).</p>


<p>Exemplu de mutare valida din starea initiala oferita ca exemplu:</p>
<figure>
<img class="w200" src="./imagini/exercitii/ex-cautare-informata-exemple-modificate/pb-blocuri/pb-blocuri-culori-numere(mutare 1a).png" alt="configuratie initiala">
</figure>
<p>Putem continua apoi mutandu-l pe 2 peste 7 cand avem si un caz de schimbare a culorii:</p>
<figure>
<img class="w200" src="./imagini/exercitii/ex-cautare-informata-exemple-modificate/pb-blocuri/pb-blocuri-culori-numere(mutare 2a).png" alt="configuratie initiala">
</figure>

<p><b>Costul</b> mutarii unui bloc este dat de numarul scris pe el adunat cu inaltimea stivei de pe care e luat.</p>

<p>O stare e considerata <b>scop</b> daca toate stivele au in varf aceeasi culoare (precizată in fisierul de intrare). <strong>Atenție, astea înseamnă că în starea scop nu putem avea stive nevide!</strong>
</p>
<p>Exemplu de stare posibila finala, pentru cazul in care avem culoarea rosie drept culoare scop (pentru anumite blocuri s-a schimbat culoarea in urma unor mutari):</p>
<figure>
<img class="w200" src="./imagini/exercitii/ex-cautare-informata-exemple-modificate/pb-blocuri/pb-blocuri-culori-numere(stare-finala-rosu).png" alt="configuratie initiala">
</figure>
<p>Deci pot fi mai multe stari finale posibile pentru aceeasi configuratie initiala si testarea atingerii scopului trebuie facuta prin verificarea conditiei, NU prin enumerarea posibilitatilor de nod scop.
</p>







<!------------------------- input --------------------------->

<b>Fisierul de intrare</b> va conține pe primul rând culoarea care trebuie să se găsească în vârful stivelor scop, iar, dedesubt, starea inițială (stivele cu blocurile). O stare în fișierul de input se va reprezenta astfel:<p></p>
<ul>
	<li>fiecare stivă pe câte un rând. Se consideră că baza stivei e la stânga și vârful stivei e la dreapta.</li>
	<li>blocurile de pe o stivă se vor reprezenta prin: informatiile blocurilor separate de "/" (slash)</li>
	<li>informația dintr-un bloc va fi sub forma numar[culoare]. Culoarea nu trebuie sa aiba numele complet. O putem codifica și printr-o literă, de exemplu r pentru roșu, a pentru albastru etc.</li>
	<li>Stivele vide se evidențiază prin "-" (minus)</li>
</ul>


<p>
De exemplu, pentru starea inițială de mai jos  și culoarea cerută galben (g):</p>
<figure>
<img class="w200" src="./imagini/exercitii/ex-cautare-informata-exemple-modificate/pb-blocuri/pb-blocuri-culori-numere(initiala-stiva-vida).png" alt="configuratie initiala cu stivă vidă">
</figure>
<p>
fișierul de intrare ar fi:
<samp class="output">
g<br>
4[r]/9[g]/7[a]/10[r]<br>
8[a]/1[g]<br>
11[g]/3[a]/5[r]<br>
-<br>
8[r]/2[g]<br>
</samp>
</p>







<!------------------------- output --------------------------->
<p><b>Model fișier output.</b> O stare în fișierul de output se va reprezenta afișând stivele de sus în jos, toate aliniate la bază. Afișarea unei configurații va avea un număr de rânduri egal cu înălțimea celei mai înalte stive. Dacă o stivă nu ajunge pănă la un anumit nivel în locul în care trebuia afișat blocul ei se vor pune spații (deci, dacă e cazul într-o stare finală, pentru stivă vidă vom avea spațiu începând cu cel mai de jos nivel). Pentru un bloc pe stivă se va afișa informația lui în formatul fișierului de intrare, adica numar[culoare]. Între două stive se va afișa o coloană de spații. Toate blocurile dintr-o stivă încep de la aceeași coloană în zona de afișare. Sub fiecare configurație se va afișa o linie de simboluri "-"(minus) care începe de sub prima stivă și se termină la ultima.</p>
<p>În afișarea drumului, configurațiile (nodurile) apar în ordine cronologică, numerotate (cu indice între 1 si ND, unde ND e numărul de noduri din drum). Se afișează pe o linie separată indicele și dedesubt configurația corespunzătoare.</p>
<p>Între două soluții se va afișa un separator, de exemplu "##########################". </p>
<p>De exemplu, pentru configurația de mai jos, dacă ar fi în fișierul de output
</p><figure>
<img class="w200" src="./imagini/exercitii/ex-cautare-informata-exemple-modificate/pb-blocuri/pb-blocuri-culori-numere(stare-finala-galben).png" alt="configuratie finala">
</figure>
presupunând ca e al 7-lea nod într-un drum, am avea:
<samp class="output">
7)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5[g] <br>
9[g] 1[g] 3[g]&nbsp;&nbsp;7[g]&nbsp;&nbsp;2[g]<br>
4[r] 8[a] 11[g] 10[r] 8[r]<br>
--------------------------
</samp>





<hr class="despartitor_tema">

				
				<div style="background-color:#eae6f8 ; border: 1px dashed #67d3ea"><b>Upload:</b><label for="file">Alege fisier:</label> <input type="file" name="fisier2[]" id="fisier2" multiple="multiple"> <br>

							<input type="hidden" name="numefis2" id="numefis2" value="ex-cautare-informata-exemple-modificate.txt">
<input type="submit" value="Uploadeaza"><br>
<br><b><i>Fisiere uploadate:</i></b> 
-
				  
			   </div>


			</div></div>

import time
from search import *
from Cars import *

def main():

    name = "Marcu Andrei"
    print("{}, Problema nr.".format(name), 1 + (sum(map(ord,name)) % 4)) #calcul nr problema
    print('\n------------------------------------------------------------------------------------------------------------------\n')

    print("\n Programul va testa mai multe euristici intr-un numar limitat de iteratii dat de mine deoarece unele euristici rezolva mult mai rapid problema")
    print("\n Exista insa si cazuri care nu sunt rezolvabile cu niciuna din euristici in numarul de iteratii dat de mine, asadar nu va afisa o solutie")
    print("\n Numarul de iteratii este determinat in functie de dimensiunea matricii, formula fiind matrix_size^2 * 1000 iteratii")
    print("\n Starea initiala este generata random, iar starea finala este generata in functie de starea initiala\n")
    
    matrix_size = int(input("Matrix_size = ")) #citire dimensiune matrice
    initial = []
    goal = []
    generate_state(initial,goal,matrix_size) #generate state initial si goal

    print("Initial: ", tuple(initial))
    print("Goal:    ", tuple(goal))


    carsMiss = Cars(tuple(initial), tuple(goal))
    carsMht = CarsMht(tuple(initial), tuple(goal))
    carsDist = CarsDist(tuple(initial), tuple(goal))
    carsMisColRow = CarsMisColRow(tuple(initial), tuple(goal))
    carsDiagonal = CarsDiagonalDistance(tuple(initial), tuple(goal))

    cnt = 0 #variabila folosita pentru a afisa mesajul in cazul in care problema nu este rezolvata de niciuna dintre euristici in numarul de iteratii dat

    #Aici m-am folosit de exceptii pentru a opri executia unei euristici in cazul in care dureaza prea mult si alte euristici ar putea rezolva aceasta problema mult mai rapid
    #Asadar toate euristiciile sunt limitate la un numar cunoscut de pasi(matrix_size ^ 2 * 1000)
    #Aceasta limitare poate fi eliminata/modificata din functia result din fisierul Cars.py, clasa Cars

    try:
        print("Rezolvare folosind euristica Diagonal Distance adaptata pentru problema nostra:")
        t1 = time.time()
        astar_search(carsDiagonal).solution()
        t2 = time.time()
        print('\nRealizat in :', t2 - t1)
        print("\n\nRealizat in : {} iteratii".format(carsDiagonal.total_iterations))
    except:
        cnt += 1
        print("Nu a fost gasita o solutie folosind Diagonal Distance in numarul de iteratii dat")
        pass
 
    try:
        print("Rezolvare folosind euristica Manhattan Distance:")
        t1 = time.time()
        astar_search(carsMht).solution()
        t2 = time.time()
        print('\nRealizat in :', t2 - t1)
        print("\n\nRealizat in : {} iteratii".format(carsMht.total_iterations))
    except:
        cnt += 1
        print("Nu a fost gasita o solutie folosind Manhattn Distance in numarul de iteratii dat")
        pass

    try:
        print("Rezolvare folosind euristica cu distanta dintre pozitia actuala a piesei si destinatie:")
        t1 = time.time()
        astar_search(carsDist).solution()
        t2 = time.time()
        print('\nRealizat in :', t2 - t1)
        print("\n\nRealizat in : {} iteratii".format(carsDist.total_iterations))
    except:
        cnt += 1
        print("Nu a fost gasita o solutie folosind distanta dintre pozitia actuala a piesei si destinatie in numarul de iteratii dat")
        pass 

    try:
        print("Rezolvare folosind euristica cu masini missplaced:")
        t1 = time.time()
        astar_search(carsMiss).solution()
        t2 = time.time()
        print('\nRealizat in :', t2 - t1)
        print("\n\nRealizat in : {} iteratii".format(carsMiss.total_iterations))
    except:
        cnt += 1
        print("Nu a fost gasita o solutie folosind euristica misplaced in numarul de iteratii dat")
        pass   

    try:
        print("Rezolvare folosind euristica cu nr de piese plasate gresit pe linie si coloana :")
        t1 = time.time()
        astar_search(carsMisColRow).solution()
        t2 = time.time()
        print('\nRealizat in :', t2 - t1)
        print("\n\nRealizat in : {} iteratii".format(carsMisColRow.total_iterations))
    except:
        cnt += 1
        print("Nu a fost gasita o solutie folosind euristica cu nr de piese plasate gresit pe linie si coloana in numarul de iteratii dat")
        pass

    if cnt == 5:
        print("Euristicile nu au reusit sa gaseasca o solutie in mai putin de {} de iteratii".format(len(initial) * 1000))

if __name__ == "__main__":
    main()

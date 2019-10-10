import time
from search import *
import P1
import P2

def main():
    #water jug problem
    print("Water jug problem:")
    water_jug = P1.WaterJug((0,0), (2,0))
    t1 = time.time()
    print(breadth_first_tree_search(water_jug).solution())
    t2 = time.time()
    exe_time = t2-t1
    print("Realizat in : %.8f secunde folosind breadth_first_tree_search" % exe_time)
    print("Rezultat: ", breadth_first_tree_search(water_jug).state)

    #15 puzzle problem
    print("\n\n15 Puzzle problem:")

    puzzle_15 = P2.Puzzle15((5,1,7,3,9,2,11,4,13,6,15,8,0,10,14,12), (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0))
    puzzle_15_mis_dist = P2.Puzzle15MisDist((5,1,7,3,9,2,11,4,13,6,15,8,0,10,14,12), (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0))
    puzzle_15_mis_col_row = P2.Puzzle15MisColRow((5,1,7,3,9,2,11,4,13,6,15,8,0,10,14,12), (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0))


    print("\nInitial : ",puzzle_15_mis_dist.initial)
    t1 = time.time()
    print(astar_search(puzzle_15_mis_dist).solution())
    t2 = time.time()
    exe_time = t2-t1
    print("Realizat in : %.8f secunde folosind A* cu heuristica care calculeaza suma elementelor misplaced si distanta dintre acestea" % exe_time)
    print("Rezultat : ", astar_search(puzzle_15_mis_dist).state)

    print("\nInitial : ", puzzle_15_mis_col_row.initial)
    t1 = time.time()
    print(astar_search(puzzle_15_mis_col_row).solution())
    t2 = time.time()
    exe_time = t2-t1
    print("Realizat in : %.8f secunde folosind A* cu heuristica care calculeaza suma elementelor misplaced de pe fiecare coloana si linie" % exe_time)
    print("Rezultat : ", astar_search(puzzle_15_mis_col_row).state)

    print("\nInitial : ",puzzle_15.initial)
    t1 = time.time()
    print(astar_search(puzzle_15).solution())
    t2 = time.time()
    exe_time = t2-t1
    print("Realizat in : %.8f secunde folosind A* cu heuristica initiala" % exe_time)
    print("Rezultat : ", astar_search(puzzle_15).state)



if __name__ == "__main__":
    main()

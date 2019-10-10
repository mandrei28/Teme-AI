from search import Problem
import math
from queue import *
import random

class Cars(Problem):

    def __init__(self, initial, goal = None):
        """ Define goal state and initialize a problem """
        self.goal = goal
        self.matrix_size = int(math.sqrt(len(initial)))
        self.total_iterations = 0
        self.cars = Queue(self.matrix_size) # o coada in care salvam ordinea in care se muta masinile
        self.delta = {'UP': -self.matrix_size, 'DOWN': self.matrix_size, 'LEFT':-1, 'RIGHT':1, 'JUMPLEFT':-2, 'JUMPRIGHT':2, 'JUMPDOWN':2 * self.matrix_size, 'JUMPUP':-2 * self.matrix_size, 'STAY':0}
        for i in range (1, self.matrix_size + 1):
            self.cars.put(i) # umplem coada cu masini de la 1 la matrix_size+1
        Problem.__init__(self, initial, goal)


    def actions(self, state):
        
        possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT', 'JUMPLEFT', 'JUMPRIGHT', 'JUMPUP', 'JUMPDOWN', 'STAY']

        x = self.cars.get() #de fiecare data cand scoatem o masina o punem din nou la sfarsit in coada
        self.cars.put(x)
        #aceasta coada ne ajuta sa mentinem ordinea in care se vor efectua miscarile


        self.index = state.index(x)

        if(self.goal[self.index] == state[self.index]): #daca am ajuns la destinatie facem doar STAY
            possible_actions = ['STAY']
            return possible_actions

        if self.index % self.matrix_size == 0 or state[self.index - 1] != 0: #daca suntem pe prima coloana sau daca avem o alta masina in stanga stergem LEFT
            possible_actions.remove('LEFT')

        if self.index % self.matrix_size == self.matrix_size - 1 or state[self.index + 1] != 0: # daca suntem pe ultima coloana sau daca avem masina in dreapta stergem RIGHT
            possible_actions.remove('RIGHT')

        if self.index < self.matrix_size or state[self.index - self.matrix_size] != 0: # suntem pe prima linie sau daca avem masina deasupra stergem UP 
            possible_actions.remove('UP')
            
        if self.index > (pow(self.matrix_size, 2) - self.matrix_size - 1) or state[self.index + self.matrix_size] != 0: # daca suntem pe ultima linie sau daca avem masina sub eliminam DOWN
            possible_actions.remove('DOWN')
        

        if self.index - 2 >= 0 and self.index - 1 >= 0: # verificam daca prin salt masina va iesi din matrice
            #daca suntem pe prima sau a 2-a coloana, daca nu avem masina in stanga sau daca avem masina 2 pozitii in stanga eliminam JUMPLEFT
            if self.index % self.matrix_size == 1 or self.index % self.matrix_size == 0  or state[self.index-1] == 0 or state[self.index-2] != 0:
                possible_actions.remove('JUMPLEFT')
        else:
            possible_actions.remove('JUMPLEFT')
        
        if self.index + 2 < self.matrix_size * 2 and self.index+1 < self.matrix_size * 2: # verificam daca prin salt masina va iesi din matrice
            #daca suntem pe ultima sau penultima coloana, daca nu avem masina in dreapta sau daca avem masina 2 pozitii in dreapta eliminam JUMPRIGHT
            if self.index % self.matrix_size == 1 or self.index % self.matrix_size == 2 or state[self.index+1] == 0 or state[self.index+2] != 0:
                possible_actions.remove('JUMPRIGHT')
        else:
            possible_actions.remove('JUMPRIGHT')
        
        if self.index - self.matrix_size >= 0 and self.index - 2 * self.matrix_size >= 0: # verificam daca prin salt masina va iesi din matrice
            #daca suntem pe prima sau a 2-a linie, daca nu avem masina deasupra sau daca avem masina 2 pozitii mai sus eliminam JUMPUP
            if self.index < 2 * self.matrix_size or state[self.index-self.matrix_size] == 0 or  state[self.index - 2 * self.matrix_size] != 0:
                possible_actions.remove('JUMPUP')
        else:
            possible_actions.remove('JUMPUP')

        if self.index+self.matrix_size < self.matrix_size * 2 and self.index+2 * self.matrix_size < self.matrix_size * 2: # verificam daca prin salt masina va iesi din matrice
            #daca suntem pe ultima sau penultima linie, daca nu avem masina sub sau daca avem masina 2 pozitii mai jos eliminam JUMPDOWN
            if self.index > pow(self.matrix_size, 2) - 2 * self.matrix_size - 1 or state[self.index+self.matrix_size] == 0 or  state[self.index+2 * self.matrix_size] != 0:
                possible_actions.remove('JUMPDOWN')
        else:
            possible_actions.remove('JUMPDOWN')
               
        return possible_actions

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """
        # blank is the index of the blank square
        self.total_iterations += 1 # limita de iteratii
        if(self.total_iterations > pow(self.matrix_size,2) * 1000): # in cazul in care s-a ajuns la nr de iteratii dorit lansam o exceptie pentru a sari peste aceasta executie
            raise Exception

        new_state = list(state) # aici vom salva noul state
       
        neighbour = self.index + self.delta[action] # calculam noua pozitie a masinii si o salvam
        new_state[self.index], new_state[neighbour] = new_state[neighbour], new_state[self.index] # interschimbam pozitia masinei cu noua pozitie

        return tuple(new_state)

    def h(self, node):
        """ Return the heuristic value for a given state. Default heuristic function used is
        h(n) = number of misplaced tiles """

        return sum(s != g for (s, g) in zip(node.state, self.goal)) #euristica initiala, numarul de piese plasate gresit.

class CarsDiagonalDistance(Cars): #euristica optima, este o adaptare a Chebyshev distance pentru operatii de jump.
    def h(self, node):
        dx = 0
        dy = 0
        for i in range(1, self.matrix_size + 1):
            s = node.state.index(i)
            g = self.goal.index(i)
            dx += abs((s//self.matrix_size) - (g//self.matrix_size)) #suma distantelor dintre x-ul curent si destinatie
            dy += abs((s%self.matrix_size) - (g%self.matrix_size)) #suma distantelor dintre y-ul curent si destinatie
        return 1 * (dx + dy) + (2 * self.matrix_size - 2 * 1) * min(dx,dy) # O adaptare a formulei lui Chebyshev pentru distanta, 1 fiind costul pentru o deplasare normala iar 2*matrix_size costul pentru o deplasare de tip JUMP


class CarsMht(Cars): #euristica folosind Manhattan distance, aceasta nu este optima pe toate cazurile deoarece avem si operatii de jump
    def h(self, node):
        return sum( ( abs((s // self.matrix_size) - (g // self.matrix_size)) + abs((s % self.matrix_size) - (g % self.matrix_size)) ) for (s,g) in zip (node.state, self.goal) )



class CarsDist(Cars): #calculeaza distanta dintre piesele asezate gresit si pozitia pe care ar trebui sa o aiba aceste piese. Nu este optima pe majoritatea cazurilor
    def h(self, node):

        dist = 0 # the distance between the misplaced tiles
        for i in node.state:
            if node.state[i] != self.goal[i]: #daca piesa e asezata gresit
                dist += math.fabs(node.state.index(i) - self.goal.index(i)) #calculam distanta dintre aceasta si destinatie

        return dist #returnam suma distantelor
    
        
class CarsMisColRow(Cars):#calculeaza numarul de piese amplasate gresit pe coloana si linie si returneaza suma acestora
    def h(self, node):

        misplaced_row = 0 # number of misplaced tiles on rows
        misplaced_col = 0 # number of misplaced tiles on columns

        for i in range(pow(self.matrix_size, 2)):
            if node.state[i] != self.goal[i]: #daca piesa e asezata gresit
                for j in range(self.matrix_size - 1):

                    if i % self.matrix_size == j: # daca se afla pe coloana j incrementam numarul de piese plasate gresit pe coloana
                        misplaced_col += 1
                    if i // self.matrix_size == j: # daca se afla pe linia j incrementam numarul de piese plasate gresit pe coloana
                        misplaced_row += 1

        total_heurst = misplaced_col + misplaced_row
        
        return total_heurst




def generate_state(initial, goal, matrix_size): # creeaza un input initial random si generaza goal-ul pentru inputul respectiv
    for iterator in range ( pow(matrix_size,2)):
        if iterator < matrix_size: #daca suntem pe prima linie
            value = random.randint(1, matrix_size)
            while value in initial: # daca valoarea generata random exista deja in matrice vom genera pana avem o valoare noua
                value = random.randint(1, matrix_size)
            initial.append(value) # introducem valoarea din lista
        else: #daca nu suntem pe prima linie
            initial.append(0)
        
    for iterator in range (pow(matrix_size,2)):
        if iterator < pow(matrix_size, 2) - matrix_size: #daca nu suntem pe ultima linie
            goal.append(0)
        else: #daca suntem pe ultima linie
            matrix_size -= 1
            goal.append(initial[matrix_size]) #introducem in goal elementul de pe pozitia matrix_size care va fi decrementat la fiecare pas, astfel realizand goal-ul in ordine inversa fata de state-ul initial

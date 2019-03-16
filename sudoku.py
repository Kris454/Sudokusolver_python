import os
import sys

def generate_graph4():
    graph = {}
    group = []
    firstofblockfor4 = [1,3,9,11]
    b = 0
    for x in xrange(1, n*n+1):
        graph[x] = set([])
    for x in xrange(1, n*n+1):
        div = (x-1)/n
        for y in xrange (1, n+1):
            if x != ((div*n)+y):
                graph[x].add((div*n)+y)
        mul = x % n
        if mul == 0:
            mul = n
        for z in xrange (0, n):
            if x != ((n*z)+mul):
                graph[x].add((n*z)+mul)
    
    for x in firstofblockfor4:
        b = b+1
        group.append([])
        group[b].append(x)
        group[b].append(x+1)
        group[b].append(x+4)
        group[b].append(x+5)
    
    for x in xrange(1, n+1):        #add egdes in boxes
        for y in group[x]:
            for z in group[x]:
                if y != z:
                    graph[y].add(z)
    return graph    
                
def generate_graph9():
    graph = {}
    group = []
    firstofblockfor9 = [1,4,7,28,31,34,55,58,61]
    b = 0
    for x in xrange(1, n*n+1):
        graph[x] = set([])
    for x in xrange(1, n*n+1):
        div = (x-1)/n
        for y in xrange (1, n+1):
            if x != ((div*n)+y):
                graph[x].add((div*n)+y)
        mul = x % n
        if mul == 0:
            mul = n
        for z in xrange (0, n):
            if x != ((n*z)+mul):
                graph[x].add((n*z)+mul)

    group.append([])   #group indexes to create edges in boxes 

    for x in firstofblockfor9:
        b = b+1
        group.append([])
        group[b].append(x)
        group[b].append(x+1)
        group[b].append(x+2)
        group[b].append(x+9)
        group[b].append(x+10)
        group[b].append(x+11)
        group[b].append(x+18)
        group[b].append(x+19)
        group[b].append(x+20)

    for x in xrange(1, n+1):        #add egdes in boxes
        for y in group[x]:
            for z in group[x]:
                if y != z:
                    graph[y].add(z)
    return graph

def generate_graph6():
    graph = {}
    group = []
    firstofblockfor6 = [1,3,5,19,21,23]
    b = 0
    for x in xrange(1, n*n+1):
        graph[x] = set([])
    for x in xrange(1, n*n+1):
        div = (x-1)/n
        for y in xrange (1, n+1):
            if x != ((div*n)+y):
                graph[x].add((div*n)+y)
        mul = x % n
        if mul == 0:
            mul = n
        for z in xrange (0, n):
            if x != ((n*z)+mul):
                graph[x].add((n*z)+mul)
    
    group.append([])
    for x in firstofblockfor6:
        b = b+1
        group.append([])
        group[b].append(x)
        group[b].append(x+1)
        group[b].append(x+6)
        group[b].append(x+7)
        group[b].append(x+12)
        group[b].append(x+13)
    
    for x in xrange(1, n+1):       
        for y in group[x]:
            for z in group[x]:
                if y != z:
                    graph[y].add(z)
    return graph

def check_sudoku():
    for x in sudoku:
        if Colors[x] != 0:
            tmp = Colors[x]
            if tmp > n:
                print "Wrong digits in Sudoku"
                return False
            for y in sudoku[x]:
                if tmp == Colors[y]:
                    print "Wrong Sudoku"
                    print "The same digits on position" + str(y) + " i  " + str(x)
                    return False
    return True

def print_sudoku4(Table):
    poz = 2
    box = 8
    end = 16
    print "+--+--+"
    sys.stdout.write("|")
    
    for x in xrange(1,end+1):
        y = str(Table[x])
        sys.stdout.write(str(y))
        if(x % poz == 0):
            sys.stdout.write("|")
        sys.stdout.flush()
        if(x % n == 0 ):
            print ""
            if(x % box == 0 and x < end-1 ):
                print "+--+--+"
            if(x < end):
                sys.stdout.write("|")
            if(x == end):
                print "+--+--+"
    
def print_sudoku6(Table):
    poz = 2
    box = 18
    end = 36
    print "+--+--+--+"
    sys.stdout.write("|")
    
    for x in xrange(1,end+1):
        y = str(Table[x])
        sys.stdout.write(str(y))
        if(x % poz == 0):
            sys.stdout.write("|")
        sys.stdout.flush()
        if(x % n == 0 ):
            print ""
            if(x % box == 0 and x < end-1 ):
                print "+--+--+--+"
            if(x < end):
                sys.stdout.write("|")
            if(x == end):
                print "+--+--+--+"


def print_sudoku9(Tablica):
    poz = 3
    box = 27
    end = 81
    print "+---+---+---+"

    sys.stdout.write("|")
    for x in xrange(1,end+1):
        y = str(Tablica[x])
        sys.stdout.write(str(y))
        if(x % poz == 0):
            sys.stdout.write("|")
        sys.stdout.flush()
        if(x % n == 0 ):
            print ""
            if(x % box == 0 and x < end-1 ):
                print "+---+---+---+"
            if(x < end):
                sys.stdout.write("|")
            if(x == end):
                print "+---+---+---+"

def is_safe(source, c):
    """Is available color for vertex?"""  
    for target in sudoku[source]:   # Loop for adjacent 
        if Colors[target] == c:
            return False
    return True

def graph_color(k, k_colors): 
    """Node coloring with k colors using backtracking."""
    node = node_list[k]
    for c in xrange(1,k_colors):
         if is_safe(node, c):
            Colors[node] = c   # save color to table
            if k+1 < n*n:
                graph_color(k+1, k_colors)
            else:
                print "Solution"
                if(n==9):
                    print_sudoku9(Colors)
                elif(n==4):
                    print_sudoku4(Colors)
                elif(n==6):
                    print_sudoku6(Colors)
                #print Colors 
            Colors[node] = None   # erase


Colors = [] # Table keep vertex color
i = 0 # number colored vertex at start
n = 0 # size of sudoku

print "Sudoku size 4: 4x4, 6: 6x6, 9: 9x9"
try:
    n = int(raw_input("Enter the size: "))
except ValueError:
    print "The vault is wrong"
if(n != 4 and n != 9 and n!=6):
    print ("You have entered unsupported size")
    sys.exit()
if(n==4):
    sudoku = generate_graph4()
elif(n==9):
    sudoku = generate_graph9()
elif(n==6):
    sudoku = generate_graph6()

try:
    nazwa = raw_input("Enter file name with sudoku: ")
    F = open(nazwa, "r")
except IOError: 
      print "IO error"

Colors = "0" + F.read().replace('\n', '') # parsing loaded file,  0 at begin because 0 indexing from 1
F.close()
Colors = map(int, Colors) 
node_list = list(sudoku) 

for x in xrange (1, n*n+1):  # Shift to the list begin colored nodes and cout them
    if Colors[x] != 0:
        node_list.remove(x)
        node_list.insert(0, x)
        i += 1

print "Loaded sudoku"
if(n==9):
    print_sudoku9(Colors)
elif(n==4):
    print_sudoku4(Colors)
elif(n==6):
    print_sudoku6(Colors)


if(check_sudoku() == False):
    sys.exit()
graph_color(i,k_colors=n+1)# n+1 colors because colors identified from 1 not from 0 



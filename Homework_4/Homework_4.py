import sys

Map = sys.stdin.read()#get the input
Map = Map.split('\n')#transform the data from string to list, each line to an element in the list
if len(Map) <= 0:#if the input is empty
    exit(0)#exit

i = 0
while i < len(Map):#skip the comments in the input
    if '$' in Map[i] or Map[i] == '':#if the line is comment
        Map.pop(i)#delete the comment
        continue
    i += 1

if len(Map) <= 2:#if the map is empty or the coordinates are not enough
    exit(0)#exit

start = Map[0].split()#get the coordinate of the start
start[0] = int(start[0])#transform the data in start coordinate from string to int
start[1] = int(start[1])#transform the data in start coordinate from string to int
start = tuple(start)#transform the start coordinate from list to tuple for convenience of later operation
goal = Map[1].split()#get the coordinate of the goal
goal[0] = int(goal[0])#transform the data in goal coordinate from string to int
goal[1] = int(goal[1])#transform the data in goal coordinate from string to int
goal = tuple(goal)#transform the goal coordinate from list to tuple for convenience of later operation

if Map[-1] == '':#get the true map and reform its format, need to begin with -2 in win
    Map = Map[-2:1:-1]
else:#but -1 in oj!
    Map = Map[-1:1:-1]

for k in range(len(Map)):#separate the string representing each line, and transform the Map into 2D-list
    Map[k] = list(Map[k])
width = len(Map[0])#get the width of the Map
height = len(Map)#get the height of the Map

def printPath(Map):#print the original Map and exit
    Map = Map[::-1]#get the Map of right form
    for r in range(len(Map)):#print the original Map
        for s in Map[r]:
            print(s,end = '')
        print('')
    exit()#exit

if Map[start[1]][start[0]] == 'X' or Map[goal[1]][goal[0]] == 'X':#if the coordinate of the start or goal is invalid
    printPath(Map)#print the original Map and exit

if not(0 <= start[1] <= len(Map) - 1 and 0 <= goal[1] <= len(Map) - 1 and  0 <= start[0] <= len(Map[0]) - 1 and 0 <= goal[0] <= len(Map[0]) - 1 ):#if the start or the goal is out of range
    printPath(Map)#print the original Map and exit

def neighbor(x,y):#get the valid neighbor coordinates of (x,y)
    L = [(x,y - 1),(x - 1,y - 1),(x - 1,y),(x - 1,y + 1),(x,y + 1),(x + 1,y + 1),(x + 1,y), (x + 1,y - 1)]#get the potential neighbor
    neighbor = []#create the empty list to store valid neighbor
    for l in L:#get the valid neighbor coordinates
        if 0 <= l[0] <= (width - 1) and 0 <= l[1] <= (height - 1):
            neighbor.append(l)
    return neighbor

distance = {}#create a dictionary to store the distance of every coordinate
for m in range(width):#set all the coordinates' distance as infinity
    for n in range(height):
        distance[(m,n)] = float('inf')
distance[start] = 0#set the start's distance as infinity
waveFront = [start]#put the start into waveFront(active set)
node = start#set the begin node as start
while waveFront != []:#once the waveFront is empty, the distance of coordinate that can be calculated has all been calculated, so leave the loop
    minDistNode = None
    for p in waveFront:#select the ﬁrst node with the minimum dist value from the waveFront
        if minDistNode == None:
            minDistNode = p
        else:
            if distance[p] < distance[minDistNode]:
                minDistNode = p
    node = minDistNode
    waveFront.remove(node)#remove the node from the waveFront
    if node == goal:#if the distances of all the coordinates on the way from start to goal has been calculated
        break#leave the loop

    neighbors = neighbor(node[0],node[1])#get the node's neighbor with valid coordinates
    for q in range(len(neighbors)):
        if Map[neighbors[q][1]][neighbors[q][0]] == '.':
            neighDist = distance[node] + ((neighbors[q][0] - node[0]) ** 2 + (neighbors[q][1] - node[1]) ** 2) ** 0.5
            if neighDist < distance[neighbors[q]]:
                distance[neighbors[q]] = neighDist#update the distance of the neighbor coordinates
                waveFront.append(neighbors[q])#add the neighbor coordinates to the waveFront(active set)

node_ = goal#find the path from the goal
while node != start:#when having found the way to start, leave the loop
    node = None
    neighbors = neighbor(node_[0],node_[1])#get the valid neighbor coordinates of node_
    for r in range(len(neighbors)):#get the coordinate closest to start in the neighbor coordinates
        if node == None:
            node = neighbors[r]
        else:
            if distance[neighbors[r]] < distance[node]:
                node = neighbors[r]

    if distance[node] != float('inf'):#only if the node is valid
        Map[node[1]][node[0]] = 'P'#set it as the path
    else:#if there is a wall that can not be passed between the start and the goal
        printPath(Map)#print the orginal map and exit
    node_ = node#find the path from the new 'P'

Map[goal[1]][goal[0]] = 'P'#set the goal as path, too
printPath(Map)#print the path and exit
class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def kdtree(point_list, axis=0):
    if not point_list:
        return None    
    
    point_list.sort(key=lambda p: p[axis])
    
    median = len(point_list) // 2

    newNode = Node(point_list[median])
    newNode.left = kdtree(point_list[:median], axis^1)
    newNode.right = kdtree(point_list[median + 1:], axis^1)
    return newNode



def traverse(subtree):
    if subtree is None:
        return    
    traverse(subtree.left)
    print(subtree.key)
    traverse(subtree.right)


# main function
# x = kdtree([(2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2)], 0)
# # print(x.key)
# traverse(x)








pqSize,k,p,q=0,0,0,0


# (distance from my query point, the point)
from json.encoder import INFINITY
from queue import PriorityQueue


priorityQ = PriorityQueue()


# euclidean distance
import math
def Edis(p,q,x,y):
    return math.sqrt((p-x)**2+(q-y)**2)

# find the k-nearest neighbors
def KNN(subtree, depth):
    global pqSize,k
    if(subtree == None):
        return
    nextBranch = Node(key=None, left=None, right=None)
    otherBranch = Node(key=None, left=None, right=None)
    # decide which subtree to visit first
    x,y = subtree.key
    if(depth == 0):
        # x-axis
        if(x<p):
            nextBranch = subtree.left
            otherBranch = subtree.right
        else:
            nextBranch = subtree.right
            otherBranch = subtree.left
    else:
        # y-axis
        if(y<q):
            nextBranch = subtree.left
            otherBranch = subtree.right
        else:
            # print("y axis")
            nextBranch = subtree.right
            otherBranch = subtree.left
    


    KNN(nextBranch, depth+1)

    # find the distance between the query point and the current subtree root
    distance = Edis(p,q,subtree.key[0], subtree.key[1])

    
    if(pqSize < k):
        # if the size of priority queue is less than k, then we can add this point to the priority queue
        priorityQ.put((-1*distance, subtree))
        pqSize += 1
        # print('ke jabe ', subtree.location, pqSize)
    else:
        top = priorityQ.get()
        if(top[0]*-1 < distance):
            priorityQ.put(top)
        else:
            priorityQ.put((-distance, subtree))

    
    # check if the other subtree has any points
    worstbest = priorityQ.get()
    priorityQ.put(worstbest)

    radius = Edis(p,q,subtree.key[0], subtree.key[1])
    dist = INFINITY
    if depth==0:
        dist = abs(p-x)
    else:
        dist = abs(q-y)

    if(radius >= dist):
        KNN(otherBranch, depth+1)
    
    return
    



def main():    
    # point_list = [(7, 2), (5, 4), (9, 6), (4, 7), (8, 1), (2, 3)]
    point_list = [(5,4),(2,6),(13,3),(8,7),(3,1),(10,2)]
    tree = kdtree(point_list)
    
    global p,q,k
    p = 9
    q = 4
    k = 1
    KNN(tree, 0)

    print("distance", "co-ordinates")
    
    while not priorityQ.empty():
        x = priorityQ.get()
        print(format(x[0]*-1,".2f"), " -> ", x[1].key)

if __name__ == "__main__":
    main()
from cmath import inf
from queue import PriorityQueue
from re import sub


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





pqSize,k,p,q=0,0,0,0


# (distance from my query point, the point)

priorityQ = PriorityQueue()

# NOTE:
    # previouly i was storing the whole node
    # problem with that it's not comparaable
    # so when {distance, node}
        # the distance is same priority query don't know which one to put first

    # eg.
        # point_list = [(5,4),(2,6),(13,3),(8,7),(3,1),(10,2)]
        
        # p = 8
        # q = 4
        
        # k = 4



# euclidean distance
import math
def Edis(p,q,x,y):
    return math.sqrt((p-x)**2+(q-y)**2)


# find the k-nearest neighbors
def KNN(subtree, axis):
    global pqSize,k
    if(subtree == None):
        return

    nextBranch = otherBranch = Node(key=None, left=None, right=None)
    # decide which subtree to visit first
    x,y = subtree.key
    if(axis == 0):
        # x-axis
        nextBranch, otherBranch = (subtree.left, subtree.right) if(p < x) else (subtree.right, subtree.left)
    else:
        # y-axis
        nextBranch, otherBranch = (subtree.left, subtree.right) if(q < y) else (subtree.right, subtree.left)
    

    KNN(nextBranch, axis^1)

    # find the distance between the query point and the current subtree root
    distance = Edis(p,q,subtree.key[0], subtree.key[1])
    if(pqSize < k):
        priorityQ.put((-1*distance, subtree.key))
        pqSize += 1
    else:
        top = priorityQ.get()
        if(top[0]*-1 < distance):
            priorityQ.put(top)
        else:
            priorityQ.put((-distance, subtree.key))

    
    # check if the other subtree has any points
    worstbest = priorityQ.get()
    priorityQ.put(worstbest)
    radius = Edis(p,q,subtree.key[0], subtree.key[1])
    dist = abs(p-x) if(axis == 0) else abs(q-y)
    if(radius >= dist):
        KNN(otherBranch, axis^1)
    
    return
    



def main():    
    point_list = [(7, 2), (5, 4), (9, 6), (4, 7), (8, 1), (2, 3)]
    # point_list = [(5,4),(2,6),(13,3),(8,7),(3,1),(10,2)]
    tree = kdtree(point_list)
    
    global p,q,k
    p = 8
    q = 4
    k = 4
    KNN(tree, 0)

    print("distance", "co-ordinates")
    
    while not priorityQ.empty():
        x = priorityQ.get()
        print(format(x[0]*-1,".2f"), " -> ", x[1])

if __name__ == "__main__":
    main()



















































# priority queue
class priQueue:
    def __init__(self):
        self.pq_arr = []
        self.size = 0

    def put(self, item):
        self.size += 1
        self.pq_arr.append(item)
        self.pq_arr.sort(reverse=True)

    def get(self):
        if(self.size == 0):
            return
        self.size -= 1
        top = self.pq_arr[0]
        self.pq_arr.pop(0)
        return top
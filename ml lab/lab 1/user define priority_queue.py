class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right



def kdtree(point_list, depth=0):
    if not point_list:
        return None    
    

    axis = depth%len(point_list[0])
    point_list.sort(key=lambda p: p[axis])

    median = len(point_list) // 2

    newNode = Node(point_list[median])
    newNode.left = kdtree(point_list[:median], depth+1)
    newNode.right = kdtree(point_list[median + 1:], depth+1)
    return newNode




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

pq = priQueue()



k,p,q=0,0,0,



# euclidean distance
import math
def Edis(p,q,x,y):
    return math.sqrt((p-x)**2+(q-y)**2)




# find the k-nearest neighbors
def KNN(subtree, depth):
    global pqSize,k
    if(subtree == None):
        return

    nextBranch = otherBranch = Node(key=None, left=None, right=None)
    # decide which subtree to visit first
    x,y = subtree.key
    depth %= len(subtree.key)
    if(depth == 0):
        # x-axis
        nextBranch, otherBranch = (subtree.left, subtree.right) if(p < x) else (subtree.right, subtree.left)
    else:
        # y-axis
        nextBranch, otherBranch = (subtree.left, subtree.right) if(q < y) else (subtree.right, subtree.left)
    

    KNN(nextBranch, depth+1)

    # find the distance between the query point and the current subtree root
    distance = Edis(p,q,subtree.key[0], subtree.key[1])
    if(pq.size < k):
        pq.put((1*distance, subtree.key))
    else:
        top = pq.get()
        if(top[0]*1 < distance):
            pq.put(top)
        else:
            pq.put((distance, subtree.key))

    
    # check if the other subtree has any points
    worstbest = pq.get()
    pq.put(worstbest)
    radius = Edis(p,q,subtree.key[0], subtree.key[1])
    dist = abs(p-x) if(depth == 0) else abs(q-y)
    if(radius >= dist):
        KNN(otherBranch, depth+1)
    
    return
    



def main():
    
    point_list = [(7, 2), (5, 4), (9, 6), (4, 7), (8, 1), (2, 3)]
    # point_list = [(5,4),(2,6),(13,3),(8,7),(3,1),(10,2)]
    tree = kdtree(point_list)
    



    global p,q,k
    p = 8
    q = 4
    k = 3
    KNN(tree, 0)

    print("distance", "co-ordinates")

    while(pq.size > 0):
        x = pq.get()
        print(format(x[0],".2f"), " -> ", x[1])

if __name__ == "__main__":
    main()
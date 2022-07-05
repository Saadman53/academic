import random

class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def gameTree(arr, prev=0, depth=0):
    if not arr:
        return None
    first, last = arr[0], arr[-1]
    newNode = Node()
    if first > prev:
        newNode.left = gameTree(arr[1:], first, depth+1)
    if last > prev:
        newNode.right = gameTree(arr[:-1], last, depth+1)
    if newNode.left is None and newNode.right is None:
        if depth % 2 == 0:
            newNode.key = -1
        else:
            newNode.key = 1
    return newNode

def minimax(arr, node, depth=0, prev=0):
    if len(arr) == 1:
        return node.key
    first, last = arr[0], arr[-1]
    # max player
    if depth % 2 == 0:
        temp = -1
        if first > prev and node.left is not None:
            temp = max(temp, minimax(arr[1:], node.left, depth+1, first))
        if last > prev and node.right is not None:
            temp = max(temp, minimax(arr[:-1], node.right, depth+1, last))
        node.key = temp
        return node.key
    # min player
    if depth % 2 == 1:
        temp = 1
        if first > prev and node.left is not None:
            temp = min(temp, minimax(arr[1:], node.left, depth+1, first))
        if last > prev and node.right is not None:
            temp = min(temp, minimax(arr[:-1], node.right, depth+1, last))
        node.key = temp
        return node.key


def gamePlay(arr, node, depth=0, prev=0):
    if len(arr) == 1:
        return node.key
    print("\n\n")
    first, last = arr[0], arr[-1]
    # player 1's turn
    if depth % 2 == 0:
        if prev >= first and prev >= last:
            return -1
        newArr, last_selected, side = selectOption(arr, prev)
        if len(arr):
            if side == 'left':
                return gamePlay(newArr, node.left, depth + 1, last_selected)
            elif side == 'right':
                return gamePlay(newArr, node.right, depth + 1, last_selected)
    # AI's turn
    if depth % 2 == 1:
        if first > prev and node.left is not None and node.left.key == -1:
            return gamePlay(arr[1:], node.left, depth+1, first)
        elif last > prev and node.right is not None and node.right.key == -1:
            return gamePlay(arr[:-1], node.right, depth+1, last)
        else:
            if first > prev and node.left is not None:
                return gamePlay(arr[1:], node.left, depth+1, first)
            elif last > prev and node.right is not None:
                return gamePlay(arr[:-1], node.right, depth+1, last)
            else:
                return 1


     
def selectOption(arr, last_selected, side='x'):
    new_arr = []
    new_selected = 0
    side = 'x'
    print("option selection arr ", arr)
    print("last selected number ", last_selected)
    selectFormLeftOrRight = input('select a number from left or right: ')
    if selectFormLeftOrRight == 'l':
        if arr[0] > last_selected:
            new_arr = arr[1:]
            new_selected = arr[0]
            side = 'left'
        else:
            print('invalid selection')
            return selectOption(arr, last_selected)
    elif selectFormLeftOrRight == 'r':
        if arr[-1] > last_selected:
            new_arr = arr[:-1]
            new_selected = arr[-1]
            side = 'right'
        else:
            print('invalid selection')
            return selectOption(arr, last_selected)
    else:
        print('invalid selection')
        return selectOption(arr, last_selected)
    return new_arr, new_selected, side

left = []
middle = []
right = []

left = random.sample(range(1, 12), 3)
left.sort()

middle = random.sample(range(10, 25), 5)

right = random.sample(range(8, 20), 4)
right.sort(reverse=True)

arr = []
arr.extend(left)
arr.extend(middle)
arr.extend(right)


# ncount = random.randint(5, 12)
# arr = random.sample(range(1, ncount+1), ncount)
# print("ncount arr[]", ncount, arr)

print(arr)

arr = [1,2,3,6,5,4]

gt = gameTree(arr, 0)
ans = minimax(arr, gt)
play = gamePlay(arr, gt)
print("play ", play)
if(play == 1):
    print("You win")
else:
    print("AI win")

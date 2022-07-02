from ast import Not
from itertools import count
import random
from time import time
from turtle import right


class Node:
    def __init__(self, key=None, left=None, right=None, arr=None):
        self.game = arr
        self.key = key
        self.left = left
        self.right = right


def tree(arr, depth=0, nodeid=1):
    if not arr:
        return None
    newNode = Node()
    newNode.left = tree(arr[1:], depth+1, nodeid*2)
    newNode.right = tree(arr[:-1], depth+1, nodeid*2+1)
    if(newNode.left is None and newNode.right is None):
        newNode.key = arr[0]
    return newNode


def gameTree(arr, prev=0, depth=0, nodeid=1):
    if not arr:
        return None
    first, last = arr[0], arr[-1]
    newNode = Node()
    newNode.game = arr
    if first > prev:
        newNode.left = gameTree(arr[1:], first, depth+1, nodeid*2)
    if last > prev:
        newNode.right = gameTree(arr[:-1], last, depth+1, nodeid*2+1)
    if newNode.left is None and newNode.right is None:
        if depth % 2 == 0:
            newNode.key = -1
        else:
            newNode.key = 1

    # print("current gameTree : ", arr, newNode.key)
    return newNode


def selectOption(arr, last_selected, side='x'):
    # print("you have to select a number with 15 seconds")
    # countdown(15)
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


def minimax(arr, node, depth=0, nodeid=1, prev=0):

    if len(arr) == 1:
        return node.key

    first, last = arr[0], arr[-1]

    # max player
    if depth % 2 == 0:
        x = -1
        y = -1
        if first > prev and node.left is not None:
            res = 1
            if(len(arr) > 1):
                res = minimax(arr[1:], node.left, depth+1, nodeid*2, first)
            x = max(x, res)
            
            
        if last > prev and node.right is not None:
            res = 1
            if(len(arr) > 1):
                res = minimax(arr[:-1], node.right, depth+1, nodeid*2+1, last)
            y = max(y, res)
        node.key = max(x, y)

        # print("max : ", arr, node.key, nodeid)
        return node.key

    if depth % 2 == 1:
        # AI's turn
        x = 1
        y = 1
        if first > prev and node.left is not None:
            res = -1
            if(len(arr) > 1):
                res = minimax(arr[1:], node.left, depth+1, nodeid*2, first)
            x = min(x, res)

        if last > prev and node.right is not None:
            res = -1
            if(len(arr) > 1):
                res = minimax(arr[:-1], node.right, depth+1, nodeid*2+1, last)
            y = min(y, res)
            
        node.key = min(x, y)
        # print("min : ", arr, node.key, nodeid)
        return node.key


import time
def countdown(t):
    while t >= 0:
        mins, secs = divmod(t, 60)
        timer = ' ' + '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='')
        time.sleep(1)
        t -= 1

def gamePlay(arr, node, depth=0, prev=0):
    if len(arr) == 1:
        return node.key
    print("\n\n")
    first, last = arr[0], arr[-1]
    # player 1's turn
    if depth % 2 == 0:
        # print("prev first last ", prev, first, last)
        if prev >= first and prev >= last:
            return -1
            print("You lost!")
            exit(0)
        newArr, last_selected, side = selectOption(arr, prev)
        if len(arr):
            if side == 'left':
                return gamePlay(newArr, node.left, depth + 1, last_selected)
            elif side == 'right':
                return gamePlay(newArr, node.right, depth + 1, last_selected)
    # AI's turn
    if depth % 2 == 1:
        x = 1
        y = 1
        # print("AI's turn , prev, first, last arr[]", prev, first, last, arr)
        if first > prev and node.left is not None:
            if len(arr) > 1:
                x = min(x, node.left.key)
        if last > prev and node.right is not None:
            if len(arr) > 1:
                y = min(y, node.right.key)
        # print("value x, y ", x,y)
        if x == -1:
            # print("ai select value ", arr[0])
            return gamePlay(arr[1:], node.left, depth+1, first)
        elif y == -1:
            # print("ai select value ", arr[-1])
            return gamePlay(arr[:-1], node.right, depth+1, last)
        else:
            if first > prev and node.left is not None:
                # print("ai select value ", arr[0])
                return gamePlay(arr[1:], node.left, depth+1, first)
            elif last > prev and node.right is not None:
                # print("ai select value ", arr[-1])
                return gamePlay(arr[:-1], node.right, depth+1, last)
            else:
                return 1
                print("AI is LOST!")
                exit(0)


     
# arr = list(map(int, input().split()))
# arr = [5, 8, 1, 10, 9]
# arr = [5, 7, 10 ,6]

# arr = [3, 16, 6, 14, 19]


# def printTree(node):
# 	if node.key is not None:
# 		print(node.key, end=" ")
# 	if node.left is not None:
# 		printTree(node.left)
# 	if node.right is not None:
# 		printTree(node.right)

# x = tree(arr,0,1)
# printTree(x)

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

# arr = [1,2,3,6,5,4]

gt = gameTree(arr, 0)
ans = minimax(arr, gt)
play = gamePlay(arr, gt)
print("play ", play)
if(play == 1):
    print("You win")
else:
    print("AI win")

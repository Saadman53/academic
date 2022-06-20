n = int(input())
arr = list(map(int, input().split()))



# arr = [5, 8, 1, 10, 9]
# arr = [5,4,5]


class Node:

    def __init__(
        self,
        key=None,
        left=None,
        right=None,
        arr=None,
        ):
        self.game = arr
        self.key = key
        self.left = left
        self.right = right


def tree(arr, depth=0, nodeid=1):
	if not arr:
		return None
	# print(len(arr), "id = ", nodeid)
	newNode = Node()
	newNode.left = tree(arr[1:], depth+1, nodeid*2+1)
	newNode.right = tree(arr[:-1], depth+1, nodeid*2+2)

	if(newNode.left is None and newNode.right is None):
		newNode.key = arr[0]
	return newNode


# make -1, +1 game tree
# then apply minimax algorithm
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
		if depth%2 == 0:
			newNode.key = -1
		else:
			newNode.key = 1

	# aa=0
	# aaa=0
	# if newNode.left is not None:
	# 	aa = 1
	# if newNode.right is not None:
	# 	aaa = 1
	# print("node ", node, arr, "nodeid = ", nodeid, "key = ", aa, aaa, newNode.key, prev)
	return newNode


def minimax(arr, node, depth=0, nodeid=1, prev=0):
	# if(node is None):
	# 	print("node ", node, "nodeid = ", nodeid, "depth = ", depth)
	if node.left is None and node.right is None:
		return node.key

	first, last = arr[0], arr[-1]

	# max player
	if depth%2 == 0:
		x=-1
		y=-1
		if first > prev and node.left is not None:
			x = minimax(arr[1:], node.left, depth+1, nodeid*2, first)
		if last > prev and node.right is not None:
			y = minimax(arr[:-1], node.right, depth+1, nodeid*2+1, last)
		node.key = max(x, y)
		return node.key
	if depth%2 == 1:
		x=1
		y=1
		if first > prev and node.left is not None:
			x = minimax(arr[1:], node.left, depth+1, nodeid*2, first)
		if last > prev and node.right is not None:
			y = minimax(arr[:-1], node.right, depth+1, nodeid*2+1, last)
		node.key = min(x, y)
		return node.key

# def printGameTree(node,nodeid=1):
# 	if node.key is not None:
# 		print(nodeid, node.key, node.game)
# 	if node.left is not None:
# 		printGameTree(node.left,nodeid*2)
# 	if node.right is not None:
# 		printGameTree(node.right,nodeid*2+1)

# gt = gameTree(arr)
# printGameTree(gt)
# print("\n\n\n")
# ans = minimax(arr,gt)
# printGameTree(gt)
# print(ans)
# if ans == 1 or n==1:
# 	print("Alice")
# else:
# 	print("Bob")

# def printTree(node):
# 	if node.key is not None:
# 		print(node.key, end=" ")
# 	if node.left is not None:
# 		printTree(node.left)
# 	if node.right is not None:
# 		printTree(node.right)

# x = tree(arr,0,1)
# printTree(x)


def selectOption(arr, last_selected):

	new_arr=[]
	new_selected=0

	selectFormLeftOrRight = input('select a number from left or right: ')
	if selectFormLeftOrRight == 'l':
		if arr[0] > last_selected:
			new_arr = arr[1:]
			new_selected = arr[0]
		else:
			print('invalid selection')
	
	elif selectFormLeftOrRight == 'r':
		if arr[-1] > last_selected:
			new_arr = arr[:-1]
			new_selected = arr[-1]

	
	return new_arr, new_selected


last_selected = 0
while(1):
	print(arr)
	left = arr[0]
	right = arr[-1]

	if left < last_selected and right < last_selected:
		print("Oops! You lost!")
		print("Winner is AI")
		break
	else:
		newArr, last_selected = selectOption(arr,last_selected)


	gt = gameTree(newArr, last_selected)
	ans = minimax(newArr, gt)
	if ans == 1:
		# AI have to select is option optimally
		print("AI selects: ", newArr)

		if newArr[0] > last_selected:
			if gt.left is not None and gt.left.key == 1:
				arr = newArr[1:]
				last_selected = newArr[0]

		elif newArr[-1] > last_selected:
			if gt.right is not None and gt.right.key == 1:
				arr = newArr[:-1]
				last_selected = newArr[-1]
		
	else:
		if newArr[0] > last_selected:
			arr = newArr[1:]
			last_selected = newArr[0]
		elif newArr[-1] > last_selected:
			arr = newArr[:-1]
			last_selected = newArr[-1]
		else:
			print("AI is lost")
			break

	
	print("last selected: ", last_selected)

    
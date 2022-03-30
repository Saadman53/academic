import math

point_list = [(5,4),(2,6),(13,3),(8,7),(3,1),(10,2)]

while True:
  p,q,k = map(int,input().split())
  
  arr = []
  for i in point_list:
    dis = math.sqrt(abs(p-i[0])**2 + abs(q-i[1])**2)
    arr.append((dis,i))

  arr = sorted(arr)
  for i in range(k):
    print(format(arr[i][0], ".2f") , arr[i][1])

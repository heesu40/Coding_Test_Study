n = input("값:")
m = input()
print(n,m)
start = input()
import heapq
import sys
INF = int(1e9)
n,m,start = int(n),int(m),int(start)
print(type(n),type(m),type(start))
graph = [[] for i in range(n+1)]
print(graph)
distance = [INF] * (n+1)
print(distance)

# 개선된 다익스트라 알고리즘 
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

#노드의 개수, 간선의 개수 입력 받기
n, m = map(int, input().split())

#시작 노드 번호 입려 받기
start = int(input())
graph = [[] for i in range(n+1)]
print(graph) # [[], [], [], [], [], [], []]
distance = [INF] * (n+1) # [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

# [[], [(2, 2), (3, 5), (4, 1)], [(3, 3), (4, 2)], [(2, 3), (6, 5)], [(3, 3), (5, 1)], [(3, 1), (6, 2)], []]

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: 
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
    for i in graph[now]:
        cost = dist + i[1]
dijkstra(start)
for i in range(1, n+1):
    if distance[i] == INF:
         print("INFINITY")
    else :
        print(distance[i])
        
               
        
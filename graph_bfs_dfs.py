from collections import deque
class Graph :
    def __init__(self,num_nodes,edges):
        self.num_nodes=num_nodes
        self.adj_dict={}
        for n1,n2 in edges:
            if n1 not in self.adj_dict:
                self.adj_dict[n1]=[]
            if n2 not in self.adj_dict:
                self.adj_dict[n2]=[]
            self.adj_dict[n1].append(n2)
            self.adj_dict[n2].append(n1)
    def BFS(self,start_vertex):
        queue=deque()
        visited=set()
        queue.append(start_vertex)
        visited.add(start_vertex)
        while queue:
            present=queue.popleft()
            print(present)
            for adj_vertex in self.adj_dict[present]:
                 if adj_vertex not in visited:
                    queue.append(adj_vertex)
                    visited.add(adj_vertex)
    def DFS(self,start_vertex):
        stack=[]
        visited=set()
        stack.append(start_vertex)
        while stack:
            vertex=stack.pop()
            if vertex not in visited:
               visited.add(vertex)
               print(vertex)
            for adj in self.adj_dict[vertex]:
                if adj not in visited:
                    stack.append(adj)
num_nodes = 5
edges = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]
graph=Graph(num_nodes,edges)
print(graph.adj_dict)
print("==================================bfs===================================")
graph.BFS(3)
print("==================================dfs===================================")
graph.DFS(3)

class Graph:


    def __init__(self):   
        self.adj = {}

    def addEdge(self, v, w):   #add the vertices
        if v not in self.adj:
            self.adj[v] = []
        self.adj[v].append(w)

    def DFS(self, start, goal):
        stack = [start]
        visited = set()
        order = []

        while len(stack) > 0:
            v = stack.pop()  #pop the vertice and check if its visted or not 

            if v in visited:   #if visited so add in the list
                continue

            visited.add(v)
            order.append(v)
            print("Visiting:", v)

            if v == goal:     #here check for visted vetice -> goal or not
                print("Goal node", goal, "found!")
                print("DFS order:", " -> ".join(order))
                return True

            neighbours = self.adj.get(v, [])

            for w in reversed(neighbours):   #reverse the stack for the correct order
                if w not in visited:
                    stack.append(w)

        print("Goal node", goal, "not found.")
        print("DFS order:", " -> ".join(order))
        return False

g = Graph()

g.addEdge('A', 'B')
g.addEdge('A', 'F')
g.addEdge('A', 'D')
g.addEdge('A', 'E')

g.addEdge('B', 'K')
g.addEdge('B', 'J')

g.addEdge('K', 'N')
g.addEdge('K', 'M')

g.addEdge('D', 'G')

g.addEdge('E', 'C')
g.addEdge('E', 'H')
g.addEdge('E', 'I')

g.addEdge('I', 'L')

print("Depth First Search using Stack (Start = A, Goal = G)")
g.DFS('A', 'G')  #G is the goal to find
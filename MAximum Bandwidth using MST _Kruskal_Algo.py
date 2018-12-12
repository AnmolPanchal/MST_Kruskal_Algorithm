
# coding: utf-8

# In[10]:


import collections
from collections import defaultdict 
  
class Graph: 
  
    def __init__(self,vertices): 
        self.V= vertices #No. of vertices 
        self.graph = [] # default dictionary to store graph 
          
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w]) 
  
    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 

    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 
      
        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot 
  
        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1
  
    
    def KruskalMST(self): 
  
        result =[] 
  
        i = 0 # index variable,for sorted edges 
        e = 0 # index variable,for result[] 
  
        self.graph =  sorted(self.graph,key=lambda item: item[2]) 
  
        parent = [] ; rank = [] 
  
        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 
      
        # Number of edges to be taken is equal to V-1 
        while e < self.V -1 : 
  
            u,v,w =  self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent ,v) 
            if x != y: 
                e = e + 1     
                result.append([u,v,w]) 
                self.union(parent, rank, x, y)             
            
  
        # printing the contents of result[] to display the built MST 
        print( "Following are the edges in the constructed MST")
        for u,v,weight  in result: 
            #print str(u) + " -- " + str(v) + " == " + str(weight) 
            print ("%d -- %d == %d" % (u,v,weight)) 
#You can add edges based on bandwitdh values and it will show the MST with least to max bandwidths and the result.


# In[22]:


g = Graph(4) 
g.addEdge(0, 2, 30) 
g.addEdge(0, 3, 60) 
g.addEdge(2, 1, 90) 
g.addEdge(3, 1, 50) 
g.addEdge(3, 2, 70) 
  
g.KruskalMST() 



class Tree():
    def __init__(self,root):
        #Each node contains some data, then parent,
        #then indexes of children
        self.nodes = [[root,None]]

    def __printNode(self,node,ind):
        ret = "  " * ind + str(self.nodes[node][0]) + "\n"
        ch = self.nodeChildren(node)
        for c in ch:
            ret += self.__printNode(c,ind + 1)
        return ret
            
    def __str__(self):
        return self.__printNode(0,0)
        
    def addNode(self,parent,val):
        p = self.nodes[parent]
        self.nodes.append([val,parent])
        p.append(len(self.nodes) - 1)
        return len(self.nodes)-1
    
    def pathToNode(self,node):
        l = []
        while not self.nodes[node][1] is None:
            l.append(node)
            node = self.nodes[node][1]
        l.append(0)
        l.reverse()
        return l

    def nodeChildren(self,node):
        if len(self.nodes[node]) >= 3:
            return self.nodes[node][2:]
        return []

    def nodeParent(self,node):
        return self.nodes[node][1]

    def leaves(self):
        l = []
        for i in range(len(self.nodes)):
            n = self.nodes[i]
            if len(n) == 2:
                l.append(i)
        return l

    def getData(self,node):
        return self.nodes[node][0]
    

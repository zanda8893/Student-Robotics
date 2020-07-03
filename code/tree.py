
class Tree():
    def __init__(self,root):
        #Each node contains some data, then parent,
        #then indexes of children
        self.nodes = [[root,None]]

    def addNode(parent,val):
        p = self.nodes[parent]
        self.nodes.append([val,parent])
        p.append(self.nodes.length() - 1)
        return self.nodes.length()-1
    
    def pathToNode(node):
        l = []
        while not self.nodes[node][1] is None:
            l.append(node)
            node = self.nodes[node][1]
        l.reverse()
        return l

    def nodeChildren(node):
        if self.nodes[node].length() >= 3:
            return self.nodes[node][2:]
        return []

    def nodeParent(node):
        return self.nodes[node][1]

    def leaves():
        l = []
        for i in range(self.nodes.length()):
            n = self.nodes[i]
            if n.length() == 2:
                l.append(i)
            else:
                l.insert(self.leaves(i))
        return l

    def getData(node):
        return self.nodes[node][0]
    

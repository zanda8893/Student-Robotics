
class Tree():
    def __init__(self,root):
        #Each node contains some data, then parent,
        #then indexes of children
        self.nodes = [[root,None]]

    def addNode(parent,val):
        p = self.nodes[parent]
        self.nodes.append([val,parent])
        p.append(self.nodes.length() - 1)
    
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

    

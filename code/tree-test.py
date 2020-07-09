from tree import Tree

#Tree tests complete

t = Tree(3)
print(t)
a = t.addNode(0,4)
b = t.addNode(0,5)
c = t.addNode(a,6)
d = t.addNode(a,7)
e = t.addNode(d,8)
print(t)
print("Path to e:")
p = t.pathToNode(e)
for i in p:
    print("\t",t.getData(i))
print("Path to c")
p = t.pathToNode(c)
for i in p:
    print("\t",t.getData(i))
print("Leaves:")

l = t.leaves()
for i in l:
    print(t.getData(i))

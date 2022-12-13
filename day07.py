class Node (object):
    def __init__(self, name, parent=None):
        self.files = []
        self.dirs = {}
        self.parent = parent
        self.root = parent.root if parent else self
        self.name = name

    def fullname(self):
        n = self
        names = []
        while True:
            if n.parent:
                names.append(n.name)
                n = n.parent
            else:
                break
        return "/".join(names[::-1])

    def add (self, item):
        if item[:3] == "dir":
            self.dirs[item[4:]] = Node(item[4:], self)
            # print ("added {} parent is {}".format(item[4:], self.name))
        elif item:
            self.files.append(tuple(item.split(" ")))
            # print ("added file {} to dir {}".format(self.files[-1][1], self.name))

    def cd (self, items):
        if items[0] == "..":
            return self.parent
        elif items[0] == "/":
            return self.root if self.root else self
        else:
            return self.dirs[items[0]]

    def print (self, indent=0):
        print ("  "*indent, self.name, "(dir, size={})".format(self.size()))
        for d in self.dirs.values():
            d.print(indent+1)
        for f in self.files:
            print ("  "*(indent+1), f[1], f[0])

    def size(self):
        return sum(d.size() for d in self.dirs.values()) + sum(int(f[0]) for f in self.files)

    def fetch_dirs (self):
        queue = [self]
        dirs = {}
        while queue:
            n = queue.pop()
            dirs[n.fullname()] = n.size()
            queue += [d for d in n.dirs.values()]
        return dirs



with open ("day07.txt", "r") as f:
    data = [l.split("\n") for l in f.read().split("$ cd ")][1:]

node = Node("/")
for d in data:
    node = node.cd(d)
    for item in d[2:]:
        node.add(item)

node = node.root
node.print()

l = node.fetch_dirs()
print (sum(f for f in l.values() if f <= 100000))

system_size = l[""]
disk_size = 70000000
needed_space = 30000000
current_space = disk_size - system_size
space_to_free = needed_space - current_space
print(min([v for v in l.values() if v >= space_to_free]))

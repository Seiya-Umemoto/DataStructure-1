class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def set_left(self, left):
        self.left = left
    
    def set_right(self, right):
        self.right = right

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_key(self):
        return self.key

class Binary_search_tree:
    def __init__(self):
        self.root = None

    def set_root(self, root):
        self.root = root

    def search(self, key):
        return self.check(self.root, key)

    def check(self, node, key):
        if node is None:
            return None

        if node.get_key() == key:
            return node
        elif node.get_key() < key:
            return self.check(node.get_right(), key)
        else:
            return self.check(node.get_left(), key)
            
node_40 = Node(40)
node_15 = Node(15)
node_69 = Node(69)
node_8 = Node(8)
node_25 = Node(25)
node_54 = Node(54)
node_86 = Node(86)
node_5 = Node(5)
node_10 = Node(10)
node_20 = Node(20)
node_30 = Node(30)
node_50 = Node(50)
node_66 = Node(66)
node_83 = Node(83)
node_90 = Node(90)

bts = Binary_search_tree()
bts.set_root(node_40)

node_40.set_left(node_15)
node_40.set_right(node_69)

node_15.set_left(node_8)
node_15.set_right(node_25)

node_69.set_left(node_54)
node_69.set_right(node_86)

node_8.set_left(node_5)
node_8.set_right(node_10)

node_25.set_left(node_20)
node_25.set_right(node_30)

node_54.set_left(node_50)
node_54.set_right(node_66)

node_86.set_left(node_83)
node_86.set_right(node_90)

result = bts.search(66)
if result is None:
    print("fail")
else:
    print("success")



class Node:
    def __init__(self, name):
        self.left = None
        self.right = None
        self.name = name

    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right
    
    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right
    
    def get_name(self):
        return self.name
    

class BST:
    def __init__(self):
        self.root = None

    def add(self, new):
        self.__add(self.root, new)

    def __add(self, current, new):
        if self.root == None:
            self.root = new
            return
        if new.name > current.name and current.right == None:
            current.right = new
            return
        
        if new.name > current.name and current.right != None:
            self.__add(current.right, new)
            return

        if new.name < current.name and current.left == None:
            current.left = new
            return

        if new.name < current.name and current.left != None:
            self.__add(current.left, new)
            return

    def get(self, name):
        return self.__get(self.root, name)

    def __get(self, current, name):
        if current == None:
            return None
        
        if current.name == name:
            return current
        
        if name > current.name:
            return self.__get(current.right, name)
        
        if name < current.name:
            return self.__get(current.left, name)
        
    def remove(self, old):
        self.__remove(self.root, old)

    def __remove(self, current, old):
        if self.root == None:
            return
        
        if self.root != None and old.name == self.root.name:
            self.root = None
            return

        if old.name > current.name and current.right == None:
            return
        
        if old.name > current.name and current.right != None and old.name == current.right.name:
            current.right = None
            self.__reinsert_children(old)
            return
        
        if old.name > current.name and current.right != None and old.name != current.right.name:
            self.__remove(current.right, old)
            return

        if old.name < current.name and current.left == None:
            return

        if old.name < current.name and current.left != None and old.name == current.left.name:
            current.left = None
            self.__reinsert_children(old)
            return
        
        if old.name < current.name and current.left != None and old.name != current.left.name:
            self.__remove(current.left, old)
            return
    
    # be sure to remove parent from tree before calling this one
    def __reinsert_children(self, parent):
        left = parent.left
        right = parent.right

        if parent.right != None:
            parent.right = None
            self.add(right)
        
        if parent.left != None:
            parent.left = None
            self.add(left)

memories = BST()
memories.add(Node("First memory"))
memories.add(Node("Second memory"))
memories.add(Node("Third memory"))
memories.add(Node("Fourth memory"))
memories.add(Node("Fifth memory"))
memories.add(Node("Sixth memory"))
memories.add(Node("Seventh memory"))
memories.add(Node("Eight memory"))
memories.add(Node("Ninth memory"))
memories.add(Node("Tenth memory"))

memory = memories.get("Sixth memory")
memories.remove(memory)

print(memories.get("Fifth memory"))
print(memories.get("Sixth memory"))
print(memories.get("Seventh memory"))



            











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


print(memories.get("Sixth memory").get_name())



            










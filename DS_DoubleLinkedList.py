class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


    def print_list(self):
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next


    def append(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head, self.tail = new_node, new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1
        return True
    

    def pop(self):
        if self.length == 0:
            return None

        temp = self.tail
        if self.length == 1:
            self.tail, self.head = None, None
        
        else:
            self.tail = temp.prev
            self.tail.next = None
            temp.prev = None

        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head, self.tail == new_node, new_node

        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True

    
    def pop_first(self):
        if self.length == 0:
            return None

        temp = self.head

        if self.length == 1:
            self.head, self.tail = None, None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None

        self.length -= 1
        return temp

    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        if index < self.length / 2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev

        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    

    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length - 1:
            return self.append(value)

        new_node = Node(value)
        temp = self.get(index)
        pre = temp.prev
        new_node.prev = pre
        new_node.next = temp
        pre.next = new_node
        temp.prev = new_node

        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
           return self.pop_first()
        if index == self.length - 1:
           return self.pop()
        
        temp = self.get(index)
        before = temp.prev
        after = temp.next
        before.next = after
        after.pre = before
        temp.next, temp.prev = None, None
        self.length -= 1

        return temp



if __name__ == '__main__':
    DLL = DoubleLinkedList(0)
    DLL.prepend(1)
    DLL.append(5)
    DLL.append(6)
    print(DLL.remove(3).value)
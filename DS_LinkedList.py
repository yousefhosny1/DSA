class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
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
        # CASE 1: Linked List is Empty
        if self.head is None:  
            self.head, self.tail = new_node, new_node
        # CASE 2: Linked List not Empty
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def pop(self):
        if self.length == 0:
            return None

        temp = self.head
        pre = self.head

        while temp.next is not None:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
            
    def pop_first(self):
        if self.length == 0:
            return None

        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None
        return temp
    
    def get(self, index):
        if index >= 0 and index < self.length:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp
        else:
            return None

    def set_value(self, index, value):
        temp = self.get(index)

        if temp is not None:
            temp.value = value
            return True
        return False
        
    def insert(self, index, value):
        new_node = Node(value)

        if index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append(value)

        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1

        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.pop_first

        if index == self.length - 1:
            return self.pop

        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1

        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        pre = None
        after = temp.next

        for _ in range(self.length):
            after = temp.next
            temp.next = pre
            pre = temp
            temp = after
        return self
        



if __name__ == '__main__':
    LL = LinkedList(4)
    LL.append(1)
    LL.append(3)
    LL.append(0)
    LL.set_value(0, 5)
    LL.insert(1, 5)
    LL.print_list()
    print("\n", LL.remove(2), "\n")
    LL.print_list()
    print()
    LL_reversed = LL.reverse()
    LL_reversed.print_list()
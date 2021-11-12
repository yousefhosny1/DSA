class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1


    def print_list(self):
        temp = self.first

        while temp is not None:
            print(temp.value)
            temp = temp.next


    def enqueue(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.first, self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

        self.length += 1


    def dequeue(self):
        if self.length == 0:
            return None
        
        temp = self.first
        if self.length == 1:
            self.first, self.last = None, None
        else:
            self.first = self.first.next
            temp.next = None

        self.length -= 1
        return temp



if __name__ == '__main__':
    q = Queue(5)
    q.enqueue(8)
    q.enqueue(6)
    q.enqueue(7)
    q.dequeue()
    q.print_list()
        
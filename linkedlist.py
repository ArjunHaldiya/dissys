class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__ (self):
        self.head = None
        self.tail = None

    def push_front(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        if self.tail is None:
            self.tail = newNode

    def push_back(self, value):
        newNode = Node(value)
        if self.tail is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def find (self, value):
        curr = self.head
        while curr is not None:
            if curr.value == value:
                return True
            curr = curr.next
        return False

    def delete (self, value):
        prev = None
        curr = self.head
        while curr is not None:
            if curr.value == value:
                if prev is None:
                    self.head = curr.next
                else:
                    prev.next = curr.next

                if curr is self.tail:
                    self.tail = prev
                return    
                
            prev = curr
            curr = curr.next


    def reverse(self):
        prev = None
        curr = self.head

        self.tail = self.head

        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def pop_front(self):
        if self.head is None:
            raise IndexError("Cannot pop from an empty list")
        node = self.head
        self.head = node.next
        if self.head is None:
            self.tail = None
        return node.value
    

    def peek_head(self):
        if self.head is None:
            raise IndexError("Nothing to Peek")
        return self.head.value

    def is_empty_list(self):
        if self.head is None:
            return True
        return False
    
    def to_list(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.value)
            curr = curr.next

        return result
    
class Stack:
    def __init__ (self):
        self.items = LinkedList()

    def push(self, value):
        self.items.push_front(value)

    def pop(self):
        return self.items.pop_front()

    def peek(self):
        return self.items.peek_head()

    def is_empty(self):
        return self.items.is_empty_list()

class Queue:
    def __init__ (self):
        self.items = LinkedList()

    def enqueue(self, value):
        self.items.push_back(value)

    def dequeue(self):
        return self.items.pop_front()

    def peek(self):
        return self.items.peek_head()

    def is_empty(self):        
        return self.items.is_empty_list()

l = LinkedList()
l.push_front(1); l.push_front(2); l.push_front(3)
print(l.to_list())
l.reverse()
print(l.to_list())
l.find(2)
l.delete(2)
print(l.to_list())



q = Queue()
q.enqueue(1); q.enqueue(2); q.enqueue(3)
print(q.dequeue())  
print(q.peek())
print(q.is_empty())

s = Stack()
s.push(1); s.push(2); s.push(3)
print(s.pop())       
print(s.peek())      
print(s.is_empty()) 
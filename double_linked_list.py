"""
-push head
-push tail
-pop head
-pop tail
-size
"""

class Node(object):
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def set_prev(self, node=None):
        self.prev = node
    
    def set_next(self, node=None):
        self.next=node

class DLL(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def push_tail(self, val):
        n = Node(val=val, prev=self.tail)
        if self.tail is not None:
            self.tail.set_next = n
        self.tail = n
        self.size += 1

    def pop_tail(self):
        if self.tail is None:
            raise ValueError
        res = self.tail.val
        self.tail = self.tail.prev
        self.size -= 1
        if self.tail is not None:
            self.tail.set_next = None
        return res

    def pop_head(self):
        if self.head is None:
            raise ValueError
        res = self.head.val
        self.head = self.head.next
        self.size -= 1
        if self.head is not None:
            self.head.set_prev = None
        return res
    
    def push_head(self, val):
        n = Node(val=val, next=self.head)
        if self.head is not None:
            self.head.set_prev = n
        self.head = n
        self.size += 1

    
    

if __name__ == '__main__':
    d = DLL()
    assert d.size == 0
    val1 = "first"
    val2 = "second"
    d.push_tail(val1)
    assert d.size == 1
    d.push_tail(val2)
    assert d.size == 2
    assert d.pop_tail() is val2
    assert d.size == 1
    assert d.pop_tail() is val1
    assert d.size == 0

    d.push_head(val1)
    assert d.size == 1
    d.push_head(val2)
    assert d.size == 2
    assert d.pop_head() is val2
    assert d.size == 1
    assert d.pop_head() is val1
    assert d.size == 0
    print('ok')
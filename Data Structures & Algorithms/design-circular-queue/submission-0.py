class ListNode:
    def __init__(self, val= None, next = None):
        self.value = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.k = k
        self.head = ListNode()
        curr = self.head
        prev = None
        for i in range(k-1):
            curr.next = ListNode()
            prev = curr
            curr = curr.next
            prev.next = curr
        curr.next = self.head
        self.front, self.rear = self.head, self.head
        

    def enQueue(self, value: int) -> bool:
        if not self.capacity:
            return False
        if self.capacity == self.k:
            self.capacity -= 1
            self.front.value = value
            return True

        self.rear= self.rear.next
        self.rear.value = value
        self.capacity -= 1
        return True
        

    def deQueue(self) -> bool:
        if self.capacity == self.k:
            return False
        self.capacity += 1
        self.front.value = None
        self.front = self.front.next
        if self.capacity == self.k:
            self.front, self.rear = self.head, self.head
        return True
            
        

    def Front(self) -> int:
        if self.capacity == self.k:
            return -1
        return self.front.value

        

    def Rear(self) -> int:
        if self.capacity == self.k:
            return -1
        return self.rear.value

    def isEmpty(self) -> bool:
        return self.capacity == self.k
        

    def isFull(self) -> bool:
        return not self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
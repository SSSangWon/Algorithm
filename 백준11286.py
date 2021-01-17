import sys
r = sys.stdin.readline

class AbsHeap(object):
    def __init__(self):
        self.arr = []

    def swap(self, index1, index2):
        self.arr[index1], self.arr[index2] = self.arr[index2], self.arr[index1]

    def parent(self, index):
        return (index-1) // 2 

    def left_child(self, index):
        return index*2 + 1

    def right_child(self, index):
        return index*2 + 2

    def printHeap(self):
        print(self.arr)
    
    def heapPush(self, item):
        self.arr.append(item)
        i = len(self.arr) -1

        while i > 0:
            p = self.parent(i)

            if 0 <= p: 
                if abs(self.arr[i]) < abs(self.arr[p]):
                    self.swap(i, p)
                    i = p
                elif abs(self.arr[i]) == abs(self.arr[p]) and self.arr[i] < self.arr[p]:
                    self.swap(i, p)
                    i = p

                else:
                    break
            else:
                break
    
    def heapPop(self):
        i = len(self.arr) -1

        if i > 0:
            self.swap(0, i)
            value = self.arr.pop()
            self.heapify(0)
        elif i == 0:
            value = self.arr.pop()
        else:
            value = 0
        
        return value

    def heapify(self, i):
        left = self.left_child(i)
        right = self.right_child(i)
        index = i

        if left <= len(self.arr)-1 :
            if abs(self.arr[index]) > abs(self.arr[left]):
                index = left
            elif abs(self.arr[index]) == abs(self.arr[left]) and self.arr[index] > self.arr[left]:
                index = left
            
        if right <= len(self.arr)-1:
            if abs(self.arr[index]) > abs(self.arr[right]):
                index = right
            elif abs(self.arr[index]) == abs(self.arr[right]) and self.arr[index] > self.arr[right]:
                    index = right

        if index != i:
            self.swap(i, index)
            self.heapify(index)

N = int(r())
h = AbsHeap()

for i in range(N):
    n = int(r())

    if n == 0:
        print(h.heapPop())
    else:
        h.heapPush(n)

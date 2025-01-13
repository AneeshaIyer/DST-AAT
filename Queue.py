# Enter your code here. Read input from STDIN. Print output to STDOUT
class Queue:
    def __init__(self):
        self.s_in = []
        self.s_out = []

    def enqueue(self, x):
        self.s_in.append(x)
    def dequeue(self):
        if not self.s_out:
            while self.s_in:
                self.s_out.append(self.s_in.pop())
        if self.s_out:
            return self.s_out.pop()    
    def front(self):
        if not self.s_out:
            while self.s_in:
                self.s_out.append(self.s_in.pop())
        if self.s_out:
            return self.s_out[-1]

n = int(input()) 
q  = Queue()
for i in range(n):
    query = input().split()
    q1 = int(query[0])

    if q1 == 1:
        x = int(query[1])
        q.enqueue(x)
    elif q1 == 2:
        q.dequeue()
    elif q1 == 3:
        print(q.front())

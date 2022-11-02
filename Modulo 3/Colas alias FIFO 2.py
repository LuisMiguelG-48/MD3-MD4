class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.cola_list=[]

    def put(self, elem):
        self.cola_list.insert(0,elem)

    def get(self):
        if len(self.cola_list) > 0:
            elem = self.cola_list[-1]
            del self.cola_list[-1]
            return elem
        else:
            raise QueueError

class SuperQueue(Queue):
    def isempty(self):
        return len(self.cola_list)== 0

que = SuperQueue()
que.put(1)
que.put("perro")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Cola vacía")

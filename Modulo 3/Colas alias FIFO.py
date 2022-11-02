class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.__cola_list=[]

    def put(self, elem):
        self.__cola_list.insert(0,elem)

    def get(self):
        if len(self.__cola_list) > 0:
            elem = self.__cola_list[-1]
            del self.__cola_list[-1]
            return elem
        else:
            raise QueueError


que = Queue()
que.put(1)
que.put("perro")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Error de Cola")

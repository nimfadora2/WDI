class Node:
    def __init__(self,data):
        self.sur = data[0]
        self.points = data[1]
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.sur)+"\t"+str(self.points)

class BidirectionalList:
    def __init__(self):
        self.head = None
        self.end = None
        self.size = 0

    def add_begin(self,data):
        if self.head == None:
            n = Node(data)
            self.head = n
            self.end = n
            self.size+=1
        else:
            n=Node(data)
            n.next = self.head
            self.head.prev = n
            self.head = n
            self.size+=1

    def add_end(self,data):
        if self.head == None:
            n = Node(data)
            self.head = n
            self.end = n
            self.size+=1
        else:
            n = Node(data)
            n.prev = self.end
            self.end.next=n
            self.end = n
            self.size+=1

    def add_place(self,place,data):
        #place=place-1
        if place > self.size+1:
            print("To big number no such place!")
            return -1

        if place==1:
            self.add_begin(data)
        elif place == self.size+1:
            self.add_end(data)
        else:
            temp = self.head
            for i in range(place-1):
                temp = temp.next
            nowy = Node(data)
            prev = temp.prev
            nowy.prev = prev
            nowy.next = temp
            temp.prev = nowy
            prev.next = nowy
            self.size+=1

    def delete_begin(self):
        if self.size != 0:
            self.head = self.head.next
            self.head.prev = None
            self.size-=1

    def delete_end(self):
        if self.size != 0:
            self.end = self.end.prev
            self.end.next = None
            self.size-=1

    def printList_forward(self):
        n = self.head
        while n:
            print(n)
            n=n.next
        print()

    def printList_backward(self):
        n = self.end
        while n:
            print(n)
            n=n.prev
        print()

    def max(self):
        temp = self.head
        maximum = temp.points
        person = temp.sur
        while temp:
            if temp.points > maximum:
                maximum = temp.points
                person = temp.sur
            temp = temp.next


        print(str(person)+"\t" + str(maximum))


lista = BidirectionalList()
lista.add_begin(['Kinga',100])
lista.add_begin(['Piotr',90])
lista.add_begin(['Michal',80])
lista.add_end(['Ola',70])
lista.add_end(['Marta',87])
lista.add_place(1,['Przemek',50])
lista.add_place(6,['Karol',30])
lista.printList_forward()
lista.add_place(3,["Monika", 10000])
lista.printList_forward()
lista.printList_backward()


lista.printList_forward()
lista.delete_begin()
lista.printList_forward()
lista.delete_end()
lista.printList_forward()

lista.max()




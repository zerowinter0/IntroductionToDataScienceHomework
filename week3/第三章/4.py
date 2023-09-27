class node:
    def __init__(self,val):
        self.value=val
        self.next=None
class myList:
    head=None
    tail=None
    def __init__(self):
        self.head=None
        self.tail=None
    def add(self,x):##向链表尾部增加一个元素
        newNode=node(x)
        if(not self.head):
            self.head=newNode
            self.tail=self.head
        else:
            self.tail.next=newNode
            self.tail=newNode
    def search(self,x):##若链表中存在值x则将其删除
        now=self.head
        while(now!=None):
            if(now.value==x):
                return True
            now=now.next
        return False
    def delete(self,x):##删除链表中遇到的第一个x
        now=self.head
        last=None
        while(now!=None):
            if(now.value==x):
                if(now==self.tail):
                    self.tail=last
                if(last):
                    last.next=now.next
                else:self.head=now.next
                break
            last=now
            now=now.next
    def change(self,x,y):##将链表中所有的x改为y
        now=self.head
        last=None
        while(now!=None):
            if(now.value==x):
                now.value=y
            now=now.next
l=myList()
l.add(3)
l.add(2)
l.add(5)
l.add(5)
print(l.search(3))
l.delete(3)
print(l.search(3))

print(l.search(5))
print(l.search(7))
l.change(5,7)
print(l.search(5))
print(l.search(7))
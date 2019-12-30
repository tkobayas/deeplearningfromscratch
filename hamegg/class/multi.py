class A:
    def method(self):
        print("class A")

class B:
    def method(self):
        print("class B")

class C(A):
    def method(self):
        print("class C")

class D(B,C):
    pass

d = D()
d.method()

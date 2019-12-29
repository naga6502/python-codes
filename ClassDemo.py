class AddNum:
    msg = "Hello"

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.msg = "naga"

    def add(self):
        return self.a + self.b


a1 = AddNum(1, 5)

a2 = AddNum(5, 6)

#AddNum.msg = 'Bye'

print(a1.msg+" - a1 sum value =", a1.add())
print(a2.msg+" - a2 sum value =", a2.add())

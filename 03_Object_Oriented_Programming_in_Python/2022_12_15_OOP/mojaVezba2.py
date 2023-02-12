class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def intruduce_self(self):
        print(f'Hello, my name is {self.name}')


r1 = Robot('Tom', 'red', 30)
r2 = Robot('Jerry', 'blue', 40)

r1.intruduce_self()
r2.intruduce_self()
print(r1.color)
print(r2.weight)
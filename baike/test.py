class sy:
    # def __init__(self, name, password):
    #     self.password = password
    #     self.name = name;
    val11 = 'string 1'
    def __init__(self):
        self.val11 = 'var 22'
    @classmethod
    def sayHello(cls):
        print('lei:' + str(cls) + 'var11' + cls.val11)

sy.sayHello()
# p = sy()
# p.sayHello()

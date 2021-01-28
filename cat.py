from animal_oop import Animal


class Cat(Animal):

    def __init__(self):
        self.hair = "短毛"
        # 继承父类的方法
        super().__init__()

    def catch(self):
        print("会捉老鼠")

    def talk(self):
        print("喵喵叫")


if __name__ == '__main__':
    cat = Cat()
    print(cat.name)
    cat.talk()

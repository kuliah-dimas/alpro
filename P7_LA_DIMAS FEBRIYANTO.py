class Dog:
    def __init__(self, name, age, color):
        self.__name = name
        self.__age = age
        self.__color = color

    def getName(self):
        return self.__name;    




def main():
    dog = Dog("Dimas", 18, "blue")
    name = dog.getName()
    print(name)
    
main()


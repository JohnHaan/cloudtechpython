class Animal:
    def __init__(self, name):
        self.name = name
        #print('animal name=', self.name)
    def move(self):
        print(self.name, "move")
    def speak(self):
        pass
 
class Dog (Animal):
    def speak(self):
        print(self.name)
        print("bark")
 
class Duck (Animal):
    def speak(self):
        print("quack")
        
dog = Dog("bam")
print('name=', dog.name)  #부모 클래스 인스턴스 변수 사용
dog.move() #부모 클래스 메서드 사용
dog.speak() #자식 클래스 메서드 사용


animals = [Dog('doggy'), Duck('duck')]
for a in animals:
    a.speak()
    

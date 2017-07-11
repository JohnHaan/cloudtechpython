# 가장 흔히 쓰이는 인스턴스 메서드는 
# 인스턴스 변수에 엑세스할 수 있도록 
# 메서드의 첫번째 파라미터에 항상 객체 자신을 의미하는 "self"라는 파라미터를 갖는다. 
 
class Rectangle:
    count = 0  #클래스 변수
   
    #초기자(initializer)  #클래스로부터 새 객체를 생성할 때마다 실행되는 메서드  __init__() 
    def __init__(self, width, height):
        self.width = width
        self.height = height
        Rectangle.count = 0  #초기화 할때 사용
        Rectangle.count  += 1
    
    # 메서드
    def calcArea(self):
        area = self.width * self.height
        return area
        
    def calcPyung(self):
        pyung = self.width * self.height / 3.3
        return pyung
        
    def calcDevide(self):
        devide = self.width / self.height
        return devide

a = Rectangle(30,30)  #객체 생성  #a는 객체이다, a는 Rectangle의 인스턴스
print('class count=',a.count)
area = a.calcArea() #메서드 호출
print('area=', area)
print('area=', a.calcArea()) #메서드 호출&출력
print('pyung=',a.calcPyung())
print('devide=',a.calcDevide())
a.width = 10  #인스턴스 변수 액세스
print('width=', a.width)
print('area=', a.calcArea())
print('pyung=',a.calcPyung())
print('devide=',a.calcDevide())
print('class count=',a.count)
b = Rectangle(20,20)  #객체 생성
print('class count=',b.count)  #class 변수 변화 확인
c = Rectangle(10,10)
print('class count=',c.count)






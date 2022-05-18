# 파이썬 기본 문법
# 우리가 배운 내용 : 딕셔너리, Exception Handling, 클래스, 모듈, 패키지, 라이브러리

import random # random 모듈 (난수)


# 계산기 클래스
class Calculator:
    def __init__(self, num1, num2):  # 생성자
        self.num1 = num1 # 멤버변수 초기화
        self.num2 = num2 # 멤버변수임을 명시하기 위해선 변수명 앞에다 "self" 키워드를 붙여줄 것
    
    def plus(self):  # 더하기 메소드
        try:
            result = self.num1 + self.num2
            return result
        except: # 어떤 오류가 발생하든 아래코드실행
            print("더하기 연산을 진행하던 중에, Error가 발생!")  # 예외가 발생시 처리하는 구문
        else:  # try 블록에서 그 어떠한 예외도 발생하지 않았을떄 실행
            print("아무런 예외가 발생하지 않았을때 실행되는 블록입니다.")
        finally: #예외 O든X든 무조건 아래코드 실행
            print("예외 처리와 상관없이 반드시 무조건 실행되는 블록")
    
    def divide(self): # 나누기  메소드 
        try:
            return self.num1 / self.num2
        except ZeroDivisionError:
            print("0으로 나눌 수 없습니다!")
    
    def print_random(self):
        print("난수:", random.randint(1,10)) # ranom 모듈의 난수생성 기능을 활용


obj1 = Calculator(1,2)  # 계산기 객체
print(obj1.plus())  

'''
예외 처리와 상관없이 반드시 무조건 실행되는 블록
3
'''

obj2 = Calculator(4,0) # 계산기 객체
print(obj2.divide())

'''
0으로 나눌 수 없습니다!
None
'''
# 딕셔나리 : key-value 쌍을 저장하는 자료구조. 
my_dic = dict() # 계산기 객체를 저장하는 딕셔너리 생성
my_dic['first'] = obj1  # 딕셔너리에 계산기 객체들을 저장. 이때 key값은 first, second 이며, 그에 대한 value 값은 각 계산기 객체이다.
my_dic['second'] = obj2

print("===============================")
for element in my_dic.values():   # 딕셔너리에 담겨있는 value 들에 대해 실행. 즉, 각 계산기 객체들에 대해 실행
    print(element.print_random())      # 각 객체들에 대한 print_random 메소드를 호출

'''
===============================
난수:6
난수:4
'''
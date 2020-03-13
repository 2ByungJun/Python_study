# python 1시간만에 배우기
# Youtube 코딩하는 테크보이 워니

# python
  # print("Hello World")

# 변수
x = 1
y = 2
z = 1.2

# 사칙연산
print("1. 사칙연산")
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x ** y)
print(x % y) # mod
print("\n")

# 문자열
print("2. 문자열")
x = "hello"
y = 'bye'
# 따옴표 차이는 없다
z = """
안녕하세요
병준입니다
"""
print(x) # hello
print(y) # bye
print(z) # 안녕하세요 병준입니다
print("안녕" + "잘 지내니?")
print("\n")

# 캐스팅(casting) : print( 타입값을 맞춰주는 것 )
print("3. 캐스팅(Casting)")
print("너 혹시 몇 살이니? " + str(4)) 
x = 4   # 숫자 타입
y = "4" # 문자 타입
# print(x+y) < 에러 발생
print(str(x) + y) # 문자열이기 때문에 4와 4가 붙여서 출력 : 44
print(x + int(y)) # 숫자이므로 사칙연산 발생 : 8
print("\n")


# 불리안(boolean) : True or False 
print("4. 불리안(boolean)")
x = True
y = False
print(x)
print(y)
print("\n")

# 조건문(if,else)
print("5. 조건문(if,else)")

if 2 > 1:
  print("2는 1보다 큽니다.")

if not 1 > 2:
  print("1은 2보다 크지 않습니다.")

if 0 > 0 and 2 > 1: # 둘 다 참이어야만 실행됨
  print("Hello")

if 0 > 0 or 2 > 1: # 하나가 참이어도 실행됨
  print("Hello")

x = 3
if x > 5:
  print("x는 5보다 큽니다")
elif x == 3: # 이게 아니면 else로 넘어간다.
  print("x는 3입니다.")
else:
  print("x는 5보다 크지 않습니다")
print("\n")

# 함수(function)
print("6. 함수(function)" )

# 함수 응용1
def chat(name1, name2, age):
  print("%s : 안녕? 넌 몇살이니?" % name1)
  print("%s: 나? 나는 %d" % (name2,age))

chat("알렉스","윤하",20)
chat("철수","영희",10)
print("\n")

# 함수 응용2
def dsum(a, b):
  result = a + b
  return result 
  
d = dsum(1, 2)
print(d)
d = dsum(2, 4)
print(d)
print("\n")
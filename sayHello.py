# 먼저 이름과 나이를 받아라
# 나이가 10살 미만이면 "안녕" 이라고 말해라
# 나이가 10살에서 20살 사이면 "안녕하세요" 라고 말해라
# 그 외에는 "안녕하십니까" 라고 말해라

def sayHello(name, age):
  if age < 10:
    print("안녕, " + name)
  elif 10 <= age and age < 20:
    print("안녕하세요, " + name)
  else:
    print("안녕하십니까, " + name)
  
  sayHello("병준", 9)
  sayHello("알렉스", 20)
  sayHello("윤하", 30)
  

  print("Hello")
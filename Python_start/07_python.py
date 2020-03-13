# 반복문
print("7. 반복문\n")

# for, while
# for
for i in range(3): # range(수) : 수만큼 반복해라
    print(str(i) + " 반복중 ..." )
    print("철수: 안녕 영희야 뭐해?")
    print("영희: 안녕 철수야, 그냥 있어.")
print("\n")


i = 0
# while
while i < 3:
    print(i)
    print("철수: 안녕 영희야 뭐해?")
    print("영희: 안녕 철수야, 그냥 있어.")
    i = i + 1

# 무한루프 끝내기(break, continue)
while True:
    print(i) # 0
    print("철수: 안녕 영희야 뭐해?")
    print("영희: 안녕 철수야, 그냥 있어.")
    i = i + 1
    if i > 2:
        break # 강제 종료

for i in range(100):
    print(i) # 0
    print("철수: 안녕 영희야 뭐해?")
    print("영희: 안녕 철수야, 그냥 있어.")

    if i == 1:
        continue
    # 병준이가 말을 하지 않게 continue
    print("병준: 안녕 철수와 영희야!")

# 2020.03.13
# 두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.

# 첫째 줄에 A와 B가 주어진다.
# 첫째 줄에 A-B를 출력한다

C=input().split()
A=int(C[0])
B=int(C[1])
print(A-B)


# 후기
# 초기에 input으로 받다보니 런타임에러가 발생하였다.
# 문제는 한 줄에 A와 B사이의 공백까지 받는 것이었다.
# 해결로는 split()을 이용해 int형식으로 바로 받아주어 해결하였다.
#함수 안에서 선언한 변수의 효력 범위
#vartest.py
a = 1 #함수 밖에 변수 a
def vartest(a):
    a = a + 1

vartest(a) #vartest 함수의 입력값으로 a를  줌
print(a) #a값 출력 
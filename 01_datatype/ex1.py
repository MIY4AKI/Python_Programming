# 변수
a = 2
b = 3
print(a, b)

# a = 2, b = 3
# a = (2, b) = 3 => 튜플
a = 2
b = 3
a, b = 2, 3  # 권장
# 위에서 2, 3 은 튜플이 맞음. 그 값을 a, b 에 넣는 boxing 하는거
print(a, b)

# 값 swap
temp = a
a = b
b = temp
print(a, b)

a, b = b, a  # 이렇게도 스왑 가능
print(a, b)

x = y = z = 0

# 변수명 규칙 (C와 동일)
# 숫자로 시작 불가
# 예약어 사용 금지
# 알파벳, 숫자, 특수문자(_)만 가능
# 대소문자 구분

# 2name = "뽀로로"
# !name = "크롱"
# class = "루피"

이름 = "에디"
print(이름)  # 비권장 / 가능은 함

student_name = "루피"  # snake_case 권장
studentName = "포비"  # camelCase

MAX_SCORE = 100  # 상수처럼 쓰임 / 상수는 대문자로

# for문

# C language
# for (int i=0;i<=10;i++)

# Python
# for i in iterable객체:

# 0 ~ 4
for i in range(5):
    print(i, end=" ")
print()

a = range(5)
print(a.start, a.stop, a.step)

# 1 ~ 5
for i in range(1, 6):
    print(i, end=" ")
print()

# 0 2 4 6 8
for i in range(0, 11, 2):
    print(i, end=" ")
print()

for i in range(5, 0, -1):
    print(i, end=" ")
print()

# 1 ~ 10 까지의 합
tot = 0

for i in range(1, 11):
    tot += i
print(tot)

print(sum(range(1, 11)))

s = "hi12!@한글韓子"

for c in s:
    print(c, end=" ")

print(len(s))

# 구구단 출력
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i*j}", end="\t")
    print()

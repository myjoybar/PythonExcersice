# -*- coding: utf-8 -*-
#coding=utf-8

print("=====================斐波纳契数列=====================")
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b


print("=====================Python3 条件控制=====================")
age = int(input("请输入你家狗狗的年龄: "))
print("")
if age < 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("对应人类年龄: ", human)

### 退出提示
input("点击 enter 键退出")

print("=====================while 循环=====================")
n = 100

sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1

print("1 到 %d 之和为: %d" % (n, sum))

print("=====================for 语句=====================")

languages = ["C", "C++", "Perl", "Python"]
for x in languages:
    print (x)

print("=====================range()函数=====================")

for i in range(5):
     print(i)

print("=====================range()函数=====================")

for j in range(5):
     print(j)

print("=====================指定不同的增量=====================")

for k in range(0, 10, 3):
     print(k)


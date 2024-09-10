number = int(input("请输入数字: "))  # input用于获取键盘输入
print(number)
print(type(number))  # input获得的数据是字符型

print(number + 10)  # 报错，不能把字符和数字做运算10
print(int(number) + 10)  # int可将字符串10转换成数字10
print(str(number) + str(10))  # str将10转换为字符串后实现字符串拼接


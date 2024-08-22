# item = [["cornflakes", 1.65], ["rice krispies", 1.50], ["weetabix", 1.60], ["oatmeal", 2.88830]]
# searchItem = input("Enter your wanted item: ")

# for i in item:
#     if searchItem == i[0]:
#         print(round(i[1], 2))
#         break

# print(sum([ord(d)-ord('a')for d in "abcd"]))
# import math as mt
# x = 3
# y = 7%5

# def main():
#     x= 5
#     y=2

# main()

# if y == 2:
#     x = 3
# a = math.root(x+y)
# print(x+y)

# sum = 0
# count = 0
# for value in [9, 41, 12, 3, 74, 15]:
#     sum += value
#     count+=1

# print(sum, count, int(sum/count))


# class Add:
#     fir=0
#     sen=0
#     ans=0
#     def __init__(self,f,s):
#         self.fir=f
#         self.sen=s
#     def cal(self):
#         self.ans=self.fir+self.sen
#     def dis(self):
#             print(self.ans)

# obj= Add(1000, 2000)
# obj.dis()

# x ="HKICO"
# y = "2022"

# var=x+y
# print(var[2])

# def main(number):
#     if(number == 0):
#         return 0
#     elif (number == 1):
#         return 1
#     else:
#         return (main(number - 2)+ main(number - 1))

# number = int(input("Enter A Number: "))
# for n in range(0, number):
#     print(main(n))

# str = "pynative"
# print(str[1:3])

var = 10
for i in range(10):
    for j in range(2, 10, 1):
        if var % 2 == 0:
            continue
            var += 1
    var+=1

else:
    var+=1
print(var)
#1.
# double a = input.nextDouble()
# double b = input.nextDouble()
# double c = input.nextDouble()
#         System.out.print("要求解的方程为：" + a + "*x*x + " +
#                 b + "*x + " + c + " = 0")
#         System.out.println("\n方程的判别式为:" + equation.getDiscriminant(a,b,c));
 
#         if(equation.getDiscriminant(a,b,c) >= 0) 
#             System.out.println("\n方程的根为：" + equation.getRoot1(a,b,c) +
#                     " " + equation.getRoot2(a,b,c))
#         else:
#             System.out.println("The equation has no roots...")

#2.
# for a in range(0,100): 
#     a = int(input('请输入第一个数：'))
# for b in range(0,100): 
#     b = int(input('请输入第一个数：'))
# int c:
# if (c == a+b):
#     print('true')
# else：
#     print('false')

#3.

# today = int(input('Enter todays day:'))
# count = int(input('Enter the number of days elapsed since today:'))
# fd=count%7
# b=today+fd
# c=b%7
# print('Today is 星期%d and the future day is 星期%d' %(today,c))

#4.
# a = [8,6,2]
# a.sort()
# print(a)
# 5.
# def contrast(money1,weight1,money2,weight2)
# dami1 = money1 / weight1
# dami2 = money2 / weight2
# if dami1 > dami2:
#     print("第二种大米价格好")
# elif dami1 < dami2:
#     print("第一种大米价格好")
# else:
#     print("两种大米一样好")  
# money1 = float(input("请输入第一种大米的价格:"))
# weight1 = float(input("请输入第一种大米的重量："))
# money2 = float(input("请输入第二种大米的价格:"))
# weight2 = float(input("请输入第二种大米的重量："))
#6.
# def day(year,month):
# days = ['null','31','29','31','30','31','30','31','31','30','31','30','31']
# sum = days[month]
# print("%d年%d月份有%s天" %(year,month,sum))
# def start():
# year = int(input("请输入年份："))
# month = int(input("请输入月份："))
# day(year,month)
#7. 
# import random
# def pan(pao,cai):
#     print("硬币谈起方向%d"%pao)
#     if pao == cai:
#         print("恭喜你，答对了！")
#     else：
#         print("很遗憾，答错了！")
# pao = random.random
# cai = int(input("你猜测的结果是[1.正面 2.反面]："))
# pan(pao,cai)
#8.
# import random
# user = int(input("剪刀(0), 石头(1), 布(2):"))
# comp = random.randint(0,2)
# print(comp)
# if (user==1 and comp==0) or (user==0 and comp==2) or (user==2 and comp ==1):
#     print("你赢了")
# elif user==comp:
#      print("平局")
# else：
#      print("你输了")
#9.
# year = int(input('输入那一年:'))
# m = int(input('输入月份：'))
# d = int(input('输入第几天：'))
# a = ['周六','周日','周一','周二','周三','周四','周五']
# if m == 1:
#     m == 13
#     year = year - 1
# if m == 2:
#     m = 14
#     year = year - 1
# h = int(d+((26*(m+1))//10)+(year%100)+(year%100)/4)+((year//100)/4)+5*year//100)%7
# day = a[h]
# print('那一天是一周中的：%s' %day)
#10.
# import numpy as np
# daxiao=np.random.choice(['ace','2','3','4','5','6','7','8','9','10','jack','queen','king'])
# huase=np.random.choice(['梅花','红桃','方块','黑桃'])
# print('你选择的牌是',huase,daxiao)

# a = input('是否决定抽牌y/n:')
# if a == 'y':
#     chou()
# else:
#     pass
#11.
# a = int(input('请输入一个正整数：'))
# b = a
# a2 = 0
# while b > 0:
#     a2 *= 10
#     a2 += b % 10
#     b //= 10
#     if a == a2：
#         print('%d是回文数' % a)
#     else:
#         print('%d不是回文数' % a)
#12.
# a = float(input('请输入第一条边长'))
# b = float(input('请输入第二条边长'))
# c = float(input('请输入第三条边长'))
# if a+b>c and a+c>b and b+c>a:
#     L = a+b+c
#     print('其周长为',L)
# else:
#     print('不是三角形三条边')

#13.

#14.
# money = 10000
# i = 1
# if i < 10:
#     money += money*5/100
#     i += 1
#     print(money)
#15.
# count = 0
# for i in range(100,1000):
#     if i % 5 == 0 and i % 6 == 0:
#         print(i,end ="")
#     count += 1
#     if count % 10 == 0:
#         print()
#16.


# a=1
# while a<10:
#     for i in range(a):
#         b=i+1
#         if a>=b:
#             print(f"{b}×{a}={a*b}",end="\t")
#     a+=1
#     print()
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j}×{i}={i*j}",end="\t")
#     print()

# import random
# num=random.randint(1,100)
# user_name=0
# while user_name!=num:
#     user_name=int(input("请输入1—100以内随机的一个数："))
#     if user_name<num:
#         print("小了")
#     elif user_name>num:
#         print("大了")
#     elif user_name==num:
#         print("恭喜你！猜中了！")
#         break
#     else:
#         print("请输入正确的数字！")

# a=[55,66,55,54,6,56,4,5,5]
# del a[1]
# print(a[1])
# for i in a:
#     print(i,end=" ")

# a=[55,66,55,54,6,56,4,5,5]
# print(a[0:5:1])
# a=[55,66,55,54,6,56,4,7,5]
# a.append(67)
# a.insert(1,77)
# a.remove(55)
# a.pop(4)
# a.sort()
# print(a)
# i=0
# b=[]
# while True:
#     if i<10:
#         a=int(input("请输入10个数，每输入完一个点击“enter”："))
#         if a==None or a>101:
#             print("请输入正确的数字！")
#             continue
#         b.append(a)
#         i+=1
#     else:
#         break
# b.sort()
# result=0
# for j in range(10):
#    result+=b[j]
# out_result=result/10
# print("最大值：",b[9])
# print("最小值：",b[0])
# print("平均值：",out_result)

# list1=[19,23,54,64,875,20,109,232,123,54]
# list2=[55,80,72,35,60,123,54,29,91]
# num_list=list1+list2          #解包操作
# # for num in list2:
# #     list1.append(num)
# new_list=[]
# for num in num_list:
#     if num not in new_list:
#         new_list.append(num)
# new_list.sort()
# print(new_list)
# a=[]
# for i in range(1,21):
#     num=i*i
#     a.append(num)
# print(a)
# num_list=[19,23,54,64,87,20,109,232,123,43,26,55,72]
# new_list=[]
# for num in num_list:
#     if num%2==0:
#         b=num*num
#         new_list.append(b)
# print(new_list)

# num_list=[i**2 for i in range(1,21)]
# print(num_list)

# s="skajsal"
# print(s[:2])
# index=s.find('a')
# print(index)
# num=s.count("s")
# print(num)
# a=s.upper()
# print(a)
# s1=s.split('s')
# print(s1)

# while True:
#     user_email=input()
#     index1=user_email.find('@')
#     index2=user_email.find('.')
#     user_name=user_email[0:index1-1]
#     user_adress=user_email[index1+1:]
#     if index1==-1 or index2==-1:
#         print("邮箱格式错误！请重新输入！")
#     else:
#         print("邮箱格式正确!")
#         break


# while True:
#     user_email=input()
#     index1=user_email.find('@')
#     index2=user_email.find('.')
#     user_name=user_email[0:index1-1]
#     user_adress=user_email[index1+1:]
#     if '.' in user_email and '@' in user_email:
#         print("邮箱格式正确")
#     else:
#         print("邮箱格式错误")
#         break

# user_input=input()
# i=0
# judge=True
# while i<len(user_input):
#     if user_input[i]==user_input[len(user_input)-i-1]:
#         i+=1
#     else:
#         judge=False
#         break
# if judge==True:
#     print("好诗")
# elif judge==False:
#     print("不妙")

# user_input=input()
# if user_input==user_input[::-1]:
#     print("好诗！")
# else:
#     print("不妙！")

# tuple1=(1,5,7,9,7,94,8,4,5,58)
# print(tuple1.index(7))
# list1=[19,23,54,64,875,20,109,232,123,54]
# print(list1.index(19))
# tuple1[0]=20    #元组的值是不可修改的
# print(tuple1)

# t1=(1,25,4,8,4)
# t2=(2,12,5,4,78,44)
# a,b,c,d,e=t1
# f,*g=t2
# print(a)
# print(g)

# student=(("yz",55,66),("lsa",65,87),("skoa",54,59))
# for i in student:
#     total=i[1]+i[2]
#     average=total/2
#     print(f"{i[0]}总分：{total} 平均分：{average:.0f}")
# result1=0
# result2=0
# list1=[]
# list2=[]
# for i in student:
#     result1+=i[1]
#     result2+=i[2]
#     list1.append(i[1])
#     list2.append(i[2])
# average1=result1/3
# average2=result2/3
# list1.sort()
# list2.sort()
# print(f"语文平均分：{average1:.1f},最高分：{list1[0]},最低分：{list1[2]}")
# print(f"数学平均分：{average2:.1f},最高分：{list2[0]},最低分：{list2[2]}")

# a=()#空元组
# b=set()#空集合
# b={5,4,6,5,8,48,2,5} #无序的，不支持索引访问
# print(b)
# b.clear()
# b.add(5)
# print(b)
# b.remove(5)
# print(b)
# b.add(5)
# c=b.pop()
# print(c)
# 选修足球学生名单
# football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}

# # 选修篮球学生名单
# basketball_set = {"张铁", "墨居仁","王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}

# # 选修法语学生名单
# french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}

# # 选修艺术学生名单
# art_set = { "遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}

#交集intersection   并集union
# student=french_set.intersection(art_set)
# for i in student:
#     print(i,end=" ")
# student2=student.intersection(basketball_set)
# student3=student2.intersection(football_set)
# for i in student3:
#     print(i)
# student4=basketball_set.intersection(football_set)
# student5=basketball_set-student4
# print(student5)
# all_student=football_set.union(basketball_set,art_set,french_set)
# for i in all_student:
#     num=0
#     if i in football_set:
#        num+=1
#     if i in basketball_set:
#         num+=1
#     if i in french_set:
#         num+=1
#     if i in art_set:
#         num+=1
#     print(f"{i}一共选了{num}节课")
# all_student=football_set.union(basketball_set,art_set,french_set)
# stu_list=[*football_set,*basketball_set,*french_set,*art_set ]
# for i in all_student:
#       print(f"{i}一共选修了{stu_list.count(i)}")

# dict={0:650,1:608,2:580,3:688,3:666}
# print(dict)
# print(dict[0])
# dict[0]=688
# print(dict)
# dict={0:650,1:608,2:580,3:688,3:666}
# c=dict.pop(0)
# print(c)
# del dict[1]
# print(dict)
# dict[0]=555
# dict[1]=666
# dict[1]=888
# print(dict)
# print(dict.keys())
# print(dict.values())
# print(dict.items())
# a=dict.get(0)
# print(a)

# print("欢迎进入购物车管理系统！")
# for i in range(10):
#     print("*",end=" ")
# print("""
      
# 1、添加购物车
# 2、修改购物车
# 3、删除购物车
# 4、查询购物车
# 5、退出系统
# """)
# for i in range(10):
#     print("*",end=" ")
# Shopping_Cart=dict()
# while True:
#     user_input=int(input("请输入你要进行的操作序号："))
#     while user_input==1:
#         goods_name=input("请输入您的商品信息（输入q或quit可以退出）：")
#         if goods_name=='q' or goods_name=='quit':
#             break
#         goods_price=int(input("请输入商品价格："))
#         goods_quantity=int(input("请修改商品数量："))
#         goods_list=[]
#         goods_list=[goods_price,goods_quantity]
#         Shopping_Cart[goods_name]=goods_list
#         print("添加成功")
#     while user_input==2:
#         if Shopping_Cart==dict():
#             print("您的购物车目前为空！")
#             break
#         goods_name=input("请输入要修改的商品名称（输入q或quit可以退出）：")
#         if goods_name=='q' or goods_name=='quit':
#             break
#         print(f"{goods_name}:{Shopping_Cart.get(goods_name)}")    
#         goods_price=int(input("请输入你要修改的价格："))
#         goods_quantity=int(input("请输入你要修改的数量："))
#         goods_list=[]
#         goods_list=[goods_price,goods_quantity]
#         Shopping_Cart[goods_name]=goods_list
#         print("修改成功！")
#     while user_input==3:
#         if Shopping_Cart==dict():
#             print("您的购物车目前为空！")
#             break
#         goods_name=input("请输入要删除的商品名称（输入q或quit可以退出）：")
#         if goods_name=='q' or goods_name=='quit':
#             break
#         del Shopping_Cart[goods_name]
#         print("删除成功！")
#     if user_input==4:
#         if Shopping_Cart==dict():
#             print("您的购物车目前为空！")
#             break
#         for key, value in Shopping_Cart.items():
#             print(f"商品名称：{key}，商品价格{value[0]},商品数量{value[1]}")
#     if user_input==5:
#        break
# print("欢迎下次再来！")


# def rectangle_area(l,w):
#     return l*w
# print(rectangle_area(3,4))
# a=input()
# def vowel_letter(a):
#     count=0
#     for i in a:
#         if i in "aeiouAEIOU":
#             count+=1
#     return count
# print(vowel_letter(a))

# def class_score(score_list):
#     min_s=min(score_list)
#     max_s=max(score_list)
#     avg_s=round(sum(score_list)/len(score_list),1)
#     return min_s,max_s,avg_s       #返回一个元组

# def judge_word(a):
#     return a==a[::-1]
# a=input()
# print(judge_word(a))

# def judge_data(*args,**kwargs):
#     min_data=min(args)
#     max_data=max(args)
#     avg_data=sum(args)/len(args)
#     if kwargs.get('round') is not None:
#         avg_data=round(avg_data,kwargs.get("round"))
#     return min_data,max_data,avg_data
    
# def add(a,b):
#     return a+b
# def calc(x,y,ope):
#     return ope(x,y)
# s=calc(3,4,add)
# print(s)

# out_put=lambda:print('........')
# add=lambda x,y:x+y
# print(add(3,4))
# print(out_put())
# data_list=["C++","C","python","Jack","PHP","Java","Go","JavaScript","Rust"]
# data_list.sort(key=lambda item:len(item),reverse=True)
# print(data_list)

# def f(n):
#     if n==1:
#         return 1
#     else:
#         return n*f(n-1)
# print(f(5))



# print("请在下方窗口填写商品信息！")
# def user_cost(lists,integral,shipping_cost):
#     if not lists:
#         return 0
#     goods_cost=sum(lit[1]*lit[2] for lit in lists)
#     if goods_cost>=5000:
#         if integral>=100:
#             return goods_cost*0.9-integral//100+shipping_cost
#         else:
#             return goods_cost*0.9+shipping_cost
#     else:
#         return goods_cost+shipping_cost
# all_list=[]
# while True:
#     goods_name=""
#     goods_price=0
#     goods_quantity=0
#     goods_name=input("请输入商品名称（输入'q'或'quit'退出）：")
#     if goods_name=='q'or goods_name=="quit":
       
#        break
#     goods_price=int(input("请输入商品单价："))
#     goods_quantity=int(input("请输入商品数量："))
#     user_list=[goods_name,goods_price,goods_quantity]
#     all_list.append(user_list)
# print("你需要支付：",user_cost(all_list,219,10))

# print("=" * 40)
# print("     欢迎进入购物车结账系统")
# print("=" * 40)

# ============ 商品列表 ============
# # 每个商品是一个列表：[名称, 单价, 数量]
# shopping_list = []

# # ============ 添加商品 ============
# while True:
#     print("\n--- 添加商品 ---")
#     name = input("请输入商品名称（输入 q 退出）：")
    
#     if name == 'q' or name == 'quit':
#         break
    
#     price = int(input("请输入商品单价："))
#     quantity = int(input("请输入商品数量："))
    
#     # 添加到购物车（每条记录是一个列表）
#     shopping_list.append([name, price, quantity])
#     print(f"✅ 已添加：{name} × {quantity}，单价 {price}元")

# # ============ 查看购物车 ============
# print("\n" + "=" * 40)
# print("          您的购物车")
# print("=" * 40)

# if not shopping_list:
#     print("购物车为空！")
# else:
#     total = 0
#     print("商品名称\t单价\t数量\t小计")
#     print("-" * 40)
    
#     for item in shopping_list:
#         name = item[0]
#         price = item[1]
#         quantity = item[2]
#         subtotal = price * quantity
#         total += subtotal
#         print(f"{name}\t\t{price}\t{quantity}\t{subtotal}")
    
#     print("-" * 40)
#     print(f"商品总价：{total}元")

# # ============ 计算运费 ============
# if total >= 100:
#     shipping = 0
#     print("✅ 满100元，免运费！")
# else:
#     shipping = 10
#     print(f"运费：{shipping}元")

# # ============ 计算折扣 ============
# user_points = 219  # 用户积分
# final_total = total

# if total >= 500:
#     print("🎉 满500元，享受9折优惠！")
#     final_total = total * 0.9
#     print(f"折扣后：{final_total:.2f}元")
    
#     if user_points >= 100:
#         points_discount = user_points // 100
#         final_total -= points_discount
#         print(f"💳 使用积分抵扣 {points_discount}元")
#         print(f"积分抵扣后：{final_total:.2f}元")

# # ============ 加上运费 ============
# final_total += shipping

# # ============ 输出最终结果 ============
# print("\n" + "=" * 40)
# print(f"💰 您需要支付：{final_total:.2f}元")
# print("=" * 40)
# print("欢迎下次光临！)

# import units.my_pp
# a=units.my_pp.add(3,4)
# print(a)

# class car:
#     pass
# c1=car()
# c1.bread="BMW"
# c1.name="X5"
# c1.price=500000
# print(c1.__dict__)        #__dict__类的自定义属性

# class car:
#     def __init__(self,c_name,c_age):   #__init__初始化
#         self.name=c_name
#         self.age=c_age
# c1=car("BMW",20)

# class car:
#     wheel=4
#     tax_rate=0.1  #类属性
#     def __init__(self,c_name,c_price,c_brand):
#         self.name=c_name
#         self.price=c_price
#         self.brand=c_brand
#         self.wheel=2
#     # def running(self):
#     #     print(f"{self.name}正在奔跑")
#     # def total_cost(self,discount,rate):
#         # return self.price*discount+self.price*rate*12
#     def __str__(self):
#         return f"{self.brand} {self.name} {self.price}"
#     def __eq__(self,other):
#         return self.price==other.price and self.brand==other.brand and self.name==other.name
#     def __lt__(self,other):
#         return self.price<other.price
# c1=car("宝马",500000,"宝马")
# print(c1)

# c2=car("宝马",500000,"宝马")
# print(c2)
# print(c1==c2)
# print(c1<c2)
# # c1.running()
# # result=c1.total_cost(0.9,0.001)
# # print(f"应付{result}")
# print(c1.wheel)
# print(car.wheel)

# try:
#     print("=================")
#     print(my_name)
#     print("=================")
# except NameError as e:
#     print("程序异常：",e)





































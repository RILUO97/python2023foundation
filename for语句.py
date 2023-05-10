# for循环遍历序列
# （1）for循环遍历字符串
# s= 'python'
# for a in s:
#     print(a+'*')
#     print(f'当前字母是{a}')

# for 循环遍历列表

# l = ['apple','banana','dog']
# for i in l:
#     print(i+'*')
#     print(f'当前遍历出的元素是{i}')

# for 循环获取索引和值
# for i,v in enumerate(l):
#     print(f'获取的索引是{i}')
#     print(f'获取的值是{v}')


# for 循环和range()
# 获取0-10之间的偶数包含10
# for i in range(0,11,2):
#     print(i)

# for循环打印99乘法表
# 行 第m行 第一个乘数是m 第二个乘数是1-m
# 列 第n列 第一个乘数是1-n  第二个是n
for n in range(1,10):
    for m in range(1,n+1):
        print(f"{n}*{m}={n*m}",end='  ')
    print()
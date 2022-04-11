# 本程序用于绘制饼状图
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文显示
plt.figure(figsize=(6, 6))   # 将画布设定为正方形，则绘制的饼图是正圆
label = ['悲类型：7092首', '喜类型：33964首']   # 定义饼图的标签，标签是列表
explode = [0.01, 0.01]     # 设定各项距离圆心n个半径
values = [7092, 33964]
plt.pie(values, explode=explode, labels=label, autopct='%1.1f%%')  # 绘制饼图
plt.title('唐代喜悲类型词饼图')  # 绘制标题
plt.savefig('唐代喜悲类型词饼图')    # 保存图片
plt.show()
plt.figure(figsize=(6, 6))
label = ['悲类型：101565首', '喜类型：152683首']   # 定义饼图的标签，标签是列表
explode = [0.01, 0.01]     # 设定各项距离圆心n个半径
values = [101565, 152683]
plt.pie(values, explode=explode, labels=label, autopct='%1.1f%%')  # 绘制饼图
plt.title('宋代喜悲类型词饼图')  # 绘制标题
plt.savefig('宋代喜悲类型词饼图')    # 保存图片
plt.show()
import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# s是点的大小,edgecolors='none'是删除数据点的轮廓
# plt.scatter(x_values, y_values, c='red', edgecolors='none', s=40)
# 颜色映射，y值较小的点为浅蓝色，y值较大的点显示为深蓝色
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)

# 设置图标标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

plt.show()

# 自动保存图表
# plt.savefig('squares_plot.png', bbox_inches='tight')
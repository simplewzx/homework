import pandas as pd
import matplotlib.pyplot as plt

# 存储路径
save_path='D:/研究生/数据与知识工程/作业1/5'

# 读取数据
data = pd.read_excel('餐饮数据.xlsx')

# 将purchase_time列转换为日期时间格式
data['purchase_time'] = pd.to_datetime(data['purchase_time'])

# 提取配送时间（假设service-time列格式为'X分钟送达'，提取其中的分钟数）
data['delivery_time'] = data['service-time'].str.extract(r'(\d+)分钟送达').fillna(0).astype(int)

# 计算配送时间的基本统计信息
print(data['delivery_time'].describe())

# 设置中文字体为黑体
plt.rcParams['font.sans-serif'] = ['SimHei']

# 解决负号显示问题
plt.rcParams['axes.unicode_minus'] = False

# 绘制配送时间直方图并保存
plt.hist(data['delivery_time'], bins=20, edgecolor='black')
plt.xlabel('配送时间（分钟）')
plt.ylabel('订单数量')
plt.title('配送时间分布')
plt.savefig(save_path)  # 保存直方图到当前目录，可根据需要修改路径
plt.show()
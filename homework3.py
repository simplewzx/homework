import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件中的数据
data = pd.read_excel('餐饮数据.xlsx')

# 将purchase_time列转换为日期时间格式
data['purchase_time'] = pd.to_datetime(data['purchase_time'])

# 按日期统计订单数量
order_count_by_date = data.groupby(data['purchase_time'].dt.date)['comment_id'].count().reset_index()
order_count_by_date.columns = ['date', 'order_count']

# 设置中文字体为黑体，解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 数据可视化
plt.figure(figsize=(12,8))
plt.plot(order_count_by_date['date'], order_count_by_date['order_count'])
plt.xlabel('日期')
plt.ylabel('订单数量')
plt.title('日期对订单数量的影响')
plt.xticks(rotation=45)

# 存储图表
save_path='D:/研究生/数据与知识工程/作业1/3.png'
plt.savefig(save_path)
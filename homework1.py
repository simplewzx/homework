import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

# 设置字体，并读取文件
font_path = 'C:\\Windows\\Fonts\\simfang.ttf'
prop = font_manager.FontProperties(fname=font_path)
plt.rcParams['font.family'] = prop.get_name()
data1 = pd.read_excel('餐饮数据.xlsx',sheet_name='sheet1')

# 忽略product1_name中为空的数据
df = data1[data1['product1_name'].notnull()]

# 统计每个餐馆的订单数量，作为销量衡量
r_name = data1['title'].value_counts()[:10]

# 设置图片大小
df = pd.DataFrame(r_name)
plt.figure(figsize=(12, 12))

# 画出折线图
plt.plot(df.index, df['count'], 'r-o', linewidth=2)

# 画出柱状图
plt.bar(df.index, df['count'])
plt.xlabel('餐馆名称')
plt.ylabel('数量')
plt.title('销量前十的餐馆')
plt.xticks(rotation=45)

# 在绘制的图表中添加网格线
plt.grid(True)

# 存储图表
save_path='D:/研究生/数据与知识工程/作业1/1.png'
plt.savefig(save_path)

import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
data = pd.read_excel('餐饮数据.xlsx')

# 统计每个餐厅的订单数量
restaurant_orders = data['title'].value_counts()

# 选择销量前十的餐厅
top_ten_restaurants = restaurant_orders.head(10).index

# 定义评价分类函数
def categorize_rating(rating):
    if '满意' in rating:
        return '满意'
    elif '惊喜' in rating:
        return '惊喜'
    elif '一般' in rating:
        return '一般'
    elif '失望' in rating:
        return '失望'
    elif '极差' in rating:
        return '极差'
    else:
        return '其他'

# 存储每个餐馆评价分类计数的字典
restaurant_rating_counts = {restaurant: {category: 0 for category in ['满意', '惊喜', '一般', '失望', '极差', '其他']} for restaurant in top_ten_restaurants}

# 统计每个餐馆的评价分类计数
for restaurant in top_ten_restaurants:
    restaurant_ratings = data[(data['title'] == restaurant) & (data['product1_comment'].notnull())]['product1_comment']
    for rating in restaurant_ratings:
        category = categorize_rating(rating)
        restaurant_rating_counts[restaurant][category] += 1

# 设置图片大小
plt.figure(figsize=(11, 6))

# 设置中文字体为黑体
plt.rcParams['font.sans-serif'] = ['SimHei']

# 解决负号显示问题
plt.rcParams['axes.unicode_minus'] = False

# 设置柱状图宽度
bar_width = 0.15

# 设置每个餐馆在x轴上的位置
positions = range(len(top_ten_restaurants))

# 绘制柱状图
for i, category in enumerate(['满意', '惊喜', '一般', '失望', '极差', '其他']):
    counts = [restaurant_rating_counts[restaurant][category] for restaurant in top_ten_restaurants]
    plt.bar([pos + i * bar_width for pos in positions], counts, width=bar_width, label=category)

# 设置x轴标签为餐馆名称
plt.xticks([pos + bar_width * 2.5 for pos in positions], top_ten_restaurants, rotation=45)

plt.xlabel('餐馆')
plt.ylabel('数量')
plt.title('销量前十餐厅评价分布')
plt.legend()

# 调整图表布局
plt.tight_layout()

# 存储图表
save_path='D:/研究生/数据与知识工程/作业1/4.png'
plt.savefig(save_path)
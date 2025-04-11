import pandas as pd
import matplotlib.pyplot as plt
import os

def creat_frame():
    """
    创建一个包含学生信息的DataFrame并保存为CSV文件。
    """
    data = {
        '姓名': ['张三', '李四', '王五', '赵六', '陈七'],
        '年龄': [25.0, 30.0, None, 22.0, 28.0],
        '成绩': [85.5, 90.0, 78.5, 88.0, 92.0],
        '城市': ['北京', '上海', '广州', '深圳', '上海']
    }
    df = pd.DataFrame(data)
    # 确保目录存在
    os.makedirs('../data', exist_ok=True)
    df.to_csv('../data/data.csv', index=False, encoding='utf-8')

def load_data():
    """任务1: 读取数据文件"""
    df = pd.read_csv('../data/data.csv')
    return df

def show_basic_info(data):
    """任务2: 显示数据基本信息"""
    print("=== 数据前五行 ===")
    print(data.head())
    print("\n=== 数据形状 ===")
    print(data.shape)
    print("\n=== 各列数据类型 ===")
    print(data.dtypes)
    print("\n=== 缺失值统计 ===")
    print(data.isnull().sum())

def handle_missing_values(data):
    """任务3: 处理缺失值"""
    mean_age = data['年龄'].mean()
    data['年龄'] = data['年龄'].fillna(mean_age)
    print("\n=== 缺失值填充后的年龄列 ===")
    print(data['年龄'])
    return data

def analyze_statistics(data):
    """任务4: 统计分析数值列"""
    print("\n=== 数值列统计信息 ===")
    print(data[['年龄', '成绩']].describe())

def visualize_data(data, column_name='成绩'):
    """任务6: 数据可视化"""
    plt.hist(data[column_name], bins=5, edgecolor='black')
    plt.title(f'{column_name}分布直方图')
    plt.xlabel(column_name)
    plt.ylabel('频数')
    plt.show()

def save_processed_data(data):
    """任务7: 保存处理后的数据"""
    data.to_csv('../data/processed_data.csv', index=False, encoding='utf-8')
    print("\n处理后的数据已保存至 data/processed_data.csv")

def main():
    """主函数，执行所有数据处理流程"""
    creat_frame()
    data = load_data()
    show_basic_info(data)
    data = handle_missing_values(data)
    analyze_statistics(data)
    visualize_data(data)
    save_processed_data(data)

if __name__ == "__main__":
    main()
